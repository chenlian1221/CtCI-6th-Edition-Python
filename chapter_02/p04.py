"""
請撰寫程式碼，將一個鏈結串按x值進行分區，
使所有小於x的節點只排在所有大於x的節點之前。
如果x也包含在鏈結串中，則x的值指要放在小於x的的元素之後
（參考下方範例）就可以了。
分區元素x可以出現在『右分區』中的任何位置，它不需要出現在左右分區之間。

Example
input: 3 → 5 → 8 → 5 → 10 → 2 → 1 , x=5
output: 3 → 1 → 2 → 10 → 5 → 5 → 8
"""
from linkedlist import LinkedList, LinkedListNode
from collections import defaultdict
import unittest, time

def partition(ll: LinkedList, x: LinkedListNode):
    return


