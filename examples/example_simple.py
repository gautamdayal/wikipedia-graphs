# Code for a simple example

# Instead of taking command line input for this example, we supply values within the code itself
source = "Music"
breadth = 5
depth = 5

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

# Saving the figure to an output directory
plt.savefig("../output/sample.png")
