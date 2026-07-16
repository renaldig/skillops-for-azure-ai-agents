---
name: azure-app-service-deployment-review
description: Review an Azure App Service deployment plan for production readiness, including identity, configuration, monitoring, rollout, and cost concerns.
compatibility: File-based Agent Skills hosts. Live Azure checks require separately configured read-only tools.
metadata:
  owner: cloud-platform
  maturity: draft
  version: 0.4.0
---
# Azure App Service Deployment Review
Use this skill when a user asks for help reviewing a planned Azure App Service deployment, preparing an App Service deployment checklist, or identifying missing production-readiness items for a web app or API.

Do not use this skill to approve a production deployment. Provide guidance, questions, and review findings only. Human review is required before production release.

## Review workflow
1. Identify the application type: web app, API, worker, or background service.
2. Identify the target environment: development, test, staging, or production.
3. Check whether the plan specifies the region, runtime stack, App Service Plan tier, and expected traffic pattern.
4. Check whether the app uses managed identity for Azure service access where appropriate.
5. Check whether secrets are stored in Key Vault or referenced securely instead of being copied into plain application settings.
6. Check whether Application Insights or another approved monitoring approach is included.
7. Check whether health checks, deployment slots, rollback steps, and release ownership are described for production workloads.
8. Check whether resource tags, cost ownership, and environment naming conventions are included.
9. Summarize missing information before making recommendations.

## Output format
When reviewing a production deployment, separate the output into:
1. Blockers
2. Recommendations
3. Open questions
4. Suggested next steps

Avoid calling the deployment production-ready if secret handling, identity, monitoring, health checks, or rollback expectations are unknown.
