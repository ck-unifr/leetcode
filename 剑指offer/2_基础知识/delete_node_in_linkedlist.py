"""
面试题13 O(1)时间删除链表结点

要求：O(1)时间删除链表结点

思路：如果有后续结点，后续结点的值前移，删除后续结点，如果没有，只能顺序查找了

https://blog.csdn.net/dawn_after_dark/article/details/80741683

题目
给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def delete_node(link: Node, node: Node) -> None:
    # 只有一个结点
    if node == link:
        del node
    # node是尾结点
    if node.next is None:
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:
        node.val = node.next.val
        n_node = node.next
        node.next = n_node.next
        del n_node
    return
