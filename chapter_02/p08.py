'''
迴圈檢測
假設給定一個環圈鏈結串，請實作一個演算法，該演算法會回傳迴圈開始處的節點。
定義：
迴圈鏈結串：是一個鏈結串列，其中節點的下一個指標指向之前某個節點，從而在鏈結串列中形成一個迴圈。
Example:
input: A → B → C → D → E → F → C 前面出現過一樣的C
output: C
'''
import re
from linkedlist import LinkedList
from collections import defaultdict
import unittest, time

def find_cycle(ll: LinkedList):
    slow, fast = ll.head, ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break # return fast
    
    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
        
    return fast

class test(unittest.TestCase):
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    test_cases = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    test_fns = [
        find_cycle,

    ]

    def test_find_cycle(self):
        runs = 1
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for test, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    # expected = expected.copy()
                    # print(fn(test), expected)
                    assert(fn(test) == expected) 
                    f"{fn.__name__} failed for value {test}"
                    fn_runtimes[fn.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__=='__main__':
    unittest.main()