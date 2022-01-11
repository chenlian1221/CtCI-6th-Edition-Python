"""
leetcode 567

Given two strings `s1` and `s2`, 
return `true` if `s2` contains a permutation of `s1`, 
or `false` otherwise.

In other words, 
return `true` if one of `s1`'s permutations is the substring of `s2`.
"""

from collections import defaultdict, Counter
import time, unittest

def check_inclusion(s1, s2) -> bool:
    # len(s1) <= len(s2)
    cnt1 = Counter(s1)
    cnt2 = Counter(s2[:len(s1)-1])

    for i in range(len(s1)-1,len(s2)):
        curr, start = i, i-len(s1)+1

        cnt2[s2[curr]] += 1

        if cnt1 == cnt2:
            return True

        cnt2[s2[start]] -= 1 # window往右移，把地一個位置的cnt丟掉

        if cnt2[s2[start]] == 0:
            del cnt2[s2[start]]
    return False

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