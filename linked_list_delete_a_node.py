import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
            node = SinglyLinkedListNode(node_data)

            if not self.head:
                self.head = node
            else:
                self.tail.next = node


            self.tail = node
def deleteNode(head,position):
        itr=head
        index=position
        count=0
        while itr:
            if count==index:
                print(count,index)
                itr.next=itr.next.next
                print(itr.next.data,itr.next.next.data)
                break;
            itr=itr.next
            
            count=count+1

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)
