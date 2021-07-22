import collections
from os import path
import queue


#global flags to set our start and goal position on our game board 
goal = -2
start = -1

###################################################################################################
################# Graph and vertex classes
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
    def get_vertex(self,n):
        if n not in self.vert_dict:
            print(n, "not in graph")
        else:
            return self.vert_dict[n]

    def add_edge(self, from_edge, to_edge, weight):
        if from_edge not in self.vert_dict:
            self.add_vertex(from_edge)

        if to_edge not in self.vert_dict:
            self.add_vertex(to_edge)

        self.vert_dict[from_edge].add_neighbour(self.vert_dict[to_edge], weight)
      

    def get_vertices(self):
        return self.vert_dict.keys()

    def num_vert(self):
        return self.num_vertices

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




#######################################################################################
############################## BFS algo ##########################################
class BFS(object):
    def __init__(self, graph):
        self.graph = graph
        self.path = []
        self.possible_paths = []


    def bfs_util(self, start, goal, visited, add_path):

        #initial state, our visited initial state wil be marked as true
        visited[start] = True
        self.path.append(start)

        # if current path is the same same our goal
        if start == goal:
            add_path.append(self.path.copy())
        else:
            vertexes = self.graph.get_vertex(start)
            for x in vertexes.adjacent:
                if visited[x.id] == False:
                    self.bfs_util(x.id,goal,visited,add_path)
        
        # remove current vertex from path and marked it as unvisited 
        self.path.pop()
        visited[start] = False
        return add_path
   
    def BFS_paths(self,start,goal):
        self.add_path = []
        visited = [False] * (self.graph.num_vert() + 1)
        self.add_path = self.bfs_util(start,goal,visited,self.add_path)
        return  self.add_path

########################################################################################

def DFS_util(self, root):
    for node_item in root.children_list:
        if node_item.visited == False:
            self.DFS_util(node_item)
            node_item.visited = True

    print(root.get_id())
    return

def DFS_traversal(self):
        self.DFS_util(self.root)

##############################################################################################
########################## main #######################################
def main():
    print("Setting up basic maze")

    #setting up graph and files 
    
    #file_to_open = "bigMaze.lay"
    file_to_open = "mediumMaze.lay"
    #file_to_open = "smallMaze.lay"
    
    graph = Graph()


    #adding to a file to matrix chars
    game_board = []
    f = open(file_to_open,"r")
    line = f.readline()
    while line:
        col = []
        for x in line:
            print(x,end='')
            if x != '\n':
                col.append(x)
        line = f.readline() 
        game_board.append(col)


    new_b = game_board
    # count will increment to set vertex values if there is an open space 
    count = 0

 
    # Addinng nodes to our graph
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            #print(i,j, '  ', end='')
            if(game_board[i][j] == ' '):
                count = count + 1
                new_b[i][j] = count
                graph.add_vertex(count)
            elif(game_board[i][j] == 'P'):
                count = count +1
                new_b[i][j] = goal
                graph.add_vertex(goal)
            elif(game_board[i][j] == '.'):
                count = count + 1
                new_b[i][j] = start
                graph.add_vertex(start)
                

    #print(graph.get_vertices())
     # printing board 
  
    print('\n\n','Total vertecies',count)
 
    # setting up travel directions to travel on our matrix board 
    move_up = -1
    move_right = 1
    move_down = 1
    move_left = -1

    # seeting flags to check if we are outside of the matrix boundry
    right_boundary = len(game_board[0])
    left_boundary = -1
    top_boundary = -1
    botton_boundary = len(game_board)


    #now adding connections between our verticies 
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            # check that we are not outside right boundary if not, then add connection to node if any
            if( j + move_right) != right_boundary:
               if game_board[i][j] != '%':
                    if(game_board[i][j + move_right] != '%'):
                        graph.add_edge(game_board[i][j], game_board[i][j + move_right], 1)

            # check that we are not outside botton boundary, if not add connection to node if any 
            if(i + move_down) != botton_boundary:
               if game_board[i][j] != '%':
                    if(game_board[i + move_down][j] != '%'):
                        graph.add_edge(game_board[i][j], game_board[i + move_down][j], 1)
            # check that we are not outside our left boundary, if not add connection to node if any
            if(j + move_left != left_boundary):
               if game_board[i][j] != '%':
                    if(game_board[i][j + move_left] != '%'):
                        graph.add_edge(game_board[i][j], game_board[i][j + move_left], 1)

            # check that we are not outside our top boundary, if not add connection to node if any
            if(i + move_up != top_boundary):
                if game_board[i][j] != '%':
                    if(game_board[i + move_up][j] != '%'):
                        graph.add_edge(game_board[i][j], game_board[i + move_up][j], 1)
            #print(i,j)
            #check top and top left  boundaries are in range

   


    bfs = BFS(graph)
    shortes = bfs.BFS_paths(start,goal)

    # need to find the shortes path from the list of paths found 

    path_count = 0
    #give flag value for our current path to conpare and set the path with the lowest travel distance per say
    current_path = 10000000
    shortes_path_index = 0
    for i in range(len(shortes)):
        for j in range(len(shortes[i])):
            path_count += 1
        if current_path > path_count:
            current_path = path_count - 1
            shortes_path_index = i
        path_count = 0



       
           
        
    # map our shortes path with '.' 
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            for k in shortes[shortes_path_index]:
                if game_board[i][j] == k:
                    game_board[i][j] = '.'
                elif game_board[i][j] == goal:
                    game_board[i][j] = 'P'

    # remove vertex ids on our map and set it to only show current shortes path 
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if (game_board [i][j] != '%') and ((game_board[i][j] != '.') and (game_board[i][j] != 'P') ):
                game_board[i][j] = ' '
            print(game_board[i][j], end ="")
        print()
    
    print('Shortes path cost',current_path)

       
           
        
            
  


###############################################
if __name__ == '__main__':
    main()