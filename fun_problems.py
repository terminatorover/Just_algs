#/bin/usr/python


#string reversal via recursion 
def rev_s( input):
    if len(input)==1:
        return input
    else:
        return input[-1]+(rev_s(input[:len(input)-1]))

print rev_s("hello")


#palindrome checker via recursion 

def p_check( input):
    pure = input.split()
    input = ''.join(pure)
    if len(input) <=1:
        return True 
    else:
        first = input[0].upper()
        last = input[-1].upper()
        if ( first != last):
            return False
        else:
            return p_check(input[1:len(input)-1])

print p_check("aibohphobia")            
print p_check("Live not on evil")

