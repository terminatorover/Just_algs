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
            if self.vertcies.get(neigh_id) != None:
                new_vertex.add_neighbour(neigh_id,to[neigh_id])
                self.vertcies[neigh_id].add_neighbour(key,to[neigh_id])
            
        #now,that you have established all the connections, add the vertex to our collective set of vertcies
        self.vertcies[key] = new_vertex
    
    def add_edge(self,src,dest,weight):
        #given the id of the two nodes src,dest it creates an edge between them , aka lets each vetex know that it is connected to the other by the given weight(aka add that data to each node)
        self.vertcies[src].add_neighbour(dest,weight)
        self.vertcies[dest].add_neighbour(src,weight)
        
    def connection_check(self,vert_id, dest):
        if self.vertcies.get(vert_id) != None:
            src = self.vertcies.get(vert_id)
            return src.is_connected(dest)
        else:
            return None
    def vert_exist(self,vert_id):
        return not( self.vertcies.get(vert_id) == None )
    def get_vert(self,vert_id):
        return self.vertcies.get(vert_id)

g = Graph()
g.add_vertex(2,{})
g.add_vertex(4,{})
g.add_edge(2,4,3)


def get_all_short( TQueue, cost):
    #helper , takes in the priority queue and the cost of the shortest path found so far and returns
    #all other shortest paths , aka paths of the same cost if there are any left if not retuns None
    remaining = []
    cur_top = TQueue.add()
    while( not(TQueue.isEmpty()) and cur_top[2] <= cost):
        remaining.append( cur_top[1])
        cur_top = TQueue.remove()
    return remaining
        
        

def all_shortest_paths( input_graph,src_id,dest_id):
    #given a graph and source,dest, outputs all the shortest paths possible 
    all_short = []
    #first if the source,and dest vertcies are not present in the graph we return nothing
    src_vert_exist = input_graph.vert_exist(src_id)
    dest_vert_exist = input_graph.vert_exist(dest_id)
    if src_vert or dest_vert :
        return []
    
    src_vert = input_graph.get_vert(src_id)
    dest_vert = input_graph.get_vert(dest_id)
    fringe = PQueue()
    
    #now the following will be the data strucutre that will hold the id of current node, the path
    #we took to get there and the cost it took to get there. 
    fringe.add((src_id,[],0))
    done = False #set to true when we have added all our shortest paths to our all_short list
    while ( not ( fringe.isEmpty() ) and not done):

        cur_vert_id,path,cost = fringe.remove() #get a node from the fringe(should be the least costly)
        
        if cur_vert_id == dest_id:#we found our destination
            all_short.append(path)
            remaining_shortest_paths = get_all_short( fringe, cost)
            all_short.extend(remaining_shortest_paths) 
            done = True

        cur_vert = input_graph.get_vert(cur_vert_id)

        for neigh_id,weight in cur_vert.all_neighbours():
            fringe.add((neigh_id , path + [neigh_id] , cost + weight)


    return all_short

    
    
    

        


