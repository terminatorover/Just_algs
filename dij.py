#/bin/usr/python 

#assume you have an adjaceny list impmlemntation of a matrix 



def initalize( no_nodes, start, dest):
    '''returns the pred dictionary(nodes and their predcessors) , and the univisted list of nodes
     '''
    unvisited = [ x for x in range(no_nodes)]#if you ask for 10 nodes you will get 10 nodes starting from 0 to 9 
    pred = {}
    for node in unvisited:
        if node != start:
            dis[node]=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            pred[node] = "un"
        else:
            dis[node]= 0
            pred[node]= "start"
    return [unvisited,pred]

def pick_shortest( dis,start,unvisited):#start is the vertex of the start node
    nodes = unvisited
    if len(nodes) > 0:
        #we check if the start node is still if so then the shortest dis is starts nodes (0)
        if ( start in unvisited):
            del unvisited[start]
            return start
        else:
            node = nodes[0]
            shortest = dis[node]
            closet_n = node
            for n in nodes:
                if (dis[n]< shortest ):
                    shortest = dis[n]
                    closet_n = n
    del unvisited[closet_n]
    return closet_n
#### code to teste pick shortest
unvisited = [ x for x in range(10)]
del unvisited[4]
print unvisited 
start = 3
dis = {}
#[(dis[x]=x) for x in range(10)]

for x  in range(10):
    if x != 4:
        dis[x]="i"
        dis[x] = 100000000000000000000000000000000000000000000000000000
    else:
        dis[x]= 0

#print pick_shortest(dis,4,unvisited)
            
######            
def update_neigh(dis,cur,unvisited,edj,pred):
    neigh = edj[cur]
    neigh_nodes = neigh.keys()
    for n in neigh_nodes:
        if n in unvisited:
            if (dis[n]> dis[cur] + 1 ):####notice the +1 this is because the way my problem is setup i know the edge weight between two nodes is always 1
                dis[n]=dis[cur] + 1
                pred[n]= str(cur)
            

def path_finder(pred,dest):
    '''takes in the predecssor dic and the final destination and retraces the steps back to the start'''
    result = []

    cur = str(dest)
    while ( cur != "start"):
        result.append(cur)
        cur = pred[int(cur)]
    
    result.append(cur)
    result.reverse()
    return result
    
pred = {0:"start",1:"0",2:"1",3:"2"}
dest = 3
print path_finder(pred,3)
        
    
    
#CREATING GRAPHS------------*****************************------------*****************************
a_l = {}# this will be our adjacency dic

####------>>>>>>>>>FIRST WE MAKE THE MATRIX
matrix =[]
no_p = {} #helps us translate node number to coordinates
p_no = {} #Helps us translate coordinates to node numbers
allowed = {}#helps us see if we can go through that town 
#these parameters should be read from the file
H= 3
W = 4
for y in range (H):
    matrix.append([])
    for x in range(W):
        matrix[y].append(x+y)
        no_p [(x + y )] = (x,y)
        p_no [(x,y)]= (x +y )
        allowed[(x,y)]= True


list_of_not_allowed_towns = []#this should be populated from the input

for pair in list_of_not_allowed_towns:
    #iterate thorugh towns that are not allowed and make them "unallowed" set thier
    #values false in the allowed dictionary
    allowed[pair] = False 
    
def  find_neigh( town): #the input must be an x,y pair , and given a town it gives you all the nodes that need to be neighbours of this town in a list
    neigh = []
    all_towns = p_no.keys()
    for a in [-1,0,1]:    
        for b in [-1,0,1]:    
            p_town = [ town[0] +a , town[1]+ b]
            if ( (p_town !=town ) and (p_town in all_towns)):
                if (allowed(p_town)):
                    node = p_no ( p_town)
                    neigh.append(node)
    return neigh

#==================================================================
#Now we create the adjacency matrix

all_towns = no_p.keys()
all_towns.sort()
for town in all_towns:
    pair = no_p[town]
    if allowed[(pair)]:
        a_l[town]= find_neigh(pair)

#==================================================================

    

        
    





#------------*****************************------------*****************************


def dij( edj,unvisited,dis,des,pred):
    '''dis is the adjaceny list edge representation
    univisted is a list of unvisited nodes orderd numericall
    dis is a dictionary that has nodes and their corresponding distances 
    dest is going to be our final node
    pred is a dic that has keys as the nodes and the values as the previous nodes'''
   #this holds the node before the current node that will give us the shortest path
    #dis has the shortest distance to this current day haha
    
    
    
    while (not done):
        
        curr = pick_shortest( dis,start,unvisited)
        
        if ( curr == des):
            path =  path_finder(pred,des)
            done = True 
            break 
        update_neigh(dis,cur,unvisited,edj,pred)
        if ((len(unvisited)==0)):#done when all the towns are visited
            path =  path_finder(pred,des)
            done = True 
        

    return path
