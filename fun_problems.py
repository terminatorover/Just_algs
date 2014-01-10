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
    '''takes a list of queues (the one with numbers in it) and another list of
    stack 2(which will be empty )as input to give us an s2 with ordered numbers(
    all the phone numbers ordered with respect to a particular digit------
    ----Note the first queue in the list of queue is the digit 9 bucket and increases'''
    test_s = dstructs.Stack()
    count = 0
    digit = 9 - digit
    print "THE DIGIT***************" + str(digit)
    for itr in range(len(s1)):
        count += 1
        
        for itr2 in range(s1[itr].size()):
            num = s1[itr].dequeue()
            bucket_ind = num[digit] #this tells us which bucket in s2 this num goes to
            
            s2[int(9-int(bucket_ind))].enqueue(num)


    return s2
        

def radix_sort( numbers):
    '''attempt to sort phone numbers (inputed as strings). The inputs will be 
    a list of phone numbers given as strings'''
    buckets1 = [ dstructs.Queue() for x in range(10)]# get 9 stacks(buckets) 1 for each digit
    buckets2 = [ dstructs.Queue() for x in range(10)]# get 9 stacks(buckets) 1 for each digit
    number_of_digits = len(numbers[0])
    #push all the numbers into the list of appropriate buckets(aka corresponding to their LSD 
    for num in numbers:
        bucket_ind = num[-1]
        buckets1[9-int(bucket_ind)].enqueue(num)#makes sure that a phone number with LSD 9 goes to the first index (stack) of the list
    digit_count = 1 #because we have already aranged the numbers according to their last digit
    while ( digit_count < number_of_digits): 
        if ( digit_count % 2 == 1):
            buckets2 = helper(buckets1,buckets2,digit_count)
        else:
            buckets1 = helper(buckets2,buckets1,digit_count)
        digit_count += 1
    result = []    
    if ((digit_count-1) % 2 == 0):
        for itr in range(len(buckets1)):
            for itr2 in range(buckets1[itr].size()):
                num = buckets1[itr].dequeue()
                result.append(num)
    else:
        for itr in range(len(buckets2)):
            for itr2 in range(buckets2[itr].size()):
                num = buckets2[itr].dequeue()
                result.append(num)
    
    return result 

print "+++++++++++++++" + str(radix_sort(["3157505545","3157506807","3157508117","3157509946","3158255214"]))+ "-------"
check = []


for el in ["30123456789","59874561230","43157505545"]:
    check.append(int (el))

print check 
