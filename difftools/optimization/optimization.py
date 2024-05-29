import difftools.diffusion.info as ddi
import difftools.diffusion.diffuse as ddd

import numpy as np
import numpy.random as nrd
from joblib import Parallel, delayed

def infl_prop_exp(seed, sample_size, adj, Seed_set, prob_map, pop, interest_list, assum_list):
    n = adj.shape[0]
    d = np.zeros((ddi.InfoTypes_n, n), np.float64)
    if not seed is None:
        nrd.seed(seed)
    rs_N = Parallel(n_jobs=-1)(delayed(ddd.adjmat)(adj, Seed_set, seed, prob_map, pop, interest_list, assum_list) for _ in range(sample_size))
    dist = sum([x[0] for x in rs_N]) / sample_size
    
    return dist