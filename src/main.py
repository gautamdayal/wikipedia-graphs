# Code for main control flow

import sys
import Searcher
import networkx as nx
import matplotlib.pyplot as plt

"""
for command line argument, argv[0] is the start page on Wikipedia,
argv[1] is the destination page, argv[2] is the given depth (>1)
"""
if len(sys.argv) != 4:
    print("invalid arguments: argv[0] is the start page on Wikipedia, argv[1] is the destination page, argv[2] is the given depth (>1)")
    sys.exit(-1)

source = sys.argv[1]
breadth = int(sys.argv[2])
depth = int(sys.argv[3])

# print(Searcher.Searcher().search(source, breadth, depth))
searcher = Searcher.Searcher()
edges = searcher.search(source, breadth, depth)
if len(edges)== 0:
    print("page not found by library")
    quit(1)
wiki_graph = nx.Graph()
for source in edges:
    for dest in edges[source]:
        wiki_graph.add_edge(source, dest)
nx.draw(wiki_graph, with_labels = True, )

plt.savefig("../output/sample.png")
