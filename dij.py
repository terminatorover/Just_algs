#/bin/usr/python 

#assume you have an adjaceny list impmlemntation of a matrix 



def initalize( no_nodes, start, dest):
    '''returns the dis adjacency list'''


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
                pred[n]= cur
            

def path_finder(pred,dest):
    result = []
    
    
       
def dij( edj,unvisited,dis,des,pred):
    '''dis is the adjaceny list edge representation
    univisted is a list of unvisited nodes orderd numericall
    dis is a dictionary that has nodes and their corresponding distances 
    dest is going to be our final node
    pred is a dic that has keys as the nodes and the values as the previous nodes'''
   }#this holds the node before the current node that will give us the shortest path
    #dis has the shortest distance to this current day
    while (not done):
        
        curr = pick_shortest( dis,start,unvisited):
        if ( curr = des):
            
            break 
        update_neigh
        if ((len(unvisited)==0)):#done when all the towns are visited
            done = True 
        
