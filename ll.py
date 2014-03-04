#/usr/bin/python 



class Node:
    def __init__(self,node_input,next_node = None):
        self.data = node_input
        self.next = next_node
    def getdata(self):
        return self.data 
    def getnextnode(self):
        return self.next 

    def setnextnode(self,new_node):
        self.next = new_node

class linkedlist:
    def __init__(self):
        self.root = None

    def add(self,input_data):
        if self.root == None:#if we don't even have a single element
            self.root = Node(input_data)

        else:
            tmp = self.root

            if tmp.getnextnode() == None :#there is only one node(namely the root node)
                
                if tmp.getdata() > input_data:
#                    print "PUT IT AFTER  THE ROOT "
                    tmp.setnextnode(Node(input_data))

                else:
#                    print "PUT IT AT THE AHEAD OF THE ROOT"
                    new_root = Node(input_data)
                    new_root.setnextnode(tmp)
                    self.root = new_root
                
            else:
                done = False
                while ( tmp.getnextnode() != None):
                    print tmp.getdata()
                    #now check if our value is between two nodes, if so we insert it in the middle
 #                   print "INPUT DATA: ",input_data,"FIRST NODE: ",tmp.getdata(),"SECOND NODE: ",tmp.getnextnode().getdata()
                        
                    if input_data < tmp.getdata() and input_data > tmp.getnextnode().getdata():
  #                      print "IN BETWEEEN " 
                        lead = tmp.getnextnode()
                        follower = tmp
                        new_node = Node(input_data)
                        new_node.setnextnode(lead)
                        follower.setnextnode(new_node)
                        done = True
                        break 
                    if input_data > tmp.getdata():
                        new_node = Node(input_data)
                        new_node.setnextnode(tmp)
                        self.root = new_node
                        done = True
                        break 

                    tmp = tmp.getnextnode()
                if not done: 
#                        print "PUT IT AT THE END "
                        new_node = Node(input_data)
                        tmp.setnextnode(new_node)

                        
                        
    def iter(self):
        itr = self.root 
        out = ""
        while ( itr!= None):
            out += str(itr.getdata()) + "=="
            itr = itr.getnextnode()
            
        return out




            
        

class TQueue(linkedlist):

    def add(self,input_data):
        self.del_with_id(input_data[0])#If we find a node that has the same id we delete and then we enter the new data struct that has the same id(aka the vertex id ) but has a different cost(lower probably)
        if self.root == None:#if we don't even have a single element
            self.root = Node(input_data)

        else:
            tmp = self.root
            
            if tmp.getnextnode() == None :#there is only one node(namely the root node)

                
                if tmp.getdata()[2] > input_data[2]:
 #                   print "PUT IT AFTER  THE ROOT "
                    tmp.setnextnode(Node(input_data))

                else:
  #                  print "PUT IT AT THE AHEAD OF THE ROOT"
                    new_root = Node(input_data)
                    new_root.setnextnode(tmp)
                    self.root = new_root
                
            else:
                done = False

                while ( tmp.getnextnode() != None):
                    print tmp.getdata()[2]
                    #now check if our value is between two nodes, if so we insert it in the middle
   #                 print "INPUT DATA: ",input_data,"FIRST NODE: ",tmp.getdata()[2],"SECOND NODE: ",tmp.getnextnode().getdata()[2]
                        
                    if input_data[2] < tmp.getdata()[2] and input_data[2] > tmp.getnextnode().getdata()[2]:
#                        print "IN BETWEEEN " 
                        lead = tmp.getnextnode()
                        follower = tmp
                        new_node = Node(input_data)
                        new_node.setnextnode(lead)
                        follower.setnextnode(new_node)
                        done = True
                        break 
                    if input_data[2] > tmp.getdata()[2]:
                        new_node = Node(input_data)
                        new_node.setnextnode(tmp)
                        self.root = new_node
                        done = True
                        break 

                    tmp = tmp.getnextnode()
                if not done: 
#                        print "PUT IT AT THE END "
                        new_node = Node(input_data)
                        tmp.setnextnode(new_node)

    def isEmpty(self):
        return self.root == None

    def remove(self):
        root_ptr = self.root 
        next = root_ptr.getnextnode()
        self.root = next
        return root_ptr.getdata()
        
    
    def del_with_id(self,node_id):
        itr = self.root 
        if itr == None :
            return 
        if itr.getdata()[0] == node_id:#for the root having the id
            self.root = itr.getnextnode()
        while itr.getnextnode() != None and itr.getnextnode().getdata()[0] != node_id: 
            itr = itr.getnextnode()
            
        if itr.getnextnode() == None:
            return 
        if itr.getnextnode().getdata()[0] == node_id: 
            cur = itr
            next = itr.getnextnode().getnextnode()
            itr.setnextnode(next)
            
