# Token-Efficient Workflow

A Codex skill for reducing unnecessary context and repeated work in research, data analysis, and software projects while preserving evidence, completeness, and verification.

## Use

Place this folder in your Codex skills directory and restart or refresh skill discovery if necessary. Invoke it explicitly:

> Use `$token-efficient-workflow` to complete this task efficiently while preserving the required evidence and checks.

The skill supports efficient execution, workflow review, and measured comparison. It does not impose a token budget, access your usage history, or guarantee savings. It does not override the user’s instructions or other required skills.

## Optional comparison utility

Requires Python 3.9 or later and only the standard library. The two JSON inputs must be **independently prepared, pre-aggregated, non-overlapping run records** with verified accounting and comparable tasks. The utility reads only the two paths supplied and prints results; it does not inspect logs or verify the supplied assertions.

```sh
python scripts/compare_usage.py examples/baseline.json examples/candidate.json
python -m unittest discover -s tests
```

The example data are fictional. The output is a percentage change in recorded total tokens, not a claim of causation or cost savings. For valid comparisons, review [measurement guidance](references/measurement.md); preserve unknown fields as null and never sum cached or reasoning tokens on top of their parent totals. Return codes: 0 comparable, 1 insufficiently comparable, 2 invalid input.

## Structure

- `SKILL.md`: concise instructions loaded on invocation.
- `references/`: on-demand workflow review and measurement guidance.
- `scripts/compare_usage.py`: optional normalized-record comparison.
- `tests/` and `examples/`: tests and synthetic demonstration.

## Privacy and limitations

The skill does not automatically scan history or upload data. Confirm authorization and remove private paths, transcripts, credentials and project data before sharing any real records. A single before/after comparison is exploratory; cache, model, tool and task differences may confound results. The script cannot verify source coverage, parent-child accounting, task equivalence or quality.

---

本技能用于减少重复读取和上下文负担，优先保证任务完整、证据可追溯和必要的质量检查。使用时可直接输入 `$token-efficient-workflow`。示例数据均为虚构数据；比较工具不会自动读取历史记录，也不能保证节省比例。上传真实用量记录前，请检查隐私信息。
