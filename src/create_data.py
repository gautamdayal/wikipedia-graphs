from classes import *

node_0 = WikiPage('/wiki/Kerbal_Space_Program', 'Kerbal Space Program')
# print(node_0.make_csv())

# def createSubgraph(root, breadth, depth):
#     out_file = open(f"../data/{root.title}_{breadth}_{depth}", 'w')
#     out_dict = {}
#
#     out_file.close()

print(node_0.crawl(only_link=True))
