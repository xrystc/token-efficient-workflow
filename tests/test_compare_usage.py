import copy
import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / 'scripts' / 'compare_usage.py'
spec = importlib.util.spec_from_file_location('compare_usage', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def record():
    return dict(task='task', scope='scope', model='model', settings='same',
                quality_criteria='criteria', accounting_basis='input + output',
                coverage_complete=True, non_overlapping=True, accounting_verified=True,
                task_complete=True, quality_passed=True, input_tokens=80,
                cached_input_tokens=50, output_tokens=20, reasoning_tokens=5, total_tokens=100)


class CompareTests(unittest.TestCase):
    def test_comparable(self):
        a = record(); b = copy.deepcopy(a)
        b.update(input_tokens=60, total_tokens=80)
        result = module.compare(a, b)
        self.assertTrue(result['comparable'])
        self.assertEqual(result['total_change_percent'], -20)

    def test_incomplete_and_mismatched_no_percentage(self):
        a = record(); b = record(); b.update(scope='different', quality_passed=False)
        result = module.compare(a, b)
        self.assertFalse(result['comparable'])
        self.assertNotIn('total_change_percent', result)
        self.assertIn('scope differs', result['limitations'])

    def test_cache_not_added_to_total(self):
        a = record(); b = record(); b['total_tokens'] = 150
        self.assertFalse(module.compare(a, b)['comparable'])

    def test_missing_and_zero_total(self):
        a = record(); b = record(); b['total_tokens'] = None
        self.assertFalse(module.compare(a, b)['comparable'])
        a.update(input_tokens=0, cached_input_tokens=0, output_tokens=0, reasoning_tokens=0, total_tokens=0)
        self.assertFalse(module.compare(a, record())['comparable'])

    def test_invalid_counter(self):
        a = record(); a['cached_input_tokens'] = 81
        with self.assertRaises(ValueError): module.compare(a, record())
        a = record(); a['input_tokens'] = True
        with self.assertRaises(ValueError): module.compare(a, record())


if __name__ == '__main__':
    unittest.main()
