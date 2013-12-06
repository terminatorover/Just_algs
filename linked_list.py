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
#        if self.head != None:
#            print "the head is a moving target: " + str(self.head.data)
        fresh_add = Node(data)
        
        if self.head == None:

            self.head = fresh_add
            print "added node with data:--- " + str(data)

        else:
            print "OK"
            ##if it's only a node then we add fresh_add to the end
            if self.head.next == None:
                self.head.next = fresh_add
                print "added node with data:---------- " + str(data)
            else:#now we have more than a node ,lets go
                prev = self.head
                tmp = self.head.next
                print "this should be 6: " + str(data)
                print "this shoul NOT be None: " + str(tmp)
                while (tmp):
                    if ( tmp.data < data):#if the data in tmp node is smaller that that of the 
                        #Node that we currently have then advance both pointers
                        
                        tmp = tmp.next
                        prev = prev.next 
                        if (tmp == None):
                            #while advancing pointers if you find that tmp is past the end node
                            #then use prev to make sure that the last node points to the new node
                            prev.next = fresh_add
                            

                    else:
                        print "four should be here: " + str(data)
                        if ( self.head.data > data):#checks if the node to be added has data
                            #smaller that the head node of the linked list if so it makes 
                            #the new fresh node the head of the list. This piece of oode
                            #code have come first in the function, but i'm too lazy to move it lol
                            print "ONCE"
                            print "------------------------------------"
                            print self.head.data, fresh_add.data

                            fresh_add.next = self.head
                            self.head = fresh_add


                            print "------------------------------------"
                            break 

                        else: #this the the in between part
                            print "ONCE"
                            fresh_add.next = tmp
                            prev.next = fresh_add

                            print "added node with data:------------------------ " + str(data)
                            break 
                        
                

                    
            

            

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



mylist = LinkedList()

for i in range(30):
    
mylist.sorted_add(3)
mylist.sorted_add(6)
mylist.sorted_add(4)
mylist.sorted_add(-1)

print "this is what i see"  


mylist.see()



        
    
    
        
