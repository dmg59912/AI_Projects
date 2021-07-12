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



    def get_vertex(self,node):
        pass

    def add_edge(self, from_edge, to_edge, weight):
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)

        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)

        self.vert_dict[from_edge].add_neighbour(self.vert_dict[to_edge], weight)
        pass

    def get_vertices(self):
        return self.vert_dict.keys()

    def graph_summary():
        pass


class Vertex:

    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def get_connections(self):
        pass

    def add_neighbour(self, obj_neighbour, weight):
        self.adjacent[obj_neighbour] = weight

    def get_id(self):
        pass

    def get_weight(self, neigjbour):
        pass

#########################################################################################
def main():
    print("Setting up basic graph")


###############################################
if __name__ == '__main__':
    main()