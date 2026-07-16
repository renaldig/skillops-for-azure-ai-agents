# Foundry Search Integration Record

## Azure resources
- Storage account:
- Blob container: policy-docs
- Search service:
- Search endpoint:
- Generated index:
- Embedding model deployment: text-embedding-3-small

## Foundry project
- Project: skillops-foundry-sandbox
- Project connection: skillops-policy-search
- Connection resource ID:
- Project managed identity:

## Versioned assets
- Repository commit:
- Skill: azure-ai-search-retrieval-design
- Skill version:
- Toolbox: policy-retrieval-toolbox
- Toolbox version:
- Hosted agent version:
- Chat model deployment: gpt-4.1

## Role assignments
| Identity | Role | Scope |
|---|---|---|
| Azure AI Search managed identity | Storage Blob Data Reader | Storage account |
| Azure AI Search managed identity | Foundry Project Manager or current equivalent | Foundry parent resource |
| Foundry project managed identity | Search Index Data Contributor | Search service |
| Foundry project managed identity | Search Service Contributor | Search service |

## Test outcomes
- Answerable parental-leave query:
- Missing bicycle-benefit evidence:
- Individual approval-history boundary:
- Citation verified:
- Trace verified:

## Cleanup decision
