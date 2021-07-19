

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

#######################################################################################
#############################################

def main():
    print("Setting up basic maze")

    #setting up graph and files 
    
    file_to_open = "smallMaze.lay"
    graph = Graph()

    #reading in a loop
    f = open(file_to_open,"r")

    for x in f:
        print(x,end='')
    f.close()

    print('\n\n')
    #get the lenght of the data 
    f = open(file_to_open,"r")
    data = f.read()
    len_char = len(data)
    print(len_char)
    f.close()

    print('\n\n')

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

    print("\n\n")
    print(len(game_board))
    print(len(game_board[0]))
    print(game_board)

    new_b = game_board
    count = 0

    #set up a flag for start and goal to add to our graph
    goal = -2
    start = -1

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
                


            print(game_board[i][j], ' ', end ="")
        print()

    print(graph.get_vertices())
     # printing board 
     # 8, 1
   
    print('\n\n',count)
 
    # setting up travel directions the matrix board 
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

    graph.graph_summary()
           
        
            
  


###############################################
if __name__ == '__main__':
    main()