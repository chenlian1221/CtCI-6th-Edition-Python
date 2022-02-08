"""
撰寫程式碼來從未排序的鏈結串列中刪除重複項。
延伸：如果不允許使用暫存記憶體，如何解決這個問題？
"""

from linked_list import LinkedList, LinkedListNode
from collections import defaultdict
import unittest, time


def remove_dep(ll: LinkedList) -> LinkedList:
    prev, curr = None, ll.head
    seen = set()
    while curr:
        if curr.value in seen:
            prev = curr.next
        else:
            seen.add(curr.value)
            prev = curr
        curr = curr.next
    ll.tail = prev
    return ll

class test(unittest.TestCase):

    test_cases = [
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    test_fns = [
        remove_dep,

    ]
    def test_remove_dep(self):

        runs = 1000
        fn_runtimes = defaultdict(float)
        
        for _ in range(runs):
            for ll, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    expected = expected.copy()
                    dep = fn(LinkedList(ll))
                    print(dep.values(), expected)
                    assert(
                        dep.values() == expected
                    ), f"{fn.__name__} failed for value {ll}"
                    dep.add(5)
                    expected.append(5)
                    assert dep.values() == expected
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
        print(f"\n{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()