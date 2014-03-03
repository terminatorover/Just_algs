#!bin/usr/python 
#concept wise this really works like a turing machine

def find_space( li,ind):
    '''x^ y output #x  ^y(the arrow is under y)
    #assume that the ind is under the first space'''
    if len(li) == ind:
        return -1 
    for i in range(ind,len(li)):
        if li[i] == ' ':
            continue
        else:

            return i

    return i #happens when there is space at the end of the string 

def word_rev( li, start,end):
    #takes a word(a part of the list in this case) and reverses it (that part only
    mid = ((end-start)+1)/2
    for x in range(start,mid+start):
        tmp = li[x]
        li[x] = li[end-(x-start)]
        li[end-(x-start)] = tmp 
        
        
    
def rev_str( li):
    done = False
    li.reverse()
    len_li = len(li)
    start = 0
    end = 0
    done = False
    while ( not done) :
        while ( (li[end]!= ' ')):# simply trying to find the word in the string
            end += 1
            if ( end == len_li):
                done = True 
                break 

        word_rev(li,start,end-1)
        start = find_space(li,end)#find the next space
        if ( start == -1):
            done = True
        else:
            end = start
        
        
        
x= "abc kbg xyz  "
print x
y = list(x)

rev_str(y)
j = ' '.join(y)
print j
