import json
import csv
import os
import datetime
import networkx as nx

def set_path(name):
    jst_now = datetime.datetime.utcnow() + datetime.timedelta(hours = +9)
    jst_now_str = datetime.datetime.strftime(jst_now, '%Y-%m-%d_%H:%M:%S')
    path_name = 'results/' + jst_now_str + '_' + name
    os.makedirs(path_name)

    return path_name

def write_inputs(path_name, inputs):
    with open(path_name + '/inputs.json', 'w') as f:
        json.dump(inputs, f, indent = 4)

def write_outputs(path_name, outputs):
    with open(path_name + '/outputs.json', 'w') as f:
        json.dump(outputs, f, indent = 4)

# def write_adj(path_name, adj):
#     with open(path_name + '/adj.csv', 'w') as f:
#         writer = csv.writer(f)
#         writer.writerows(adj)

def write_graph(path_name, G):
    nx.write_edgelist(G, path_name + "/graph.edgelist")

def write_interest(path_name, interest):
    with open(path_name + '/interest.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['low', 'high'])
        writer.writerows(interest)

def write_assum(path_name, assum):
    with open(path_name + '/assum.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['F', 'T'])
        writer.writerows(assum)

def write_SeedSet(path_name, seed_set):
    with open(path_name + '/seed_set.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['F', 'T'])
        writer.writerows(seed_set)

def write_SeedSet_index(path_name, S_list):
    S_list_index = []
    for S in S_list:
        S_list_index.append(
            {
                "F": [i for i, x in enumerate(S[0]) if x == 1],
                "T": [i for i, x in enumerate(S[1]) if x == 1]
            }
        )
    with open(path_name + '/seed_set_index.json', 'w') as f:
        json.dump(S_list_index, f, indent = 4)