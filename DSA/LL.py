class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pre_append(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.length+=1

    def pop(self):
        temp=self.head
        while temp.next is not self.tail:
            temp=temp.next
        temp.next=None
        self.tail=temp
        self.length-=1

    def pop_first(self):
        temp=self.head.next
        self.head.next=None
        self.head=temp
        self.length-=1


ll=LinkedList(1)
ll.pre_append(2)
ll.append(3)
ll.print_list()
print(ll.head.value)
print(ll.tail.value)
