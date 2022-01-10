"""
leetcode 217
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""


from collections import defaultdict
from typing import List
import unittest, time

def contains_duplicate_set(s: List) -> bool:

    return len(s) != len(set(s))

def contains_duplicate_sort(s: List) -> bool:
    s = sorted(s)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False

def contains_duplicate_dict(s: List) -> bool:
    d = defaultdict(int)
    for ch in s:
        if ch in d:
            return True
        d[ch] += 1
    return False

"""
1000 runs
contains_duplicate_set: 2.4947999999988535 ms
contains_duplicate_sort: 3.759200000000018 ms
contains_duplicate_dict: 4.211199999999986 ms
"""
class test(unittest.TestCase):
    test_cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
    ]

    test_fns = [
        contains_duplicate_set,
        contains_duplicate_sort,
        contains_duplicate_dict
    ]

    def test_containsDuplicate(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for arr, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(arr) == expected
                    ), f"{fn.__name__} failed for values: {arr}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{runs} runs")

        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime} ms")

if __name__ == '__main__':
    unittest.main()