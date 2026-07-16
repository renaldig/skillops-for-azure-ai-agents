# Skill Approval Workflow

This workflow describes how internal Azure Agent Skills move from idea to shared use. A shared skill must have a named owner, defined scope, reviewer, test scenarios, publication status, review date, and record of any Foundry skill, toolbox, agent, and deployment versions.

## Roles
- **Author**: writes or updates the skill.
- **Technical owner**: checks Azure engineering accuracy.
- **Risk reviewer**: reviews security, data, reliability, or operations risk.
- **Approver**: confirms that the skill is ready for the intended status.

## Approval steps
1. Propose the skill by creating a skill brief.
2. Draft `SKILL.md` and supporting examples.
3. Run at least two golden tasks.
4. Request owner and risk review.
5. Publish only after approval and status assignment.
6. For hosted deployments, create new Foundry skill, toolbox, and agent versions rather than overwriting the active release.
7. Link the deployment to the evaluation record and rollback target.

## Testing rule
A skill moves to Approved status only when reviewers can see at least two test scenarios and an evaluation record showing how the skill changed assistant behaviour.
