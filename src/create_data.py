from classes import *

node_0 = WikiPage('/wiki/Doctor_Who', 'Doctor Who')
# print(node_0.make_csv())

def createSubgraphData(root, breadth, depth):
    out_file = open(f"../data/{root.title}_{breadth}_{depth}", 'w')
    out_dict = {}

    out_file.close()
