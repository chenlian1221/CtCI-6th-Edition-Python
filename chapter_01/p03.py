'''
寫一個方法用’%20’來替換字串中的所有空格。
您可以假設字串尾端有足夠空間來容納額外字元，並且您擁有字串的『真實』長度的資訊。
Example
input: “Mr John Smith          ” , 13
output: “Mr%20John%20Smith”

'''


from collections import defaultdict
import unittest, time

def urlify_python_lib(s: str, n: int) -> str:
    return s[:n].replace(" ", "%20")

def urlify_reversed(s: str, n: int) -> str:
    # "Mr John Smith       "
    s_list = list(s)  # ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    idx = len(s_list) # 20

    '''
    s先轉為list
    for loop從n-th數回來
    遇到字元 = " " (space): 改成 %20

    '''
    for i in range(n-1, -1, -1):
        if s_list[i] == " ":
            s_list[idx-3:idx] = "%20" 
            idx -= 3
        else:
            s_list[idx-1] = s_list[i]
            idx -= 1

    # print(list("Mr John Smith       "))
    return "".join(s_list[idx:])

def urlify_dic(s: str, n: int) -> str:
    out_list = {}
    for i in range(n):
        # print(i, s[i])
        if s[i] == " ":
            out_list[i] = "%20"
        else:
            out_list[i] = s[i]

    return "".join(out_list.values())


'''
reversed(range(n)) seems to be faster than range(n)[::-1]

$ python -m timeit "reversed(range(1000000000))"
1000000 loops, best of 3: 0.598 usec per loop
$ python -m timeit "range(1000000000)[::-1]"
1000000 loops, best of 3: 0.945 usec per loop


1000
urlify_python_lib: 4.235400 ms
urlify_reversed: 20.788300 ms
urlify_dic: 16.381200 ms

'''

class Test(unittest.TestCase):
    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    test_fns = [
        urlify_python_lib,
        urlify_reversed,
        urlify_dic,
    ]
    def test_urlify(self):
        runs = 1000
        fn_runtime = defaultdict(float)

        for _ in range(runs):
            for s,n in self.test_cases:
                for fn in self.test_fns:
                    start = time.perf_counter()
                    # print('s: ',s,'n: ',n,'expected: ', self.test_cases[(s,n)])
                    assert(
                        fn(s,n) == self.test_cases[(s,n)]
                    ), f"{fn.__name__} failed for value: {s,n}"
                    fn_runtime[fn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
        print(f"\n{runs}")    
        for fn_name, runtime in fn_runtime.items():
            print(f"{fn_name}: {runtime:1f} ms")
        


if __name__=='__main__':
    unittest.main()
    