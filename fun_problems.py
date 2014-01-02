#/bin/usr/python


#string reversal via recursion 
def rev_s( input):
    if len(input)==1:
        return input
    else:
        return input[-1]+(rev_s(input[:len(input)-1]))

print rev_s("abcde")
