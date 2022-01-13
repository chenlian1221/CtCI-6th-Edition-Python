"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?

"""

from collections import defaultdict
from typing import List
import unittest, time

def compress(arr: List) -> int:
    # if len(arr) <= 2:
    #     return len(arr)
    prev, idx, cnt = arr[0], 0, 0
    for a in arr:
        if a == prev:
            cnt += 1
        else: 
            arr[idx] = prev
            idx += 1
            if cnt > 1:
                cnt = str(cnt)
                for j in range(len(cnt)):
                    arr[idx] = cnt[j]
                    idx+=1
            prev = a
            cnt = 1
    arr[idx] = prev
    idx += 1        
    if cnt > 1:
        cnt = str(cnt)
        for i in range(len(cnt)):
            arr[idx] = cnt[i]
            idx += 1
    print(idx,arr[:idx])
    return idx


class test(unittest.TestCase):

    test_cases = [
        (["a","a","b","b","c","c","c"], 6), # a 2 b 2 c 3 
        (["a"], 1),
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"],4), # a b 12 -> a b 1 2 
    ]

    test_fns = [
        compress, 

    ]

    def test_compress(self):
        runs = 2
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for fn in self.test_fns:
                for arr, expected in self.test_cases:
                
                    start = time.perf_counter()
                    assert(
                        fn(arr) == expected
                    ), f"{fn.__name__} failed for values {arr}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"{runs} runs")
        for fn_name, fn_runtime in fn_runtimes.items():
            print(f"{fn_name}: {fn_runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()