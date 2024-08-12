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
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre_temp=self.head
        while temp.next is not None:
            pre_temp=temp
            temp=temp.next
        self.tail=pre_temp
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head.next
        self.head.next=None
        self.head=temp
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value
    def get(self,pos):
        if pos<0 or pos>=self.length:
            return None
        temp=self.head
        for _ in range(pos):
            temp=temp.next
        return temp

    def set(self,pos,value):
        temp=self.get(pos)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,pos,value):
        if pos<0 or pos>self.length:
            return False
        if pos==0:
            return self.pre_append(value)
        if pos==self.length:
            return self.append(value)
        temp=self.get(pos-1)
        new_node=Node(value)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True


    def remove(self,index):
        if index < 0 or index >=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reversed(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

ll=LinkedList(1)
ll.pre_append(2)
ll.append(3)
ll.append(4)
ll.set(2,100)
ll.set(1,400)
ll.insert(2,5)
ll.remove(2)
ll.reversed()
ll.print_list()