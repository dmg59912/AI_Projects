
from Graph.Graph import Graph
from pathlib import Path
from SearchAlgorithms.DFSRec import DFSRec

# Converting maze to graph

output_folder = Path("Output/")
data_folder = Path("Data/TextData/")


data = data_folder / "map.txt"

g = Graph(data)
g.graph_build()
size = g.graph_length()

g.graph_summary()

dfs = DFSRec(g, size, 2)
dfs.DFS_recursive()
