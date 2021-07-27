# Rios Rios 
# ID 006666515
# CECS 451 Assignment 3


###################################################################################################################
####################################  CLASS TREE         ##########################################################
class Tree(object):
    def __init__(self):
        self.node_dict = {}
        self.num_node = 0
        self.root = None

    def add_node(self, node_id,parent_id):
        # if node is the root, then root has no parent else add node with given parent
        if len(parent_id) == 0:
            parent = None
            new_node = Node(node_id, parent)
            self.root = new_node
        else:
            parent = self.node_dict[parent_id]
            new_node = Node(node_id,parent)
            parent.add_child(node_id, new_node)

        self.node_dict[node_id] = new_node
        self.num_node += 1

    def get_node(self, node_id):
        if node_id in self.node_dict:
            return self.node_dict[node_id]


    def get_nodes(self):
        return self.node_dict.keys()

    def DFS_util(self, root):
        for node_item in root.children_list:
            if node_item.visited == False:
                self.DFS_util(node_item)
                node_item.visited = True

        print(root.get_id())
        return
    
    def DFS_traversal(self):
        self.DFS_util(self.root)

#################################################################################################
################################# CLASS NODE     ################################################
class Node:
    def __init__(self,id, parent_node):
        self.id = id
        self.parent_node = parent_node
        self.visited = False
        self.children_list = []

    def add_child(self, child_id, child_node):
        if child_id not in self.children_list:
            self.children_list.append(child_node)

    def get_children_node(self):
        return self.children_list

    def get_id(self):
        return self.id

    def get_parent(self):
        return self.parent_node

###################################################################################################
########################################   MAIN ####################################################
def main():
    print("Setting up basic maze")

	# adding nodes to tree first inserting children then parent 
	tree = Tree()
	tree.add_node('X','')
	tree.add_node('Q','X')
	tree.add_node('F','X')
	tree.add_node('D','X')
	tree.add_node('C','Q')
	tree.add_node('N','Q')
	tree.add_node('R','Q')
	tree.add_node('S','F')
	tree.add_node('M','F')
	tree.add_node('L','M')
	tree.add_node('H','D')

	tree.DFS_traversal()


###############################################
if __name__ == '__main__':
    main()
