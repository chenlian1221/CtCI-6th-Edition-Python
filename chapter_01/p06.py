"""
藉由計算重複字元來實作一個執行基本的字串壓縮方法。
例如：字串aabcccccaaa將變成a2b1c5a3。
如果『壓縮』字串不會變得比原來自傳更小，
那個您的方法應該回傳原來的字串。
可以假設字串只有大寫和小寫字母(a-z)。
"""

from collections import defaultdict
import unittest, time


def compress_string(s:str) -> str:
    if len(s) <= 2:
        return s
    result, times = s[0], 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            times += 1
        else: 
            result = (result + str(times) + s[i]) if times > 1 else (result + s[i])
            times = 1
    result = result+str(times) if times > 1 else result
    return s if len(result)>=len(s) else result


class test(unittest.TestCase):
    
    test_cases = [
        ("aabcccccaaa", "a2bc5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    test_fns = [
        compress_string,

    ]

    def test_compress_string(self):

        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for s, expected in self.test_cases:
                for fn in self.test_fns:

                    start = time.perf_counter()
                    assert(
                        fn(s) == expected
                    ), f"{fn.__name__}: {fn(s)} failed for values {s}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__=='__main__':
    unittest.main()