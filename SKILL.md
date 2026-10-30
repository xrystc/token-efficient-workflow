---
name: token-efficient-workflow
description: Reduce avoidable context and repeated work in research, data analysis and coding. Use when a user requests token-efficient execution, context optimization, or an efficiency review. Preserve required evidence, task completeness and validation; measure savings only from comparable actual usage records.
---

# Token-efficient workflow

Deliver the requested result, preserving accuracy, authorization, required verification and provenance. Minimize unnecessary context and repeated work, not necessary scientific review. Do not promise a savings percentage.

## Choose a mode

- **Execute efficiently:** Apply the decisions below to the actual task; use other required domain skills normally. Do not create extra files or reports by default.
- **Review a workflow:** Examine task-relevant artifacts and actual usage if authorized; distinguish observations, plausible causes and recommendations. Read [workflow review](references/workflow-review.md).
- **Measure an improvement:** Read [measurement](references/measurement.md). For already normalized, non-overlapping run records, use `scripts/compare_usage.py`; it does not discover logs or verify the truth of metadata.

## Execution decisions

1. **Orient:** Identify the goal, constraints, authoritative inputs, deliverable, and latest relevant state. Use a concise verified index or recent handoff when available. Resolve conflicts against primary evidence; retain instructions and unresolved uncertainties.
2. **Retrieve progressively:** Locate by scope, path and identifier. Start with schema, headings, targeted passages or relevant rows; expand to full material whenever necessary. Exclude irrelevant dependencies, caches and previews from searches; never delete them as a shortcut. Limit tool output without hiding errors or decisive evidence.
3. **Compute locally:** Use deterministic tools for bulk joins, counts, deduplication and validation. Return relevant summaries and exceptions with source pointers; examine representative cases and consequential anomalies. Avoid dumping entire datasets into conversation.
4. **Reuse carefully:** Before repeating a search, extraction or model, verify source, scope, inputs, version, parameters and freshness. Reuse compatible artifacts; repeat if requested or needed for accuracy. Treat independent studies, observations and effects as different units.
5. **Control context:** At natural milestones, retain a compact checkpoint of objective, constraints, source paths and versions, decisions, unresolved issues and next action. Create or update files only within authorized scope. Preserve history and provenance. Context compaction can reduce input volume while affecting cache reuse; do not assume net savings.
6. **Parallelize deliberately:** Delegate only when authorized and when work can be separated. Assign distinct scopes, minimal necessary context, source IDs and concise output; reconcile overlapping results. Parallel work can cost more tokens.
7. **Verify and deliver:** Perform checks proportionate to the task. Identify limitations, uncertainties and actual outputs. Do not claim token or cost savings without comparable measured runs.
