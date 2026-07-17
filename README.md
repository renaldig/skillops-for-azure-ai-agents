# SkillOps for Azure AI Agents — Supplementary Files

This package is aligned to the Chapters 1–10 supplied with the manuscript. It contains the starter assets, sample inputs, templates, reference outputs, Azure configuration files, and hosted-agent source files needed for the exercises used in the book.

## How to use the package

1. Open the folder for the chapter you are completing.
2. Read that chapter's `README.md` before copying files.
3. Treat folders named `starter` or files ending in `-template` as inputs to complete.
4. Treat folders named `reference` and `Final_Completed_Repository` as comparison material. Do not copy the final repository over your work unless you intentionally want a completed example.
5. Replace every value inside angle brackets, such as `<subscription-id>`, before running commands.
6. Use sandbox or non-production Azure resources. Review commands before running them and remove paid resources when finished.

## Exercise coverage

- Chapter 1: SkillOps inventory
- Chapter 3: Skill activation and read-only Azure MCP context
- Chapter 4: Comprehensive skill design review
- Chapter 5: Internal skill repository and App Service review skill
- Chapter 6: Deployment validation, Bicep checks, Foundry hosted agent, and release readiness
- Chapter 7: KQL diagnostics and read-only Azure Monitor investigation
- Chapter 8: Azure AI Search retrieval design and a Foundry hosted retrieval agent
- Chapter 9: Golden tasks, local/hosted comparison, and Foundry evaluation
- Chapter 10: Approval workflow, MCP access boundaries, release promotion, and rollback

Chapter 2 has no exercise. Its folder contains concise reference diagrams and worksheets only.

## Chapter 8 hosted-agent source

Chapter 8 includes a complete source reference with `main.py`, `requirements.txt`, `.env.example`, `.dockerignore`, `.azdignore`, `toolbox.yaml`, an `azure.yaml` reference, and an optional `Dockerfile`. Current Microsoft Foundry scaffolds can use Python code deployment from `azure.yaml`, so the Dockerfile is not required by every generated project. It is included as a transparent container reference and for environments that use container deployment.

## Security and privacy

All policy, telemetry, incident, employee, and release examples in this package are fictional. Do not add secrets, bearer tokens, connection strings, customer data, employee records, or sensitive log payloads to source control.

## Validation

Run the included validator from the package root:

```powershell
python .\tools\validate_supplementary_files.py
```

The validator checks required files, JSON and JSONL syntax, YAML syntax, Agent Skill front matter, Python syntax, duplicate skill names, and the presence of hidden `.github` and `.vscode` assets.
