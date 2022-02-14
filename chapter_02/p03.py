"""
刪除中間節點：
請實作一個演算法，刪除單向鏈結串列中間部分的某個節點
（及除第一個和最後一個節點外的任何節點，不一定是正中間節點），而且只能存取中間節點。
Example:
input: 鍊結串 a → b → c → d → e → f 中的節點c
output: 不回傳任何結果，但是新的鏈結串要看起來像  a → b → d → e → f 
"""

from linkedlist import LinkedList, LinkedListNode
from collections import defaultdict
import unittest, time
def partition(ll: LinkedList):
    return


class test(unittest.TestCase):
    test_cases = [

    ]

    test_fns = [

    ]

    def test_partition(self):
        runs = 1000

        for _ in range(runs):
            for test, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    