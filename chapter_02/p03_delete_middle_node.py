from linked_list import LinkedList


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    print('1---',ll) # 1 -> 2 -> 3 -> 4
    middle_node = ll.add(5)
    print('2---',ll) # 1 -> 2 -> 3 -> 4 -> 5
    ll.add_multiple([7, 8, 9])
    print('3---',ll) # 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
    
    delete_middle_node(middle_node)
    print('4---',ll) # 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
