"""
給定一個由NxN矩陣表示的圖像，
其中圖像中的每隔像素為4個位元組，
請撰寫一個方法將圖像旋轉90度，
您能在同一塊記憶體中就地(in place)完成嗎？
"""

from collections import defaultdict
import unittest, time

def rotate_matrix(matrix):
    return



class test(unittest.TestCase):

    test_cases = [

    ]

    test_fns = [

    ]

    def test_rotate_matrix(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for matr, expected in self.test_cases:
                for fn in self.test_fns:

                    start = time.perf_counter()
                    assert(
                        fn(matr) == expected
                    ), f"{fn.__name__} failed for values {matr}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()