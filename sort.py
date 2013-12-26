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
    for pas in range(len(li)-1,-1,-1):
        for ind in range(pas-1): 
            print ind,pas
            if li[ind] > li[ind+1]:
                tmp = li[ind]
                li[ind] = li[ind + 1]
                li[ind + 1] = li[ind]

        
        
li = [4,-1,0,10,7,6]
print li
bubble_sort(li)
print li
