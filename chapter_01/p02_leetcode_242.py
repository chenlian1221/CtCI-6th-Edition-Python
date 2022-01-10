"""
leetcode 242
Given two strings s and t, 
return true if t is an anagram of s, 
and false otherwise.
"""
from collections import defaultdict, Counter
import unittest, time


def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


""""
1000 runs
is_anagram_sort: 3.9884000000028896 ms
is_anagram_counter: 14.519799999998558 ms
"""

class test(unittest.TestCase):
    
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("leetcode", "letcode", False),
    ]

    test_fns = [
        is_anagram_sort,
        is_anagram_counter
    ]

    def test_is_anagram(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for s,t,expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(s,t) == expected
                    ), f"{fn.__name__} failed for values {s,t}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime} ms")

if __name__ == '__main__':
    unittest.main()