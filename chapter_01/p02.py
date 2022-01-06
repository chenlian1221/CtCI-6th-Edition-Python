'''
實作一個演算法來判斷一個字串中的字元是否不重複。如果不能使用其他的資料結構怎麼辦？
'''
from collections import Counter, defaultdict
import unittest, time

def check_permutation_sorted(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_counter(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

class test(unittest.TestCase):
    test_cases = [
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    ]
    test_fns = [
        check_permutation_sorted,
        check_permutation_counter,
    ]

    def test_check_permutation(self):
        runs = 1000
        fn_rumtimes = defaultdict(float)

        for _ in range(runs):
            for s1, s2, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(s1,s2) == expected
                    ), f"{fn.__name__} failed for value: {s1,s2}"
                    fn_rumtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
        print(f"\n{runs} runs")
        for fn_name, runtime in fn_rumtimes.items():
            print(f"{fn_name}: {runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()

