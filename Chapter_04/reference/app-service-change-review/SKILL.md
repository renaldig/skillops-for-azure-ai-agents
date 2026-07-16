---
name: app-service-change-review
description: Use this skill when reviewing an Azure App Service application change before release. Check hosting plan fit, configuration, identity, secrets, network exposure, monitoring, and rollback readiness.
compatibility: File-based Agent Skills hosts. Live checks require separately configured read-only Azure tools.
metadata:
  owner: cloud-platform
  maturity: draft
---
# App Service Change Review

## Purpose
Help review an Azure App Service change before release and identify risks, missing information, and next steps for a human reviewer.

## Intake
Identify or ask for the target environment, App Service plan, deployment method, identity model, application settings, network exposure, monitoring setup, and rollback plan.

## Review workflow
1. Summarize the proposed change.
2. Identify whether the target environment is production or non-production.
3. Review the App Service plan and scaling assumptions.
4. Check whether secrets are stored outside application settings where appropriate, such as through Key Vault references.
5. Review managed identity usage and access boundaries.
6. Review network exposure and access restrictions.
7. Review logging, alerts, health checks, deployment slots, and rollback readiness.

## Network exposure decision rules
- If the workload is production and handles sensitive data, ask whether private endpoints or an approved ingress pattern are required before suggesting public access.
- If the workload must be public, check authentication, TLS, WAF or gateway controls, logging, and monitoring.
- If network requirements are unknown, ask for expected callers and data classification.

## Output format
Return a summary, findings with severity, missing information, review questions, and next steps.

## Boundaries
Keep production approval and Azure resource changes with a human reviewer. Ask for human review when the change affects production, identity, secrets, public network exposure, or current pricing and service-limit assumptions.
