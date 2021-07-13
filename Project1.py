# Constructs a graph data structure.
#  (c) 2021 Rios
#
# Date: 7/8/2021
# Name: Rios 
# Student ID: 006666515
# Emai: Rios.rios@student.csulb.edu
# Version: 1.0.0





class Graph(object):
    def __init__(self):
        #defining empty dictionary
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        new_v = Vertex(node)
        self.vert_dict[node] = new_v
        self.num_vertices = self.num_vertices + 1

    #returns node value if it is in graph
    def get_vertex(self,node):
        if node not in self.vert_dict:
            print(node, "not in graph")
        else:
            return node

    def add_edge(self, from_edge, to_edge, weight):
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)

        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)

        self.vert_dict[from_edge].add_neighbour(self.vert_dict[to_edge], weight)
      

    def get_vertices(self):
        return self.vert_dict.keys()

    #plotting our graph 
    def graph_summary(self):
        for i in self.get_vertices():
            node = self.vert_dict[i]
            for j in node.get_connections():
                #j_str = str(j)
               # print(str(node.id))
                print(i, '->', j.get_id( ) , ' : ', node.get_weight(j))



class Vertex:

    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    #returns  all connections is our adjcent dictionary
    def get_connections(self):
        return self.adjacent.keys()

    def add_neighbour(self, obj_neighbour, weight):
        self.adjacent[obj_neighbour] = weight

    def get_id(self):
        return self.id

    #gets weight of selected neighbour
    def get_weight(self, neighbour):
        return self.adjacent[neighbour]


#########################################################################################
def main():
    print("Setting up basic graph")

    graph = Graph()

    #setting up vertex 
    graph.add_vertex('s')
    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    
    #test 
    #should print vertext not in graph
    graph.get_vertex('r')
    
    #adding edges with weights, From -> TO and weight value
    graph.add_edge('s','a',10)
    graph.add_edge('s','c',5)
    graph.add_edge('a','c',2)
    graph.add_edge('a','b',1)
    graph.add_edge('b','d',4)
    graph.add_edge('c','a',3)
    graph.add_edge('c','b',9)
    graph.add_edge('c','d',2)
    graph.add_edge('d','b',6)
    graph.add_edge('d','s',7)



    graph.graph_summary()


###############################################
if __name__ == '__main__':
    main()