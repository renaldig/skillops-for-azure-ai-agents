---
name: azure-deployment-validation-review
description: Guide an assistant through Azure deployment validation,
  quota checks, what-if review, identity checks, and release gates.
---
Use this skill when the user asks whether Azure deployment files
are ready, asks for pre-flight checks, or wants to validate before
running a deployment.
Required workflow:
1. Identify the target environment, subscription, resource group,
   region, and deployment method.
2. Inspect available deployment files such as Bicep, ARM JSON,
   Terraform, azure.yaml, pipeline YAML, or scripts.
3. List the resources that will be created or changed.
4. Recommend static checks for the file type.
5. Recommend Azure validation or what-if commands where relevant.
6. Check or request quota and regional availability information.
7. Review identity, secrets, monitoring, tagging, and cost risks.
8. Return a pass, warning, or stop decision.
Never tell the user to deploy if high-risk validation results are
missing, unknown, or failing. Ask for confirmation before any
command that creates, modifies, or deletes Azure resources.

## Internal expectations
- Production resources must have owner, application, environment, costCenter, and dataClassification tags.
- Runtime access to Azure services should use managed identity where supported.
- Secrets must not be stored in source code or committed files.
- New production workloads must include monitoring and alerts.
- What-if output must be reviewed before production deployment.
- A rollback or mitigation plan must exist before release.
