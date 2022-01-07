'''
您得到一個字串，請寫一個函式來檢查他是否是一個回文的變位字。
回文的意思是單詞或短語無論向前讀或向後讀都是一樣的。變位字就是字母重新排列。
回文不局限於字典單字。
Example
input: Tact Coa
output: True (acceptable answer: “taco cat”, “atco cat”)
'''

from collections import defaultdict, Counter
import unittest, time

def is_palindrome_permutation_counter(s: str) -> bool:
    '''
    去count每個字元出現次數 (space可忽略，不分大小寫)
    如果字串長度是偶數: 每個字元出現次數都要是偶數
    如果字串長度是奇數: 只能有一個字元出現次數為奇數
    '''
    s_list = list(s.replace(" ", "").lower())
    cnt = Counter(s_list)
    flag = False
    for _, times in cnt.items():
        if times % 2 == 1 and flag == False:
            flag = True
        elif times % 2 == 1 and flag == True:
            return False
    return True


class test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    test_fns = [
        is_palindrome_permutation_counter,
    ]

    def test_is_palindrome_permutation(self):
        runs = 1000
        fn_runtime = defaultdict(float)

        for _ in range(runs):
            for text, expected in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    assert(
                        fn(text) == expected
                    ), f"{fn.__name__} failed for value: {text}"
                    fn_runtime[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000


        print(f"\n{runs} runs")
        for fn_name, runtime in fn_runtime.items():
            print(f"{fn_name}: {runtime} ms")
        

if __name__ == '__main__':
    unittest.main()