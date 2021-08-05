# Rios Rios 
# ID 006666515
# CECS 451 Assignment 3

import csv
min_infinity = -1000000
max_infinity = 1000000
###################################################################################################################
####################################  CLASS TREE         ##########################################################
class Tree(object):
    def __init__(self):
        self.node_dict = {}
        self.num_node = 0
        self.root = None
        self.depth = 0

    def add_node(self, node_id, node_value, parent_id):
        # if node is the root, then root has no parent else add node with given parent
        if self.num_node == 0:
            parent = None
            new_v = Node(node_id, node_value, parent)
            self.root = new_v
        else:
            parent = self.node_dict[parent_id]
            new_v = Node(node_id, node_value, parent)
            parent.add_child(node_id, new_v)

        self.node_dict[node_id] = new_v
        self.num_node += 1

    #print current tree
    def print_tree_no_p(self):
        for node in self.get_nodes():
            nd = self.node_dict[node]
            print(nd.get_id(), '[', nd.get_value(),']')

    def print_tree_pruning(self):
        for node in self.get_nodes():
            nd = self.node_dict[node]
            print(nd.get_id(), '[', nd.get_value(),']',nd.pruned)


    def get_node(self, node_id):
        if node_id in self.node_dict:
            return self.node_dict[node_id]
        else:
            return None

    def get_nodes(self):
        return self.node_dict.keys()

    # use depth search to find the actual depth of our tree
    def depth_util(self, root):

        for item in root.get_children_nodes():
            node = self.node_dict[item]
            self.depth += 1
            self.depth_util(node)
            return

    def get_depth(self):
        self.depth_util(self.root)
        return self.depth

    # use minmax algo with pruning 
    def minimax_prune(self, current_node, depth):
        # start with max first
            current_node.pruned = False
            self.max_value_prune(current_node, min_infinity, max_infinity, depth)
 

    def max_value_no_pruning(self, current_node, depth):
        if depth == 0:
            return current_node.get_value()

        max_value = min_infinity

        # at each level we want to find the max 
        for child in current_node.get_children_nodes():
            child_node = self.node_dict[child]

      
            max_value = max(max_value, self.min_value_no_pruning(child_node, depth - 1))
            current_node.value = max_value
        return max_value

    def min_value_no_pruning(self, current_node, depth):
        if depth == 0:
            return current_node.get_value()

        min_value = max_infinity

        # at eac level we want to find min values 
        for child in current_node.get_children_nodes():
            child_node = self.node_dict[child]

            min_value = min(min_value, self.max_value_no_pruning(child_node, depth - 1))
            current_node.value = min_value

        # print("Node: ", current_node.get_id(), "[", current_node.get_value(), "]")
        return min_value
    # prune version of the max and min value functions
    def max_value_prune(self, current_node, infinity, neg_infinity, depth):

        if depth == 0:
            return current_node.get_value()

        for child in current_node.get_children_nodes():
            child_node = current_node.child_dict[child]
            child_node.pruned = False

            infinity = max(infinity, self.min_value_prune(child_node, infinity, neg_infinity, depth - 1))
            current_node.value = infinity
            current_node.alpha = infinity
            current_node.beta = neg_infinity

            if neg_infinity <= infinity:  
                return infinity
        return infinity

    def min_value_prune(self, current_node, infinity, neg_infinity, depth):
        if depth == 0:
            return current_node.get_value()

        for child in current_node.get_children_nodes():
            child_node = current_node.child_dict[child]
            child_node.pruned = False

            neg_infinity = min(neg_infinity, self.max_value_prune(child_node, infinity, neg_infinity, depth - 1))
            current_node.value = neg_infinity
            current_node.alpha = infinity
            current_node.beta = neg_infinity

            if neg_infinity <= infinity:
                return neg_infinity

        return neg_infinity

#################################################################################################
################################# CLASS NODE     ################################################
class Node:
    def __init__(self, node_id, node_value, parent):
        self.id = node_id
        self.parent = parent
        #need to cast to float or else will think is a string 
        self.value = float(node_value)
        # marked or prune True if prune, False if not
        self.pruned = True 
        self.visited = False 
        self.child_dict = {}  


    def add_child(self, child_id, child_node):
        self.child_dict[child_id] = child_node

    def get_children_nodes(self):
        return self.child_dict.keys()

    def get_parent(self):
        return self.parent

    def get_value(self):
        return self.value

    def get_id(self):
        return self.id


    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////// Main.////////////////////////////////////////////////////////////////////////
def main():
    print("Setting up MinMax tree pruning")
    min_max_tree = Tree()



    # going to use columns 1 and 2 to extract data, we are not worried abt col 0 = min/max for now 
    col_1 = 1
    col_2 = 2
    
    ############ remove # from file to select which to run 
    #file = "tree2.txt"
    file = "tree1.txt"
    ##########################################################
    with open(file, 'r') as csvfile:
        cvsreader = csv.reader(csvfile,delimiter=',')
        count = 0
        for row in cvsreader:
            #if count 0 the we are in line 1 and so we need to extract and set our root node
            if count == 0:  
                #need to remove excess white space and then find our '=' and store the value next to the '=' sign
                parse_space = row[col_2].replace(" ", "")  
                root = parse_space[0:parse_space.find("=")]  
                root_value = parse_space[parse_space.find("=") + 1: len(parse_space)] 

                min_max_tree.add_node(root, root_value, " ")
            # need to get the rest of the data after we get our root 
            else: 
                parent = row[col_1].replace(" ", "")

                for col in range(2, len(row)):
                    #need to remove excess white space and then find our '=' and store the value next to the '=' sign
                    parse_space = row[col].replace(" ", "")
                    child = parse_space[0:parse_space.find("=")]
                    child_value = parse_space[parse_space.find("=") + 1: len(row[col])]

                    # add values to the tree
                    min_max_tree.add_node(child, child_value, parent)

            count += 1

    depth = min_max_tree.get_depth()
    root_node = min_max_tree.root
   
   #printing min_max with no prune 
    print("MinMax all node values without pruning")
    min_max_tree.max_value_no_pruning(root_node,depth)
    min_max_tree.print_tree_no_p()

    print()

    #printing min_max with pruning 
    print("MinMax with prune nodes")
    min_max_tree.minimax_prune(root_node,depth)
    min_max_tree.print_tree_pruning()
  

#####################################################################################################################
################################################################################################################
if __name__ == '__main__':
    main()


