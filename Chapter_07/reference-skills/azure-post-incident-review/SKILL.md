---
name: azure-post-incident-review
metadata:
  owner: platform-sre
  domain: reliability
  maturity: draft
description: Help an assistant prepare blameless post-incident
  reviews and convert findings into Azure reliability actions.
---
Use this skill after an Azure incident has been mitigated or
resolved and the team needs to prepare a post-incident review.
Gather these inputs:
1. Incident summary and severity.
2. Start time, detection time, mitigation time, and resolution time.
3. Affected resources, services, environments, and users.
4. Alerts, dashboards, KQL results, and other telemetry evidence.
5. Recent deployments or configuration changes.
6. Mitigation steps and communication history.
7. Known gaps in monitoring, ownership, deployment, or response.
Create the review with these sections:
- Summary
- Customer or user impact
- Timeline
- What happened technically
- What went well
- What made detection or response harder
- Contributing factors
- Action items with owners and due dates
- Skill library updates needed
Rules:
- Keep the review blameless.
- Focus on systems, signals, processes, and decisions.
- Use only facts supported by the available evidence.
- Convert lessons into specific improvements.
