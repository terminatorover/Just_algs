#!/usr/bin/python
class Stack:
    def __init__(self):
        self.alist = []
    def push(self,item):
        self.alist.append(item)
    def pop(self):
        return self.alist.pop()
    def isEmpty(self):
        return self.alist == []
class Node:
    def __init__(self,let,flag=None):
        self.this_letter = let
        self.next = {}#maps letters to their corresponding nodes
        self.flag = flag
    def get_letter(self):
        return self.this_letter
    def all_nodes(self):
        return self.next.values()
    def get_node(self,input_letter):
        return self.next.get(input_letter)
    def _addletter(self,input_letter,input_node):
        self.next[input_letter] = input_node
        
    def full_word(self):
        return self.flag != None
    

class Trie:
    def __init__(self):
        self.root = Node(" ")
    
    def add(self,word):
        tmp  = self.root 
        len_word = len(word)
        for ind in range(len_word):#first we do a longest prefix match(seaching for abcd we go until we get the last node in our node corresponding to abcd 
            next = tmp.get_node(word[ind])
            if next == None:
                self.add_routine(word[ind:],tmp)#when we find that we have reached the last prefix
                return 
            else:
                tmp = next

    def add_routine(self,input_word,input_node):
        #takes in a node and a word to add and populates the trie by extending the given word with the letters of the input word
        current_node = input_node
        len_word = len(input_word)
        for ind in range( len_word):
            letter = input_word[ind]
            if ind != len_word - 1:
                new_node = Node(letter)
                current_node._addletter(letter,new_node)
            else:#because we want to set the flag to true for the last letter of the word
                new_node = Node(letter,True)
                current_node._addletter(letter,new_node)
                
            current_node = current_node.get_node(letter)

    def exists(self,prefix):
        #checks if teh given prefix is present if so gives us the last node containting the last leter of the prefix, else returns none
        current = self.root
        for ele in prefix:

            if current.get_node(ele) == None:#then you don't have that letter DONE
                return None
            else:
                current = current.get_node(ele)
                
        return current

    def reccomend(self,prefix,count):
        #takes in the user inputed string prefix and the number of recommendations needed and returns as many as count if there are that many and it stops at that point if there happen to be more words to reccomend. 
        recs = []
        s = Stack()
        last_node = self.exists(prefix)
        if last_node == None: #then their is no prefix match(aka nothing in the trie that even matches the user inputed string
            return recs 

        s.push((last_node,prefix)) #add the node and the word assocaited with it (aka the letters before it  + its own letter

        while (  (not s.isEmpty() ) and count > len(recs)):
            node,word = s.pop()
            if node.full_word():
                recs.append(word)
            for node_child in node.all_nodes():
                s.push((node_child, word + node_child.get_letter()))
        return recs

        
    def find_longest(self,input_ip):
        ret_val = None
        cur_val = ""
        current = self.root
        for bit in input_ip:
            if current.get_node(bit) == None:#then you don't have that letter :DONE
                return ret_val  
            current = current.get_node(bit)
            cur_val += bit
            if current.full_word():
                ret_val = cur_val 


        return ret_val
        

new_trie = Trie()
new_trie.add("dog")
new_trie.add("doge")
new_trie.add("catle")
new_trie.add("catleelkj")
new_trie.add("catled")

#print new_trie.reccomend("z",3)
print new_trie.find_longest("catleelk")
