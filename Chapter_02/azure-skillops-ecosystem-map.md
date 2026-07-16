# Azure SkillOps Ecosystem Map

```text
Canonical skill in Git
        |
        +--> .github/skills/ --> GitHub Copilot Agent mode
        |
        +--> Registered skill version in Microsoft Foundry
                 |
                 +--> Toolbox version / MCP endpoint
                          |
                          +--> Hosted agent version
                                   |
                                   +--> Azure tools and data
                                   +--> Traces and evaluation
                                   +--> Published endpoint
```

## Boundaries

- Skill: reusable guidance and workflow instructions
- Tool: callable read or action capability
- Identity and RBAC: actual access boundary
- Agent: model-driven runtime that loads guidance and uses tools
- Evaluation: evidence that a version behaves acceptably
- Governance: ownership, approval, promotion, and rollback
