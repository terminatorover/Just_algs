#ur/bin/python 

from ll import *


class Vertex:
    def __init__(self,key):
        self.id = key
        self.neigh = {}#key/value pair where keys are ids of neighbours and values are their corresponding edge weights
    def add_neighbour(self,new_key,weight):
        self.neigh[new_key] = weight
    def all_neighbours(self):
        return [ (neigh,self.neigh[neigh]) for neigh in self.neigh.keys() ]#returns a list of tuples where the first element is the id of the neighbour and the second one is the weight of the corresponding edge
    def is_connected(self,check_id):
        return not( None == self.neigh.get(check_id) )

    def del_neigh(self,neigh_id):
        if self.neigh.get(neigh_id) != None:
            self.neigh.pop(neigh_id)

class Graph:
    def __init__(self):
        self.vertcies = {} #maps vertex ids to vertex objects
    
    def add_vertex(self,key,to):
        #specify the id of the vertex you are creating and all the other vertcies its connected to 
        #via a dictionary where the keys are the neighbours id's and the values are the weights of the 
        #connections(edge weights)
        new_vertex = Vertex(key)#make the new vertex

        attach_to = to.keys()

        for neigh_id in attach_to:#make sure it and its neighbour both know that they are now related
            if self.vertcies.get(neigh_id) == None: #important, if the neighbour you are trying to connect to doesn't exist make it and add it to the set of vertcies the graph has
                new_neigh = Vertex(neigh_id)
                self.vertcies[neigh_id] = new_neigh
            new_vertex.add_neighbour(neigh_id,to[neigh_id])
            self.vertcies[neigh_id].add_neighbour(key,to[neigh_id])
            
        #now,that you have established all the connections, add the vertex to our collective set of vertcies
        self.vertcies[key] = new_vertex
    
    def add_undirected_edge(self,src,dest,weight):
        #given the id of the two nodes src,dest it creates an edge between them , aka lets each vetex know that it is connected to the other by the given weight(aka add that data to each node)
        if self.vertcies.get(src) == None or self.vertcies.get(dest) == None:
            return False

        self.vertcies[src].add_neighbour(dest,weight)
        self.vertcies[dest].add_neighbour(src,weight)
        return True

    def add_directed_edge(self,src,dest,weight):
        if self.vertcies.get(src) == None:
            return False
        self.vertcies[src].add_neighbour(dest,weight)
        return True

    def connection_check(self,vert_id, dest):
        if self.vertcies.get(vert_id) != None:
            src = self.vertcies.get(vert_id)
            return src.is_connected(dest)
        else:
            return None
    def vert_exist(self,vert_id):
        return vert_id in self.vertcies 
    def get_vert(self,vert_id):
        return self.vertcies.get(vert_id)
    def remove_edge(self,src,dest):
        #assumes a directed edge
        if self.vertcies.get(src) == None or self.vertcies.get(dest) == None:
            return False
            
        self.vertcies.get(src).del_neigh(dest)
        self.vertcies.get(dest).del_neigh(src)
        return True
        
    def __str__(self):
        return str(self.vertcies.keys())
g = Graph()
g.add_vertex(2,{})
g.add_vertex(4,{})



def get_all_short( TQueue, cost,dest_id):
    #helper , takes in the priority queue and the cost of the shortest path found so far and returns
    #all other shortest paths , aka paths of the same cost if there are any left if not retuns None
    remaining = []
    cur_top = TQueue.remove()
    while( not(TQueue.isEmpty()) and cur_top[2] <= cost and cur_top[0] == dest_id ):
        remaining.append( cur_top[1])
        cur_top = TQueue.remove()
    return remaining
        

