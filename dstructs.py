#/bin/usr/python 

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,new_item):
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        if not( self.isEmpty()):
            return self.items[-1]
        else:
            return False 
    def iter(self):
        strr = ""
        self.items.reverse()
        for item in self.items:
            strr += str(item)
        return strr
#------------------------------Parentheses ---------------------
def parcheck( string):
    d_s = Stack()
    failed = False
    for el in string:
        if ( el in  '()'):
            if el == '(':
                d_s.push(el)
            else:
                try:
                    d_s.pop()
                except:
                    failed = True 
        else:
            continue 
        if (failed == True):
             break

    if not failed:

        if d_s.size() > 0:
            return False
        else:
            return True 
    else:
        return False 

sti = "((()))())"
print parcheck(sti)

#------------------------------Parentheses ---------------------
#+++++++++++++++++++++++++++++from decimal to any base under hexamdecimal++++++
def convert(n,base):
    no = n
    s = Stack()
    digits = "0123456789ABCDEF"
    while (1):
        if ( no < base):
            s.push(no)
            break 
        rem = no % base
        s.push(digits[rem])
        no = (no - rem )/ base#the new number
    return s.iter()

print convert( 27,16)    

#+++++++++++++++++++++++++++++to binary+++++++++++++++++++++++++++++

#$$$$$$$$$$$$$$$$$$$$$ infix to postfix$$$$$$$$$$$$$$
def pop_all( my_stack):
    final = []
    while ( my_stack.size()):
        final.append( my_stack.pop() )
    return final
def i_post(exp):
    s = Stack()
    output = []
    a_exp = exp.split()
    symbols = "ABCD"
    l_aexp = len(a_exp)
    index = 0
    value = {}
    value['+'] = 1
    value['-'] = 2
    value['*'] = 3
    value['/'] = 4
    while ( index < l_aexp):
        if a_exp[index] in symbols:
            output.append(a_exp[index])
        else:
            top = s.peek()
            if top == False:
                s.push(a_exp[index])
            elif (value[top]< value[a_exp[index]]): 
                s.push(a_exp[index])
            else:
                output.extend(pop_all(s))
                s.push(a_exp[index])
        index += 1
    output.extend(pop_all(s))
    return output            

print i_post("A * B + C * D")
print i_post("A + B * C")
#$$$$$$$$$$$$$$$$$$$$$ infix to postfix$$$$$$$$$$$$$$

class Queue:
    def __init__(self):
        self.items = [] 
    
        
