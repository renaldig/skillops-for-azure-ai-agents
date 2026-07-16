---
name: azure-kql-diagnostics
metadata:
  owner: platform-sre
  domain: azure-monitor
  maturity: draft
description: Help an assistant choose and adapt KQL queries for
  Application Insights and Log Analytics investigations.
---
Use this skill when the user needs to investigate an Azure
application using Application Insights or Log Analytics queries.
Before writing KQL:
1. Ask for the resource, workspace, or Application Insights
   component being investigated.
2. Ask for the time window and timezone.
3. Ask which symptom is being investigated.
4. Confirm which tables are available. Common workspace-based
   tables include AppRequests, AppDependencies, AppExceptions,
   and AppTraces.
Query sequence:
1. Start with request volume, failure rate, and latency.
2. Inspect failed or slow dependencies.
3. Inspect exceptions and traces.
4. Correlate findings by time, operation name, dependency target,
   result code, or operation identifier.
5. Summarize what the query result proves, what remains
   unproven, and what to check next.
Treat root cause as unresolved until a strong query result or
multiple supporting signals back the conclusion. If the query
result is missing, ask for it instead of filling the gap.
