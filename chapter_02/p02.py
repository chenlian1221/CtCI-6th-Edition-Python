from linkedlist import LinkedList, LinkedListNode
from collections import defaultdict
import unittest, time

def find_kth_from_end(ll: LinkedList, k: int) -> LinkedList:
    '''
    1. 先去count整個linked list長度 = c
    2. for loop從頭去找到 c-k
    '''

    # node = ll.head
    # c = 0
    # while node:
    #     c += 1
    #     node = node .next  
    # if k != c:  
    #     node = ll.head
    #     for i in range(c-k):
    #         node = node.next
    # else:
    #     return ll.tail
    # return ll.head

    curr = temp = ll.head
    for _ in range(k):
        if not temp:
            return None
        temp = temp.next

    while temp:
        curr = curr.next
        temp = temp.next
    return curr


class test(unittest.TestCase):

    test_cases = [
        # list, k, expected
        ([10, 20, 30, 40, 50], 1, 50),
        ((10, 20, 30, 40, 50), 5, 10),
    ]

    test_fns = [
        find_kth_from_end,
        
    ]

    def test_find_kth_from_end(self):
        runs = 1000
        fn_runtimes = defaultdict(float)
        for _ in range(runs):
            for ll, n, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    f = fn(LinkedList(ll),n)
                    # print(f.value,expected)
                    assert(f.value == expected), f"{fn.__name__} failed for value {ll}, {n}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__ =='__main__':
    unittest.main()