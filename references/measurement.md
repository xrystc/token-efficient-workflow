# Measuring usage and efficiency

## Accounting

Use observed usage, never estimates derived from files, lines or turns. Identify the source, time interval, coverage and counter semantics. Per-request usage can be summed only when records do not overlap. Cumulative snapshots are not independent requests: use correctly delimited deltas or a verified final snapshot, accounting for resets, resumed sessions and rotated logs. Verify whether parent totals include children; do not add them blindly. Cached input is often a subset of input and reasoning output a subset of output: verify source semantics and avoid adding subsets twice. Unknown values remain unknown, not zero. Never scan unrelated private sessions; use the narrowest authorized scope.

Distinguish token volume from cost, elapsed time and quality. Cache can reduce processing or charges without reducing reported token counts. Pricing and product behavior can vary; verify current official sources when making cost claims.

## Compare two runs

Choose the same defined task and deliverable, comparable input material, coverage, environment and accounting. Record model and settings; disclose differences. Check completion and quality using the same criteria before interpreting efficiency. A single comparison is exploratory, not proof of a general saving; replicated trials with representative tasks are stronger. Record cache state when known. Report input, cached input, output, reasoning output and total separately; no causal attribution from the aggregate alone.

`scripts/compare_usage.py BASELINE.json CANDIDATE.json` consumes **one pre-aggregated record per run**. It does not read Codex logs or prove completeness, exclusivity, equivalence or quality; those are assertions supplied by the operator. Required fields and a synthetic example are in `examples/`. It refuses a percentage if coverage/accounting/completion/quality assertions fail, task/scope/model/settings/quality criteria differ, total is absent or baseline total is zero. Cache state and other unrecorded differences can still confound interpretation. Output contains no pricing.
