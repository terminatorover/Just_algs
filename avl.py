#!/usr/bin/python



class Node:
    def __init__(self,key,h=0,rc=None,lc=None,p=None):
        self.key =  key
        self.rightChild = rc 
        self.leftChild = lc
        self.height = h 
        self.parent = p
        
    def get_data(self):
        return self.key
    def set_key(self,new_key):
        self.key = new_key
    def get_h(self):
        return self.height
    def set_h(self,new_height):
        self.height = new_height
    def get_parent(self):
        return self.parent
    def get_rc(self):
        return self.rightKey
    def get_lc(self):
        return self.leftChild
    def get_height(self):
        return self.height
    def set_rc(self,right_child_node):
        self.rightChild = right_child_node
    def set_lc(self,left_child_node):
        self.leftChild = left_child_node
    def get_parent(self):
        return self.parent
    def has_rc(self):
        return self.rightChild != None
    def has_lc(self):
        return self.leftChild != None
    def has_child(self):
        return self.has_lc() and self.has_rc()
    def is_lc(self):
        return self.parent.key > self.key
    def is_rc(self):
        return self.parent.key < self.key

class AVL:
    def __init__(self):
        self.root  = None
    
    def update(self,node):
        #given a node updates the height of it's parents(used in adding routine)
        #also returns the node in the tree that happens to be unbalanced
        if node == None:
            return None
        if node.get_h() > 2 or node.get_h() < -2:
            #this node is valid so now increment the height of its parent appropraitely
            parent = node.get_parent()
            if parent != None:
                if node.is_lc():
                    parent_h = parent.get_h()
                    parent.set_h(parent_h + 1)
                else:
                    parent_h = parent.get_h()
                    parent.set_h(parent_h - 1)                

            update(parent)
        else:
            return node
        
    #-------------------------------------------------------------ROTATION 
    def l_rotation(self,node):
        #does a left  rotaion given the unbalanced node
        x = node
        y = node.get_rc()
        A = node.get_lc()
        C = y.get_rc()
        B = y.get_lc()
        parent = x.get_parent()
        left_right = x.is_lc()# True if x is the left child False if not
        if parent == None:
            self.root = y 
        else:
            if left_right:#if True it means we should set the parent's left child to y 
                parent.set_lc(y)
            else:
                parent.set_rc(y)
        #pointer movments
        y.set_lc(x)
        y.set_rc(C)

        x.set_lc(A)        
        x.set_rc(B)
        return 
    def r_rotation(self,node):
        #does a  right rotaion given the unbalanced node
        y = node
        x = node.get_lc()
        A = x.get_lc()
        B = x.get_rc()
        C = y.get_rc()
        parent = y.get_parent()
        left_right = y.is_lc()
        if parent == None:
            self.root = x
        else:
            if left_right:#if True it means we should set the parent's left child to y 
                parent.set_lc(x)
            else:
                parent.set_rc(x)
        x.set_lc(A)
        x.set_rc(y)

        y.set_rc(B)
        y.set_lc(C)
        return 


    def balancer(self,node):
        #given the node that isn't balanced balances it figures out which type
        #of rotation to use and then calls one of helper rotation functions
        node_h = node.get_h()
        if node_h > 1:#then its at least an L rotation 
            next_node = node.get_lc()
            if next_node.get_h() >= 1:
                rotation = "LL"
            elif next_node.get_h() <= -1:
                rotation = "LR"
        elif node_h < -1:
            next_node = node.get_rc()
            if next_node.get_h() >= 1:
                rotation = "RL"
            elif next_node.get_h() <= -1:
                rotation = "RR"
        if rotation == "LL":
            self.l_rotation(node)
        elif rotation == "RR":
            self.r_rotation(node)
        elif rotation == "LR":#two rotations, left on the inside and right ont the outside
            self.l_rotation(next_node)
            self.r_rotation(node)
        else:#RL rotation
            self.r_rotation(next_node)
            self.l_rotation(node)
        
        
    def add(self,key):
        #given a key add that to the AVL TREE
        new_node = Node(key)
        #if there are no nodes in the tree we will make this node the head of the tree
        if self.root == None:
            self.root == new_node
            return 
        itr = self.root #get the root node(we know we have because we just checked 
        done = False
        while ( not done ) :
            if itr.get_data() == key:#FOR THIS IMPLEMENATAION WE DON'T ALLOW DUPLICATE VALUES
                done = True 
            if itr.get_data() < key:
                if itr.has_rc():
                    itr = itr.get_rc()
                else:
                    itr.set_rc(new_node)
                    done = True
            else:
                if itr.has_lc():
                    itr = itr.get_lc()
                else:
                    itr.set_lc(new_node)
                    done = True
                    
    def find(self,key):
        #will use _find to do the heavy lifting 
        root = self.root
        return self._find(key,root)
        
    def _find(self,key,node):
        #recursive find subroutine
        if node == None:
            return node
        else:
            if node.get_data() == key:
                return node
            elif node.get_data() < key:
                return _find(key,node.get_rc())
            else:
                return _find(key,node.get_lc())
#------------------------------------------all about deleting--------------------------------            
    def swap_data(self,node1,node2):
        #given two nodes exchanges their keys
        key1 = node1.get_data()
        key2 = node2.get_data()

        node1.set_data(key2)
        node2.set_data(key1)

        
    def find_next_best(self,node):
        #given the key of the node you want to remove this will give you the node that will be 
        #just under your key
        node_for_deletion = node
        if node_for_deletion != None:#the node with the given key exsists
            #now we move left
            cur = node_for_deletion.get_lc()
            while ( cur.get_rc() != None):
                cur = cur.get_rc()

        return cur
            
    def del_node_with_two_children(self,node):
        #given a node with two children it removes it
        #first step get the next best node
        next_best = self.find_next_best(node)
        self.swap_data(next_best,node)#swtich data
        if next_best.has_lc() or next_best.has_rc():#delete the next best node (at the fringe)
            self.del_node_with_one_child(next_best)
        else:
            self.del_node_with_no_child(next_best)
            

    def del_node_with_no_child(self,node):
        #delets a node if it has no children(aka apropraite for that type of deletion)
        #this is the only time the height of the parent(which is the only thing that can change) changes
        parent = node.get_parent()
        if node.is_rc() :
            parent.set_rc( None)
            old_parent_height = parent.get_h()
            parent.set_h(old_parent_height + 1) 
        else:
            parent.set_lc(None)
            old_parent_height = parent.get_h()
            parent.set_h(old_parent_height - 1) 
    def del_node_with_one_child(self,node):
        #deletes a node with only one child
        parent = node.get_parent()
        if node.has_lc():
            child = node.get_lc()
            parent.set_lc(child)
        else:
            child = node.get_rc()
            parent.set_rc(child)
            
        
    def remove(self,key):
        if self.root == None:
            return 
        node_to_del = self.find(key)
        if node_to_del.has_rc() and node_to_del.has_lc():#both children
            self.del_node_with_two_children(node_to_del)
            return 
        if not(node_to_del.has_rc() ) and not(node_to_del.has_lc()):#no children
            self.del_node_with_no_child(node_to_del)
            return 

        self.del_node_with_one_child(node_to_del)
        
    
                                                 
#-------------------------------------------delete DONE ---------------------------------
        

    
        

