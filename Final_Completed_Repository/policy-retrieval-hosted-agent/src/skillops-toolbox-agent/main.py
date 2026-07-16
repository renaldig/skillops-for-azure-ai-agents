# Educational adaptation of the Microsoft Foundry toolbox hosted-agent pattern.
import asyncio
import os
from collections.abc import Callable

import httpx
from agent_framework import Agent, MCPStreamableHTTPTool
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv()


def resolve_toolbox_endpoint() -> str:
    """Return a versioned toolbox MCP endpoint."""
    endpoint = os.environ.get("TOOLBOX_ENDPOINT")
    if endpoint is not None:
        if not endpoint.strip():
            raise ValueError("TOOLBOX_ENDPOINT is set but empty")
        return endpoint.rstrip("/")

    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    toolbox_name = os.environ["TOOLBOX_NAME"]
    return f"{project_endpoint}/toolboxes/{toolbox_name}/mcp?api-version=v1"


class ToolboxAuth(httpx.Auth):
    """Add a fresh Microsoft Entra bearer token to each toolbox request."""

    def __init__(self, token_provider: Callable[[], str]):
        self._get_token = token_provider

    def auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = f"Bearer {self._get_token()}"
        yield request


async def main() -> None:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    model_name = (
        os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME")
        or os.environ.get("FOUNDRY_MODEL_NAME")
    )
    if not model_name:
        raise ValueError(
            "Set AZURE_AI_MODEL_DEPLOYMENT_NAME or FOUNDRY_MODEL_NAME."
        )

    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential, "https://ai.azure.com/.default"
    )
    toolbox_endpoint = resolve_toolbox_endpoint()
    toolbox_name = (
        os.environ.get("TOOLBOX_NAME")
        or toolbox_endpoint.rsplit("/mcp", 1)[0].rsplit("/", 1)[-1]
    )

    async with httpx.AsyncClient(
        auth=ToolboxAuth(token_provider),
        headers={"Foundry-Features": "Toolboxes=V1Preview"},
        timeout=120.0,
    ) as http_client:
        toolbox = MCPStreamableHTTPTool(
            name=toolbox_name,
            url=toolbox_endpoint,
            http_client=http_client,
            load_prompts=False,
        )
        client = FoundryChatClient(
            project_endpoint=project_endpoint,
            model=model_name,
            credential=credential,
        )
        agent = Agent(
            client=client,
            instructions=(
                "Apply the approved SkillOps guidance exposed by the toolbox. "
                "Keep evidence, assumptions, and recommendations separate. "
                "Do not invent missing Azure or policy evidence."
            ),
            tools=toolbox,
            default_options={"store": False},
        )
        server = ResponsesHostServer(agent)
        await server.run_async()


if __name__ == "__main__":
    asyncio.run(main())
