import matplotlib.pyplot as plt
import networkx as nx
import sys
import json
import csv
import numpy as np

path = sys.argv[1]
G = nx.read_edgelist(path + '/graph.edgelist', create_using = nx.DiGraph)
colors = ['gray' for _ in list(G)]

if path[-9:] == 'diffusion':
    with open(path + '/outputs.json') as f:
        result = json.load(f)
    # print('result', result[0][0])

    for i, x in enumerate(result[0][0][0]):
        if x == 1:
            colors[i] = 'lightblue'
    for i, x in enumerate(result[0][0][1]):
        if x == 1:
            colors[i] = 'pink'
    # print('color', colors)

with open(path + '/seed_set.csv') as f:
    reader = csv.reader(f)
    l_2d = [row for row in reader]
arr_t = np.array(l_2d[1:]).T.astype(int)
# print('arr_t', arr_t)

for i, x in enumerate(arr_t[0]):
    if x == 1:
        colors[i] = 'blue'
for i, x in enumerate(arr_t[1]):
    if x == 1:
        colors[i] = 'red'
# print('colors', colors)

# print(list(G))

nx.draw_networkx(G, node_color = [colors[int(i)] for i in list(G)])
plt.show()