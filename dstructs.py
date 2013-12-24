#usr/bin/python 


#binary search tree 
class Node : 
    def __init__(self,key=None ,value=None ,right = None, left= None, no = 1):#default vals specified
        self.key = key 
        self.value = value 
        self.right = right 
        self.left = left 
        self.no = no 
    
    def get_key(self):
        return self.key
    def get_val(self):
        return self.get_val
    def get_right (self):
        return self.right 
    def get_left (self):
        return self.left
    def get_no (self):
        return self.no 

    def set_key(self,key):
        self.key = key 
    def set_val(self,value):
        self.value = value
    def set_right (self,right):
        self.right = right 
    def set_left (self,left):
        self.left = left 
    def set_no (self,no):
        self.no = no

class BST:
    
    def __init__(self):
        self.root = None  
        
    def insert(self,key,value):
        if self.root == None:
            new = Node ( key, value)
            self.root = new
        else:
            cur = self.root
            done = False 
            while ( not done ):
                if ( cur.get_key() == key):
                    done = True #meaning that the key to be inserted already exists

                
                elif ( cur.get_key() < key ):
                    if ( cur.get_right() != None):
                        cur = cur.get_right()
                    else:
                        new = Node ( key, value)
                        cur.set_right(new)
                        done = True
                else:
                    if ( cur.get_left() != None):
                        cur = cur.get_left(new) 
                    else:
                        new = Node ( key, value)
                        cur.set_left(new)
                        done = True
                        
                    
                
        



    def find( self, key):
        if self.root == None or self.root == key ):
            return self.root
        elif self.root.get_key() < key: 
            return find (self, self.root.get_right() , key)
        else:
            return find (self, self.root.get_left() , key)
    

        
