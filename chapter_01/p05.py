"""
可以對字串執行的編輯有三種：插入一個字元，刪除一個字元，替換一個字元。假設有兩個字串，請寫一個函式檢驗它們是否為1個(或0個）編輯距離。
Example
pale, ple → True
pales, pale → True
pale, bale → True
pale, bake → False
"""
from collections import defaultdict
import unittest, time

def one_edit(s1: str, s2: str) -> bool:
    """
    會有三種情況要討論:
    1. s1長度 = s2長度:
        逐一檢查只能有一個字元不同
    2. s1長度 - s2長度 = 1
        s1 = s2 insert 一個字元
    3. s2長度 - s1長度 = 1:
        s2 = s1 insert 一個字元
    其餘狀況均為Fasle (不可能編輯劇離為0 or 1)
    """
    if len(s1) == len(s2):
        return one_edit_equal_length(s1, s2)
    elif len(s1) == len(s2)+1:
        return one_edit_insert(s1, s2)
    elif len(s1)+1 == len(s2):
        return one_edit_insert(s2, s1)
    else: 
        return False

def one_edit_equal_length(s1, s2):
    flag = False
    for i in range(len(s1)):
        if s1[i] != s2[i] and flag:
            return False
        elif s1[i] != s2[i] and not flag:
            flag = True
    return True

def one_edit_insert(s_long, s_short):
    flag, i_long, i_short = False, 0, 0
    while i_long < len(s_long) and i_short < len(s_short):
        if s_long[i_long] != s_short[i_short]:
            if not flag:
                flag = True
                i_long += 1 ########
            else: 
                return False
        else:
            i_long += 1
            i_short += 1

    return True    

"""
1000 runs
one_edit_different: 40.1 ms
"""
class test(unittest.TestCase):

    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),

    ]

    test_fns = [
        one_edit,
        
    ]

    def test_one_edit_different(self):
        runs = 1000
        fn_runtimes = defaultdict(float)

        for _ in range(runs):
            for s1, s2, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(s1, s2) == expected
                    ), f"{fn.__name__} failed for values: {s1, s2}"
                    fn_runtimes[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000


        print(f"\n{runs} runs")
        for fn_name, runtime in fn_runtimes.items():
            print(f"{fn_name}: {runtime:.1f} ms")

if __name__ == '__main__':
    unittest.main()         