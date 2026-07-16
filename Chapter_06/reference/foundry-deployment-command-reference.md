# Foundry Deployment Command Reference

```bash
azd ext install microsoft.foundry
az login
azd auth login
azd ai project set "https://<foundry-resource>.services.ai.azure.com/api/projects/skillops-foundry-sandbox"
azd ai project show
azd ai skill create azure-deployment-validation-review --file ../azure-internal-skills/skills/azure-deployment-validation-review/SKILL.md --no-prompt
azd ai skill list --output table
azd ai toolbox create deployment-review-toolbox --from-file ./src/deployment-review-agent/toolbox.yaml --no-prompt
azd ai toolbox show deployment-review-toolbox --output json
azd ai agent run
azd provision
azd deploy
azd ai agent invoke "Review this deployment for validation readiness."
```
