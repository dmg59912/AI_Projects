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
	
    def __init__(self, graph, size, start_node):

        self.graph = graph
        self.size = size
        self.start_node = start_node
        

    def DFS_util(self, s):
        
        s.set_visited(True)
        print (s.get_id())
        node = self.graph.get_vertex(s.get_id())
        for v in node.adjacent:
            n = self.graph.get_vertex(v.get_id())
            if n.get_visited() == False:
                self.DFS_util(n)

    def DFS_recursive(self):
        s_node = self.graph.get_vertex(self.start_node)
        self.DFS_util(s_node)



   
#------------------------[End of DFS class]----------------------------------------------------------------