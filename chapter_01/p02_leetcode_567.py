"""
leetcode 567

Given two strings `s1` and `s2`, 
return `true` if `s2` contains a permutation of `s1`, 
or `false` otherwise.

In other words, 
return `true` if one of `s1`'s permutations is the substring of `s2`.
"""

from collections import defaultdict
import time, unittest

def check_inclusion(s1, s2) -> bool:

    return

class test(unittest.TestCase):
    
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
    ]

    test_fns = [
        check_inclusion,

    ]

    def test_check_inclusion(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for s1,s2,expected in self.test_cases:
                for fn in self.test_fns:

                    start = time.perf_counter()
                    assert(
                        fn(s1,s2) == expected
                    ), f"{fn.__name__} failed for values {s1, s2}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime} ms")

if __name__ == '__main__':
    unittest.main()