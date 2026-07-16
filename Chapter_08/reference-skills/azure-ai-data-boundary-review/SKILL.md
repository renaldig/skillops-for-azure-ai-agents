---
name: azure-ai-data-boundary-review
description: Review responsible AI, safety, and data boundary
  considerations for Azure AI, retrieval, and model workflows.
---
Use this skill when the user asks for help reviewing an Azure AI
application, retrieval workflow, model deployment, agent workflow,
or AI data flow for responsible AI and data boundary risks.
Review these boundaries:
1. Source boundary: approved and excluded data sources.
2. User boundary: who may access retrieved or generated content.
3. Prompt boundary: what data may be sent to a model.
4. Output boundary: what content must be refused, redacted,
   blocked, or escalated.
5. Logging boundary: what inputs, outputs, traces, and evaluation
   artifacts may be stored.
Also check:
- Whether content safety controls are required.
- Whether PII, secrets, credentials, or regulated data may appear.
- Whether retrieval results need citations or grounding evidence.
- Whether human review is required for high-impact decisions.
- Whether evaluation includes safety, refusal, and boundary cases.
Avoid suggesting that one service solves responsible AI risk.
Recommend layered controls and human review where appropriate.
