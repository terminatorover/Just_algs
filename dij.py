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
