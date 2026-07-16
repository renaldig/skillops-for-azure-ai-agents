---
name: azure-model-deployment-evaluation
short_description: Review Azure model deployment and evaluation
  readiness for AI applications.
description: Guide an assistant through model deployment planning,
  evaluation readiness, and release checks for Azure AI workflows.
---
Use this skill when the user asks about deploying a model,
choosing a model deployment pattern, preparing an AI app for
release, or defining evaluation checks in Microsoft Foundry.
Collect these facts first:
1. Task type and user experience.
2. Candidate model or model family, if already selected.
3. Region, quota, throughput, latency, and cost constraints.
4. Input data sensitivity and output safety requirements.
5. Evaluation dataset availability.
6. Quality, safety, and domain-specific success criteria.
7. Monitoring and rollback expectations.
Readiness checks:
1. Confirm that the model fits the task and constraints.
2. Confirm that sensitive data handling is understood.
3. Define evaluation examples before production release.
4. Include both normal and edge-case prompts.
5. Include examples that should be refused or escalated.
6. Recommend monitoring for latency, errors, token usage,
   quality signals, safety signals, and user feedback.
Treat manual prompt testing as an early smoke test,
not as production evaluation.
