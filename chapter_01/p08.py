"""
請撰寫一個這樣的演算法，如果MxN矩陣中的一個元素為0，
那麼將該字元素所在的整個列和欄都設定為0。
"""

from collections import defaultdict
from copy import deepcopy
from typing import List
import unittest, time

def rotate_matrix(matrix: List)->List:
    record_i, record_j = set(), set()
    row, col = len(matrix), len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                record_i.add(i)
                record_j.add(j)
    for i in range(row):
        for j in range(col):     
            if (i in record_i) or (j in record_j):
                matrix[i][j] = 0

    return matrix

class test(unittest.TestCase ):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    test_fns = [
        rotate_matrix,
    ]

    def test_rotate_matrix(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for mat, expected in self.test_cases:
                for fn in self.test_fns:

                    start = time.perf_counter()
                    mat = deepcopy(mat)
                    assert(
                        fn(mat) == expected
                    ), f"{fn.__name__} failed for {mat}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__=='__main__':
    unittest.main()