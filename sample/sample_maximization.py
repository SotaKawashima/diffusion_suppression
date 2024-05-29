import sys
from pathlib import Path
sys.path.append(str(Path('__file__').resolve().parent))

from difftools.diffusion.diffuse import *
from difftools.diffusion.graph import *
from difftools.diffusion.user import *
from difftools.optimization.maximization import *
import write_file as wf

from pandas import DataFrame
import networkx as nx
import time

def sample1():
    n = 50
    seed = 1
    k_F = 5
    k_T = 10
    sample_size = 100
    pop_list = [0, 0]
    pop_list[InfoType_F] = pop_high
    pop_list[InfoType_T] = pop_high

    G = make_random_graph(n, seed)
    # show_graph(G)
    adj = to_np_adjmat(G)
    print('adj\n', adj)

    SeedSet_F = make_SeedSet_F(n, k_F, seed)
    print('\nSeedSet_F\n', SeedSet_F)

    interest_list = make_interest_list(n, seed)
    # print('\ninterest_list\n', interest_list)

    assum_list = make_assum_list(n, seed)
    # print('\nassum_list\n', assum_list)

    seq = make_probability()
    prob_map = map_probability(*seq)
    print('\nprob_map\n', prob_map)

    S, hist = sim_max(adj, sample_size, pop_list, interest_list, assum_list, SeedSet_F, k_T, prob_map)

    path_name = wf.set_path('maximization')
    inputs = {'n': n, 'seed': seed, 'k_F': k_F, 'k_T': k_T, 'sample_size': sample_size, 'pop_list': pop_list, 'prob_map': seq.tolist()}
    wf.write_inputs(path_name, inputs)
    outputs = hist.tolist()
    wf.write_outputs(path_name, outputs)
    # wf.write_adj(path_name, adj)
    wf.write_graph(path_name, G)
    wf.write_interest(path_name, interest_list)
    wf.write_assum(path_name, assum_list)
    wf.write_SeedSet(path_name, S.T)

def sample2():
    n = 100
    G_seed = 0
    seed = 0
    k_F_seeds = [10, 22, 38, 48, 53, 60, 77, 78, 81, 83]
    k_F = 2
    k_T = 5
    sample_size = 100

    pop_combo = [
        [pop_high, pop_high],
        [pop_high, pop_low],
        [pop_low, pop_high],
        [pop_low, pop_low]
    ]

    G = make_random_graph(n, G_seed)
    # show_graph(G)
    adj = to_np_adjmat(G)
    # print('adj\n', adj)

    interest_list = make_interest_list(n, seed)
    # print('\ninterest_list\n', interest_list)

    assum_list = make_assum_list(n, seed)
    # print('\nassum_list\n', assum_list)

    seq = make_probability()
    prob_map = map_probability(*seq)
    # print('\nprob_map\n', prob_map)

    df = DataFrame()
    start = time.time()
    for j in k_F_seeds:
        for pop_list in pop_combo:
            SeedSet_F = make_SeedSet_F(n, k_F, j)
            # print('\nSeedSet_F\n', SeedSet_F)

            S, hist = sim_max(adj, sample_size, pop_list, interest_list, assum_list, SeedSet_F, k_T, prob_map)

            for i, x in enumerate(hist):
                df = df.append({
                    'n': n,
                    'm': len(G.edges()),
                    'density': nx.density(G),
                    'ASPL': nx.average_shortest_path_length(G),
                    'k_F_rand': j,
                    'k_F': k_F,
                    'k_T': i + 1,
                    'pop_F': pop_list[InfoType_F],
                    'pop_T': pop_list[InfoType_T],
                    'infl_sprd_F': x[InfoType_F][x[InfoType_T].argmax()] / n,
                    'infl_sprd_T': x[InfoType_T].max() / n
                }, ignore_index = True)

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    print(df)
    path_name = wf.set_path('maximization_2')
    df.to_csv(path_name + '/result.csv')
    inputs = {'n': n, 'G_seed': G_seed, 'seed': seed, 'k_F_seeds': k_F_seeds, 'k_F': k_F, 'k_T': k_T, 'sample_size': sample_size, 'pop_list': pop_list, 'prob_map': seq.tolist()}
    wf.write_inputs(path_name, inputs)
    outputs = {'elapsed_time': "{0}".format(elapsed_time) + "[sec]"}
    wf.write_outputs(path_name, outputs)
    # wf.write_adj(path_name, adj)
    wf.write_graph(path_name, G)
    wf.write_interest(path_name, interest_list)
    wf.write_assum(path_name, assum_list)
    # wf.write_SeedSet(path_name, S.T)

def sample3():
    n = 100
    G_seed = 0
    seed = 0
    k_F_seeds = [10, 22, 38, 48, 53, 60, 77, 78, 81, 83]
    k_F = 2
    k_T = 5
    sample_size = 1000

    pop_combo = [
        [pop_high, pop_high],
        # [pop_high, pop_low],
        # [pop_low, pop_high],
        [pop_low, pop_low]
    ]

    G = make_random_graph(n, G_seed)
    # show_graph(G)
    adj = to_np_adjmat(G)
    # print('adj\n', adj)

    interest_list = make_interest_list(n, seed)
    # print('\ninterest_list\n', interest_list)

    assum_list = make_assum_list(n, seed)
    # print('\nassum_list\n', assum_list)

    seq = make_probability()
    prob_map = map_probability(*seq)
    # print('\nprob_map\n', prob_map)

    S_list = []
    df = DataFrame()
    start = time.time()
    for j in k_F_seeds:
        for pop_list in pop_combo:
            SeedSet_F = make_SeedSet_F(n, k_F, j)
            # print('\nSeedSet_F\n', SeedSet_F)

            S, hist = sim_max(adj, sample_size, pop_list, interest_list, assum_list, SeedSet_F, k_T, prob_map)
            S_list.append(S)

            for i, x in enumerate(hist):
                df = df.append({
                    'n': n,
                    'm': len(G.edges()),
                    'density': nx.density(G),
                    'ASPL': nx.average_shortest_path_length(G),
                    'k_F_rand': j,
                    'k_F': k_F,
                    'k_T': i + 1,
                    'pop_F': pop_list[InfoType_F],
                    'pop_T': pop_list[InfoType_T],
                    'infl_sprd_F': x[InfoType_F][x[InfoType_T].argmax()] / n,
                    'infl_sprd_T': x[InfoType_T].max() / n
                }, ignore_index = True)

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    print(df)
    path_name = wf.set_path('maximization_3')
    df.to_csv(path_name + '/result.csv')
    inputs = {'n': n, 'G_seed': G_seed, 'seed': seed, 'k_F_seeds': k_F_seeds, 'k_F': k_F, 'k_T': k_T, 'sample_size': sample_size, 'pop_combo': pop_combo, 'prob_map': seq.tolist()}
    wf.write_inputs(path_name, inputs)
    outputs = {'elapsed_time': "{0}".format(elapsed_time) + "[sec]"}
    wf.write_outputs(path_name, outputs)
    wf.write_graph(path_name, G)
    wf.write_interest(path_name, interest_list)
    wf.write_assum(path_name, assum_list)
    wf.write_SeedSet_index(path_name, S_list)

def sim_max(adj, sample_size, pop_list, interest_list, assum_list, SeedSet_F, k_T, prob_map):
    S, hist = maximization(None, k_T, sample_size, adj, SeedSet_F, prob_map, pop_list, interest_list, assum_list)
    print('\nS\n', S)
    # print('\nhist\n', hist)

    return S, hist

if __name__ == '__main__':
    # sample2()
    sample3()