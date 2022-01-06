'''
寫一個方法用’%20’來替換字串中的所有空格。
您可以假設字串尾端有足夠空間來容納額外字元，並且您擁有字串的『真實』長度的資訊。
Example
input: “Mr John Smith          ” , 13
output: “Mr%20John%20Smith”

'''


from collections import defaultdict
import unittest, time

def urlify(s: str, n: int) -> str:
    return



class Test(unittest.TestCase):
    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    test_fns = [
        urlify,
    ]
    def test_urlify(self):
        runs = 1000
        fn_runtime = defaultdict(float)

        for _ in range(runs):
            for s, n, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(s, n) == expected
                    ), f"{fn.__name__} failed for value: {s, n}"
                    fn_runtime[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
        print(f"\n{runs}")    
        for fn_name, runtime in fn_runtime.items():
            print(f"{fn_runtime}: {runtime:1f} ms")
        


if __name__=='__main__':
    unittest.main()