'''
142. Linked List Cycle II
Medium
Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.
There is a cycle in a linked list 
    if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. 
Note that pos is not passed as a parameter.
Do not modify the linked list.
'''


from linked_list import LinkedList, LinkedListNode
from collections import defaultdict
import unittest, time

def detect_cycle(ll: LinkedList):
    fast, slow = ll.head, ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break
    
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
        ((LinkedList([1])), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    test_fns = [
        detect_cycle, 
    ]

    def test_detect_cycle(self):
        runs = 1000
        fn_runtimes = defaultdict(float)
        for _ in range(runs):
            for test, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(test) == expected
                    ),f"{fn.__name__} failed for value {test}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
        print(f"\n{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()