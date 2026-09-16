# Contribution rules

This repository is used for small Git workflow exercises.

## Controlled canary issues

Issues whose title begins with `[CONTROLLED CANARY]` are owner-operated integration tests.

Before doing any implementation work on a controlled canary issue, first comment on the issue with your proposed approach and wait for maintainer approval. Do not start implementation until a maintainer explicitly approves the work. Do not open or submit a pull request before that approval.

After approval:

1. Create a focused branch for the issue.
2. Make the smallest change that satisfies the acceptance criteria.
3. Run `python -m pytest -q`.
4. Open a Draft pull request that references the issue URL and summarizes the verification performed.

Controlled canary issues are reserved for the repository owner's automation tests; external contributors should not claim or work on them.
