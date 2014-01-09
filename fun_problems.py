#/bin/usr/python
import dstructs

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


#-------radix sort -----
#/helper function
def helper( s1,s2,digit):
    '''takes a list of stacks (the one with numbers in it) and another list of
    stack 2(which will be empty )as input to give us an s2 with ordered numbers(
    all the phone numbers ordered with respect to a particular digit------
    ----Note the first stack in the list of stack is the digit 9 bucket and increases'''
    test_s = dstructs.Stack()
    count = 0
    digit = 9 - digit
    print "THE DIGIT***************" + str(digit)
    for stack in s1:
 #       print "BEFORE---------At index "+ str(count) + str(stack.see())
        count += 1
        for num in stack.all_ele():
            bucket_ind = num[digit] #this tells us which bucket in s2 this num goes to
#            print "phone NUmber:   " + str(num)+ " pushed to bucket no " + str(9-int(bucket_ind) )
            s2[int(9-int(bucket_ind))].push(num)
    count_2 = 0
    for stack in s2:
#        print "+++++++++++++++" + str(stack == test_s)
#        print stack 
        print "AFTER---------At index "+ str(count_2) + str(stack.see())
        count_2 += 1
    return s2
        

def radix_sort( numbers):
    '''attempt to sort phone numbers (inputed as strings). The inputs will be 
    a list of phone numbers given as strings'''
    buckets1 = [ dstructs.Stack() for x in range(10)]# get 9 stacks(buckets) 1 for each digit
    buckets2 = [ dstructs.Stack() for x in range(10)]# get 9 stacks(buckets) 1 for each digit
    number_of_digits = len(numbers[0])
    print "===========" + str(number_of_digits) + "=================="

    #push all the numbers into the list of appropriate buckets(aka corresponding to their LSD 
    for num in numbers:
        bucket_ind = num[-1]
        buckets1[9-int(bucket_ind)].push(num)#makes sure that a phone number with LSD 9 goes to the first index (stack) of the list
        print "bucket index " + bucket_ind
        print "******"+str(9-int(bucket_ind)) +"********"+ str( buckets1[9-int(bucket_ind)].see()) + "*******************"
    digit_count = 1 #because we have already aranged the numbers according to their last digit
    while ( digit_count < number_of_digits): 
        if ( digit_count % 2 == 1):
            buckets2 = helper(buckets1,buckets2,digit_count)
            buckets1 = [ dstructs.Stack() for x in range(10)]# erase all the entries in the stacks
        else:
            buckets1 = helper(buckets2,buckets1,digit_count)
            buckets2 = [ dstructs.Stack() for x in range(10)]# erase all the entries in the stacks
        digit_count += 1
    result = []    
    if ((digit_count-1) % 2 == 1):
        for stack in buckets2:
            entries = stack.all_ele()
            result.extend(entries)
    else:
        for stack in buckets1:
            entries = stack.all_ele()
            result.extend(entries)

            
    return result 

print "+++++++++++++++" + str(radix_sort(["0123456789","9874561230","3157505545"]))+ "-------"
