#/bin/usr/python 


def in_sort(li):

    for key in range(len(li)):
        for index in range(key-1,-1,-1):
            print key 
            key = index + 1

            if ( li[key] < li[index]):
                tmp = li[key]
                li[key] = li[index]
                li[index] = tmp

            else:
                break 


li = [4,-1,0,10,7,6]
print li
in_sort(li)
print li


def bubble_sort( li):
#trick is not to stop sorting when you find that the next element is bigger 
#different logic(a little bit) compared to that of insertion sort
    for pas in range(len(li)-1,0,-1):
        for ind in range(pas): 
            print ind,pas
            if li[ind] > li[ind+1]:
                tmp = li[ind]
                li[ind] = li[ind + 1]
                li[ind + 1] = tmp 

        
        
li = [4,-1,0,10,7,6]
print li
bubble_sort(li)
print li

#efficient merge sort

def merge_step(list1,list2):
    l_1 = len(list1)
    l_2 = len(list2)
    ind_1 = ind_2 = 0
    result = [] 
    while( ( ind_1 < l_1) and (ind_2 < l_2 )):
        if (list1[ind_1 ] <= list2[ind_2]):
            result.append(list1[ind_1])
            ind_1 +=1 
        else:
            result.append(list1[ind_2])   
            ind_2 +=1 

    result.extend(list1[ind_1:])
    result.extend(list1[ind_2:])
    return result

def merge(input_list):
    if len(input_list ) ==1:
        return input_list
    else:
        mid = len(input_list)/2
        first_half = input_list[:mid]
        second_half = input_list[mid:]
        return merge_step(first_half,second_half)

li = [3,4,-1,0,10,7,6,100]
print li
merge(li)
print li
