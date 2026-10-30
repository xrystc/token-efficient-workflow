#!/usr/bin/env python3
"""Compare two explicitly supplied, pre-aggregated usage records."""
import argparse
import json
import sys
from pathlib import Path

FIELDS = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_tokens', 'total_tokens')
MATCH = ('task', 'scope', 'model', 'settings', 'quality_criteria', 'accounting_basis')
FLAGS = ('coverage_complete', 'non_overlapping', 'accounting_verified', 'task_complete', 'quality_passed')


def compare(base, candidate):
    problems = []
    for label, record in (('baseline', base), ('candidate', candidate)):
        if not isinstance(record, dict):
            raise ValueError(f'{label}: expected a JSON object')
        for key in MATCH:
            if not isinstance(record.get(key), str) or not record[key].strip():
                problems.append(f'{label}: missing {key}')
        for key in FLAGS:
            if record.get(key) is not True:
                problems.append(f'{label}: {key} is not true')
        for key in FIELDS:
            value = record.get(key)
            if value is not None and (type(value) is not int or value < 0):
                raise ValueError(f'{label}: {key} must be a nonnegative integer or null')
        for part, whole in (('cached_input_tokens', 'input_tokens'), ('reasoning_tokens', 'output_tokens')):
            if record.get(part) is not None and record.get(whole) is not None and record[part] > record[whole]:
                raise ValueError(f'{label}: {part} exceeds {whole}')
        if record.get('total_tokens') is None:
            problems.append(f'{label}: total_tokens missing')
        if all(record.get(k) is not None for k in ('input_tokens', 'output_tokens', 'total_tokens')):
            if record['input_tokens'] + record['output_tokens'] != record['total_tokens']:
                problems.append(f'{label}: total is not input + output; review accounting basis')
    for key in MATCH:
        if base.get(key) != candidate.get(key):
            problems.append(f'{key} differs')
    if base.get('total_tokens') == 0:
        problems.append('baseline total is zero')
    result = {'comparable': not problems, 'limitations': problems,
              'baseline': {k: base.get(k) for k in FIELDS},
              'candidate': {k: candidate.get(k) for k in FIELDS},
              'note': 'Operator assertions are not independently verified; aggregate differences do not establish causation or cost savings.'}
    if not problems:
        result['total_change_percent'] = round((candidate['total_tokens'] - base['total_tokens']) / base['total_tokens'] * 100, 2)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('baseline', type=Path)
    parser.add_argument('candidate', type=Path)
    args = parser.parse_args()
    try:
        with args.baseline.open(encoding='utf-8-sig') as f:
            baseline = json.load(f)
        with args.candidate.open(encoding='utf-8-sig') as f:
            candidate = json.load(f)
        result = compare(baseline, candidate)
    except (OSError, ValueError) as e:
        print(f'Error: {e}', file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['comparable'] else 1


if __name__ == '__main__':
    sys.exit(main())
