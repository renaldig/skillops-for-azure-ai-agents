---
name: azure-observability-investigation
description: Guide an assistant through Azure Monitor,
  Application Insights, and Log Analytics investigations for
  Azure application incidents.
---
Use this skill when the user reports an Azure application issue,
asks why an Azure workload is unhealthy, or needs help preparing
an investigation from Azure Monitor, Application Insights, or
Log Analytics data.
Start by collecting these facts:
1. Affected application, resource, or resource group.
2. Environment: dev, test, staging, production, or unknown.
3. Time window, including timezone.
4. Observed symptom: errors, latency, availability, dependency
   failure, CPU, memory, queue backlog, or another signal.
5. User or business impact.
6. Recent changes: deployments, configuration updates, scaling
   changes, networking changes, or dependency changes.
Investigation order:
1. Confirm the symptom and time window.
2. Check request volume, failures, and latency.
3. Check exceptions and dependency failures.
4. Check resource metrics and platform health signals.
5. Check recent control-plane changes if the issue started
   suddenly.
6. Separate evidence from hypotheses.
Return the result as:
- Summary of the symptom
- Data sources checked
- Key observations
- Most likely hypotheses
- Causes ruled out
- Recommended next actions
- Escalation recommendation
Only claim telemetry was queried when the user has provided
query results or the assistant has approved tool access.
When data is missing, name the missing data and explain why.