def all_shortest_paths( input_graph,src_id,dest_id):
    #given a graph and source,dest, outputs all the shortest paths possible 
    all_short = []
    #first if the source,and dest vertcies are not present in the graph we return nothing
    src_vert_exist = input_graph.vert_exist(src_id)
    dest_vert_exist = input_graph.vert_exist(dest_id)

    if not(src_vert_exist) or not(dest_vert_exist) :
        return []
    
    src_vert = input_graph.get_vert(src_id)
    dest_vert = input_graph.get_vert(dest_id)
    fringe = TQueue()
    
    #now the following will be the data strucutre that will hold the id of current node, the path
    #we took to get there and the cost it took to get there. 
    fringe.add((src_id,[],0))
    done = False #set to true when we have added all our shortest paths to our all_short list

    while ( not ( fringe.isEmpty() ) and not done):

        cur_vert_id,path,cost = fringe.remove() #get a node from the fringe(should be the least costly)
        
        if cur_vert_id == dest_id:#we found our destination
            all_short.append(path)
            remaining_shortest_paths = get_all_short( fringe, cost,dest_id)
            all_short.extend(remaining_shortest_paths) 
            done = True

        cur_vert = input_graph.get_vert(cur_vert_id)

        for neigh_id,weight in cur_vert.all_neighbours():
            fringe.add((neigh_id , path + [neigh_id] , cost + weight) )
            
                       
                       
                       


    return all_short

    

                           
#----------------------------------------------------processing input file

def get_neighbour_cords( (x,y), (W,H)):

#takes in (x,y) coordinates and gives us back all the neightbouring node's coordinates and their weights so we can just use the out put of this function for add_vertex 

    neighs = {}
    left = ( x -1, y)
    right = ( x + 1 ,y)
    top = ( x , y + 1)
    bottom = ( x ,y - 1)
    if valid_cord( left, (W,H)):
        neighs[left] = 1                           
    if valid_cord( right, (W,H)):
        neighs[right] = 1                           
    if valid_cord( top, (W,H)):
        neighs[top] = 1                           
    if valid_cord( bottom, (W,H)):
        neighs[bottom] = 1        
    return neighs

def all_cords( W,H):
    "width and height of the matrix world "
    all_c = []                       
    for i in range(W+1):
        for j in range(H+1):
                all_c.append((i,j) )
    return all_c
def valid_cord((x,y) ,(W,H)):
    if ( x > W or  x < 0  or y > H or y < 0):
        return False                           
    else:
        return True                           

#given W,H use all_cords to get all coordinates 
      #go through each coordinate and use get_neighbour_cord's output(which is a dictionary of all the valid! neighbouring vertcies and all their weights) as input for the add_vertex function (which takes the id of the new vertex and all the neighbours and their neighbours with weights(dic key/value pair)

  #-----> now that you have the graph (aka the x,y plane you need to get rid of 
                       #all the edges involving the construction , so we just need to make sure no othervertex can link up to them . to do this we simply loop over the construction site nodes and get all their valid neigbours and for each valid neigbour we use remove_edge where the src is the neighour and the dest the construction site--- so that we can remove all of the possible ways to get to it and viceversa . then we remove it off the graphs collection of vertcies. the reason that the last step is not sucfficent to get rid of these construction nodes is that when creating the graph we assumed they were linked up to their neighbours so the neigbours have edges that link up to these construction zones(which is wrong which is why we need to get rid of them for an accuate representaion
                           
def no_paths( W,H, exceptions):
    """Given the width and heigh of the box ( on the x,y plane ) + the construction sites returns 
    #the number of paths 
    #---note that the start is always be (0,0) and (W,H)"""
    all_coordinates = all_cords( W,H )
    #Now create the graph
    G = Graph()
    for x,y in all_coordinates:
        map_to = get_neighbour_cords ( (x,y), ( W,H) )
        G.add_vertex( (x,y), map_to)

    #now we have made the graph with FULL CONNECTION(AKA like an x,y plane now we need to eliminate construction coordinates
#    print G
    for x,y in exceptions:
        map_to = get_neighbour_cords ( (x,y), ( W,H) )
        for exception_neigh in map_to.keys():
            G.remove_edge( exception_neigh , ( x,y) )

    #NOW WE HAVE AN ACCURATE GRAPH , and we run Dijkstra's to get a list of all the shortest paths
    all_shortest = all_shortest_paths( G , (0,0) , (W,H) )
    
    return len(all_shortest)
    

                           
print "FINAL ANSWER", no_paths(2,2, [(1,1)])
