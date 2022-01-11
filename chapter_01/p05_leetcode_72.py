"""
leetcode 72
Given two strings `word1` and `word2`, 
return the minimum number of operations required 
to convert `word1` to `word2` .
 
You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
"""

import unittest, time
from collections import defaultdict

def min_distance(word1: str, word2: str) -> int:
    # len(word1) * len(word2) 的 dict
    l1, l2 = len(word1), len(word2)
    dic = [list(range(l2+1))]+[[r+1]+[0]*l2 for r in range(l1)]

    for i in range(l1):
        for j in range(l2):
            dic[i+1][j+1] = dic[i][j] if word1[i]==word2[j] else min(dic[i][j],dic[i][j+1],dic[i+1][j]) + 1

    return dic[l1][l2]


class test(unittest.TestCase):

    test_cases = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
    ]

    test_fns = [
        min_distance,

    ]

    def test_min_distance(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for w1, w2, expected in self.test_cases:
                for fn in self.test_fns:
                    
                    start = time.perf_counter()
                    assert(
                        fn(w1,w2) == expected
                    ), f"{fn.__name__} failed for {w1,w2}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()