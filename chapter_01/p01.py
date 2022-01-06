'''
實作一個演算法來判斷一個字串中的字元是否不重複。如果不能使用其他的資料結構怎麼辦？
'''
from collections import defaultdict
import time
import unittest

def is_unique_sorted(s: str) -> bool:
    s = sorted(s)
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            return False
        
    return True

def is_unique_set(s: str) -> bool:
    return len(set(s)) == len(s)

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]

    test_fns = [
        is_unique_sorted,
        is_unique_set
    ]

    def test_is_unique(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for text, expected in self.test_cases:
            for fn in self.test_fns:
                start = time.perf_counter()
                assert(
                    fn(text) == expected
                ), f"{fn.__name__} failed for value: {text}"
                fn_runtimes[fn.__name__] += (
                    time.perf_counter() - start
                ) * 1000
        print(f"\n{runs} runs")
        for fn_name, runtime in fn_runtimes.items():
            print(f"{fn_name}: {runtime:.1f}ms")

if __name__=='__main__':
    unittest.main()