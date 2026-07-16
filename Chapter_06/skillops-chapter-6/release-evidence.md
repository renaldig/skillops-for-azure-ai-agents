# Release Evidence for customer-feedback-api

- Target environment: staging
- Target service: Azure App Service
- Deployment method: planned through Azure Developer CLI
- Validation: deployment plan completed; Bicep validation not yet run
- What-if: not yet run
- Identity: managed identity planned for Azure SQL
- Secrets: Key Vault references planned, not yet configured
- Monitoring: Application Insights planned, smoke test not written yet
- Rollback: previous version can be redeployed, but command not recorded
- Owner: customer-experience platform squad
- Known risks: staging App Service plan SKU not confirmed
