import sys
from pathlib import Path

from numpy.lib.function_base import average
sys.path.append(str(Path('__file__').resolve().parent))

from difftools.diffusion.diffuse import *
from difftools.diffusion.graph import *
from difftools.diffusion.info import *
from difftools.diffusion.user import *
import write_file as wf

import numpy as np
from pandas import DataFrame
import time
from joblib import Parallel, delayed

def sample1():
    n = 50
    seed = 3
    k_F = 5
    k_T = 6
    sample_size = 100
    pop_list = [0, 0]
    pop_list[InfoType_F] = pop_high
    pop_list[InfoType_T] = pop_low

    G = make_random_graph(n, seed)
    # show_graph(G)
    adj = to_np_adjmat(G)
    print('adj\n', adj)

    interest_list = make_interest_list(n, seed)
    # print('\ninterest_list\n', interest_list)

    assum_list = make_assum_list(n, seed)
    # print('\nassum_list\n', assum_list)

    S = np.zeros((InfoTypes_n, n), np.int64)
    S[InfoType_F] = make_SeedSet_F(n, k_F, seed)
    S[InfoType_T] = make_SeedSet_T(S[InfoType_F], k_T, seed+1)
    print('\nS\n', S)

    seq = make_probability()
    prob_map = map_probability(*seq)
    print('\nprob_map\n', prob_map)

    rs_N = sim_diff(adj, sample_size, pop_list, interest_list, assum_list, S, prob_map)

    path_name = wf.set_path('diffusion')
    inputs = {'n': n, 'seed': seed, 'k_F': k_F, 'k_T': k_T, 'sample_size': sample_size, 'pop_list': pop_list, 'prob_map': seq.tolist()}
    wf.write_inputs(path_name, inputs)
    outputs = [[i.tolist() for i in j] for j in rs_N]
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
    k_T = 0
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
            S = np.zeros((InfoTypes_n, n), np.int64)
            S[InfoType_F] = make_SeedSet_F(n, k_F, j)
            # S[InfoType_T] = make_SeedSet_T(S[InfoType_F], k_T, seed+1)
            # print('\nS\n', S)

            rs_N = sim_diff(adj, sample_size, pop_list, interest_list, assum_list, S, prob_map)

            d = np.zeros((ddi.InfoTypes_n, n), np.float64)
            for x in rs_N:
                d += x[0]
            dist = d / sample_size

            df = df.append({
                'n': n,
                'm': len(G.edges()),
                'density': nx.density(G),
                'ASPL': nx.average_shortest_path_length(G),
                'k_F_rand': j,
                'k_F': k_F,
                'k_T': k_T,
                'pop_F': pop_list[InfoType_F],
                'pop_T': pop_list[InfoType_T],
                'infl_sprd_F': dist[0].sum() / n,
                'infl_sprd_T': dist[1].sum() / n
            }, ignore_index = True)

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    print(df)
    path_name = wf.set_path('diffusion_2')
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

def sim_diff(adj, sample_size, pop_list, interest_list, assum_list, S, prob_map):
    n = adj.shape[0]

    rs_N = Parallel(n_jobs=-1)(delayed(adjmat)(adj, S, None, prob_map, pop_list, interest_list, assum_list) for _ in range(sample_size))
    # print('\nrs_N\n', rs_N)

    # testing for influence spreads
    t_ans_m = np.zeros((2, n), np.int64)
    t_ans_m[0] = np.sum([r[0][0] for r in rs_N], axis=0)
    t_ans_m[1] = np.sum([r[0][1] for r in rs_N], axis=0)

    # print()
    # print([f"{p:.2f}" for p in t_ans_m[InfoType_F] / sample_size])
    # print([f"{p:.2f}" for p in t_ans_m[InfoType_T] / sample_size])

    return rs_N

if __name__ == '__main__':
    sample2()