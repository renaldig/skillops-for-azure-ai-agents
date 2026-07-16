# Deployment Review Hosted Agent

This folder is a source-level reference for the toolbox-capable Foundry hosted agent used by the chapter. The manuscript's `azd ai agent init` command should scaffold the current Microsoft sample. Compare generated files with this folder rather than blindly replacing newer scaffold output.

## Important files

- `azure.yaml.reference`: example consolidated hosted-agent definition
- `src/skillops-toolbox-agent/main.py`: Responses protocol host and toolbox MCP connection
- `src/skillops-toolbox-agent/toolbox.yaml`: chapter-specific skill/toolbox definition
- `src/skillops-toolbox-agent/requirements.txt`: explicit Python dependencies
- `src/skillops-toolbox-agent/.env.example`: local environment values
- `src/skillops-toolbox-agent/Dockerfile`: optional transparent container build reference

Current Foundry samples can deploy Python code directly through `azure.yaml`, so the Dockerfile is not required by every generated scaffold. Keep it when your organization uses an explicit image build; otherwise, treat it as reference.

Replace `<skill-version>` with the immutable version returned by `azd ai skill list`. Use the version-specific toolbox MCP endpoint for local and deployed runs.
