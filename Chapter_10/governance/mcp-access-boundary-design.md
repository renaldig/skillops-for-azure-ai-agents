# MCP Access Boundary Design

- Workflow name: Azure Monitor investigation assistant
- Skill: azure-observability-investigation
- Purpose: Help developers investigate failed requests and latency issues for one application.
- Environment: Development and test only for the first pilot.
- Allowed behavior: Read telemetry and summarize evidence.
- Out-of-scope behavior: Restart services, change configuration, create alerts, assign roles, or access production telemetry.

## Identity boundary
Use a dedicated identity for the pilot. The identity should be owned by the platform or SRE team and kept separate from unrelated workflows.

## RBAC boundary
The identity should have read-only access only to the development and test observability resources required for the pilot. It should **not** have subscription-wide access or permission to modify resources.

## Tool boundary
Expose only Azure Monitor and Log Analytics read operations. Configure Azure MCP Server with the `monitor` namespace and `--read-only` for the local pilot.

## Human approval boundary
The assistant may summarize telemetry and suggest next steps. A human engineer must approve any action that changes Azure resources, changes alert configuration, restarts services, or escalates the workflow to production.
