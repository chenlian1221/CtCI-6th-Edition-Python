"""
給定一個由NxN矩陣表示的圖像，
其中圖像中的每隔像素為4個位元組，
請撰寫一個方法將圖像旋轉90度，
您能在同一塊記憶體中就地(in place)完成嗎？
"""

from collections import defaultdict
import unittest, time

def rotate_matrix_basic(matrix):
    n = len(matrix)
    if n <= 1:
        return matrix
    
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i] = matrix[i][::-1]
    return matrix

class test(unittest.TestCase):

    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    test_fns = [
        rotate_matrix_basic,

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