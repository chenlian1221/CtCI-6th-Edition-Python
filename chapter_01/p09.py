"""
假設您有一個名為isSubString的方法，
它可以檢查一個單詞是否是另一個單詞的子字串。
假設有兩個字串s1和s2，限定只能使用一次isSubString呼叫，
撰寫程式碼以檢查s2是否是s1的旋轉
（例如: 『waterbottle』 是『erbottlewat』的旋轉）。
"""

from collections import defaultdict
import unittest, time

def string_rotation(s1: str, s2: str):
    if len(s1) != len(s2): 
        return False
    if len(s1) != 0:

        return s1 in s2*2

class test(unittest.TestCase):
    
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    test_fns = [
        string_rotation,
    ]

    def test_string_rotation(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for s1,s2,expected in self.test_cases:
                for fn in self.test_fns:

                    start = time.perf_counter()
                    assert(
                        fn(s1,s2) == expected
                    ), f"{fn.__name__} failed for values {s1,s2}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
        print(f"{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:1f} ms")

if __name__=='__main__':
    unittest.main()





