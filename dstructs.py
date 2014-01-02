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
def pop_all( my_stack, alll, value, key):
    final = []
    if alll:
 
        while ( my_stack.size()):
            final.append( my_stack.pop() )
        return final
    else:
 
        while ( my_stack.size() and (value[my_stack.peek()] > value[key])):
            final.append( my_stack.pop() )
        return final

        
def i_post(exp):
    s = Stack()
    output = []
    a_exp = exp.split()
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
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
                output.extend(pop_all(s,0,value,a_exp[index]))
                s.push(a_exp[index])
        index += 1
    output.extend(pop_all(s,1,value,'+'))
    return output            

print i_post("A * B + C * D")
print i_post("A + B * C")
#$$$$$$$$$$$$$$$$$$$$$ infix to postfix$$$$$$$$$$$$$$

#-----------------------------postfix eval ----------------
def pop_eval( stack,operation):
    '''Pops the last two elements on the stack and then 
    applies the operation onto them '''
    ns = []
    for i in range(2):
        ns.append(int(stack.pop()))
    if ( operation == '+'):
        return ns[1] + ns[0]
    if ( operation == '-'):
        return ns[0] - ns[1]        
    if ( operation == '*'):
        return ns[0] * ns[1]
    if ( operation == '/'):
        return float(ns[1]) / ns[0]        

        
def p_e( user_input):
    '''evaluatse a postfix expression , input should be a
    string where each char is followed by a space'''
    s = Stack()
    operations = '+-/*'
    ui = user_input.split()
    for el in  ui:
        if ( el not in operations):
            s.push(int(el))
        else:
            computed =  pop_eval(s,el)
            s.push(computed)
    return s.pop()
print p_e('7 8 + 3 2 + /')
#-----------------------------postfix eval ----------------

#-----Queue(better O(1) for removing elements and O(n) for adding elements 
class Queue:
    def __init__(self):
        self.items = [] 
    def enqueue (self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def see ( self):
        return [x for x in self.items]
#----------hot potato simulation 

def hot_potato( ppl, num):
    q = Queue()
    for person in ppl:
        q.enqueue(person)

    while( q.size() != 1):
        count  = 0
        while ( count < num  ):
            front = q.dequeue()
            q.enqueue(front)
            count += 1
        
    return q.dequeue()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
