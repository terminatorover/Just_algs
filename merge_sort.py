#/bin/usr/python


class Qeue:
    def __init__(self):
        self.the_l = []
    def pull (self):
        if (len(self.the_l)>0):
            item = self.the_l[0]
            del self.the_l[0]
            return item 

        else:
            return False
    def get_item(self):
        if (len(self.the_l)>0):
            item = self.the_l[0]
  
            return item 

            
        else:
            return "NO"
    def to_q(self,a_list):
        
        for el in a_list:
            self.the_l.append(el)
            
    def add_item( self,num):
        self.the_l.append(num)
    def leng(self):
        return len(self.the_l)
            
    def is_empty(self):
        if len(self.the_l) == 0:
            return True 
        else :
            return False 
    def see(self):
        return self.the_l 
    def sel(self,to,upto):
        return self.the_l[to:upto]

def m_step(l1, l2):
    done = False
    result = Qeue()
    t_len = (l1.leng() + l2.leng())
    check = 0
#    while (not done):
    while ( not done):
        b1 = l1.see()
        b2 = l2.see()
        
#        print "list1 Before: " + str(b1) + " " + "list2 Before: " + str(b2)
        left1 = l1.get_item()
        left2 = l2.get_item()
 #       print "left`: " + str(left1) + " " +  "left2: " + str(left2)

 
        
        if ( ( left1 == "NO" )and (left2 == "NO" )):
            return result 
        
        if (left2 == "NO"):
            while ( not l1.is_empty()):
                the_i = l1.get_item()
                result.add_item(the_i)
                l1.pull()
                check +=1
            
        elif (left1 == "NO"):
            while ( not l2.is_empty()):
                the_i = l2.get_item()
                result.add_item(the_i)
                l2.pull()
                check +=1
                
            
        else:    
            fav = less(left1,left2)
            if ( l1.get_item() == fav):
                l1.pull()
            if ( l2.get_item()== fav):
                l2.pull()
            
        
            result.add_item(fav)
#            print "result: " + str(result.see())

  #      print "list1 After: " + str(l1.see()) + " " + "list2 After: " + str(l2.see())

        if ( result.leng() == t_len):
            done = True 

            return result 


#        return result 

            
        
    

def less(n1,n2):
    if n1 < n2:
        return n1
    else:
        return n2 


def l_q( a_list):
    q = Qeue()
    for el in a_list:
        q.add_item(el)
    return q

def m_sort( ml):
    #base case
    if ml.leng() <= 1:
        return ml
    
    le = ml.leng()
    half = int(le/2)
    first = ml.sel(0,half)
    second = ml.sel(half,le)
    print first 
    print second 
    f = l_q( first)
    s = l_q (second)
    
    return m_step(m_sort(f),m_sort(s)  )

    

q1 = Qeue()
q2 = Qeue()

q1.add_item(1)
q1.add_item(3)
q1.add_item(-3)
q1.add_item(5)
q1.add_item(101)
q1.add_item(7)


q2.add_item(0)
q2.add_item(2)
q2.add_item(4)
q2.add_item(6)
q2.add_item(10)
#print q1.see()
#print q2.see()


#print str(m_step( q1,q2).see() )+ " REsult " 
print m_sort(q1).see()


