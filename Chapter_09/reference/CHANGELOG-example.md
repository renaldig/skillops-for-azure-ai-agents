Version 0.4.0 - 2026-05-22
Changed
- Added deployment slot and rollback checks to the App Service
  deployment review workflow.
- Added instruction to separate blockers, recommendations,
  open questions, and suggested next steps.
Why
- Golden task app-service-review-001 showed that the assistant
missed rollback readiness.
  rollback readiness.
Evaluation
- Reran app-service-review-001.
- Reran app-service-positive-001.
- Reran app-service-negative-001.
Result
- Improved readiness coverage.
- No false activation observed in the negative test.
Known limitations
- The skill still needs stronger guidance for networking choices
  when private access requirements are unclear.
