#/usr/bin/python 


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,my_data):
        self.data = my_data



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self,data):
        
        new = Node(data)
        if self.head == None:
            self.head = new 
            self.tail = new
        else:
            tmp = self.head
            new.next = self.head
            self.head = new

    def sorted_add(self,data):
        fresh_add = Node(data)
        
        if self.head == None:
            self.head = fresh_add
        else:
            if self.head.data > fresh_add.data:
                fresh_add.next = self.head
                self.head = fresh_add.next
            else:
                tmp = self.head

                

    def append(self,data):
        new = Node(data)
        if self.tail == None :
            self.tail = new
            self.head = new 
        else:
            final = self.tail
            final.next = new 
            self.tail = new 
            
            
    def see(self):
        tmp = self.head 
        while (tmp):
            print tmp.data
            tmp = tmp.next 

new = Node(2)

mylist = LinkedList()

mylist.add(3)
mylist.add(4)
mylist.add(6)
mylist.append(1000)
mylist.see()

        
    
    
        
