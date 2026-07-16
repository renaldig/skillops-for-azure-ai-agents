# Azure App Service Deployment Review

- Skill ID: azure-app-service-deployment-review
- Owner: platform-team
- Status: Pilot
- Risk level: Medium
- Related services: Azure App Service, Key Vault, Application Insights
- Approved mode: Guidance and review only
- Repository version: 0.4.0
- Foundry skill: `<name> / <version>`
- Toolbox: `<name> / <version>`
- Hosted agent: `<name> / <version>`
- Evaluation record: `<evaluation-name>`
- Rollback target: `<agent-name> / <version>`

## Purpose
Helps developers review an Azure App Service deployment plan before release. The skill focuses on production readiness, identity, secrets, monitoring, health checks, deployment slots, rollback, and tagging.

## Out of scope
- AKS, Functions, or Container Apps deployments
- Assigning Azure RBAC roles
- Diagnosing live production incidents

## Example prompt
Review this App Service deployment plan for production readiness using the internal `azure-app-service-deployment-review` skill.

## Feedback
Open a repository issue or contact the platform team.
