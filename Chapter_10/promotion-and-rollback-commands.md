# Promotion and Rollback Command Reference

```bash
azd ai project set "https://<foundry-resource>.services.ai.azure.com/api/projects/skillops-foundry-sandbox"
azd ai skill update azure-ai-search-retrieval-design --file ../azure-internal-skills/skills/azure-ai-search-retrieval-design/SKILL.md --no-prompt
azd ai skill list --output table
azd ai toolbox create policy-retrieval-toolbox --from-file ./candidate-policy-retrieval-toolbox.yaml --no-prompt
azd ai toolbox show policy-retrieval-toolbox --output json
azd env set TOOLBOX_ENDPOINT "https://<foundry-resource>.services.ai.azure.com/api/projects/skillops-foundry-sandbox/toolboxes/policy-retrieval-toolbox/versions/<candidate-toolbox-version>/mcp?api-version=v1"
azd deploy
azd ai toolbox publish policy-retrieval-toolbox <candidate-toolbox-version> --no-prompt
# Rollback
azd ai toolbox publish policy-retrieval-toolbox <previous-toolbox-version> --no-prompt
```
