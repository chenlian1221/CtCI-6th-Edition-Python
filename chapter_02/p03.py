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
def delete_middle_node(node: LinkedListNode):
    node.value = node.next.value
    node.next = node.next.next
    


class test(unittest.TestCase):
    test_cases = [
        ([1, 2, 3,4, 5, 7, 8, 9], 5, [1, 2, 3, 4, 7, 8, 9]),
    ]

    test_fns = [
        delete_middle_node
    ]

    def test_delete_middle_node(self):
        runs = 1000
        fn_runtimes = 0.0

        for _ in range(runs):
            for test, n, expected in self.test_cases:
                start = time.perf_counter()
                ll = LinkedList(test)
                node = LinkedListNode(n)
                assert(delete_middle_node(node) == LinkedList(expected)), f"failed by {node}"
                fn_runtimes += (time.perf_counter() - start) * 1000
        print(f"{runs} runs")
        print(f"runtimes: {fn_runtimes:.1f} ms")

if __name__=='__main__':
    unittest.main()