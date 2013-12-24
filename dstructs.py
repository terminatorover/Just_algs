#usr/bin/python 


#binary search tree 
class Node : 
    def __init__(self,key=None ,value=None ,right = None, left= None, no = 1):
        self.key = key 
        self.value = value 
        self.right = right 
        self.left = left 
        self.no = no #number of children defaults to 0
    
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
        return 0
            
