#----------------------------------------------------------------------------------------
#	Simulate DFS algorithm.
#   This version  of DFS, travers a graph in DFS order in recursive
#				 
#	(c) 2020 Arjang Fahim
#
#   
#	Date: 4/10/2020
#	email: fahim.arjang@csulb.edu
#   version: 1.0.0
#----------------------------------------------------------------------------------------

class DFSNodeColor(object):
	
    def __init__(self, graph, size):

        self.graph = graph
        self.size = size
        self.start_node = self.graph.most_visited_node().get_id()

        self.colors = self.graph.get_color_list()
        

    # going to expand from the DFSRec to 'color' our map
    def DFS_util(self, s):
        s.set_visited(True)
        
        if len(s.get_colors()) != 0 :
            s.set_color(s.get_colors()[0])
            for vertex in s.adjacent:
                node = self.graph.get_vertex(vertex.get_id())

                # will remove item until there is 1 left
                if len(node.get_colors())> 1:
                    node.get_colors().remove(s.get_colors()[0])
        else:
            print("Arc consistency fail at", s.get_id())
            exit()
            
        print(s.get_id(), "-->", self.colors[s.get_color()])


        # going to keep this part from DFSRec to recursively call function 
        node = self.graph.get_vertex(s.get_id())
        for v in node.adjacent:
            n = self.graph.get_vertex(v.get_id())
            if n.get_visited() == False:
                self.DFS_util(n)

    def DFS_recursive(self):
        s_node = self.graph.get_vertex(self.start_node)
        self.DFS_util(s_node)



   
#------------------------[End of DFS class]----------------------------------------------------------------