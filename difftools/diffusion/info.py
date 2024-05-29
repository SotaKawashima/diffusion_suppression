import numpy as np
import numpy.random as nrd

pop_low = 0
pop_high = 1
pops_n = 2

InfoType_F = 0
InfoType_T = 1
InfoTypes_n = 2

def make_Info(pop):
    a = np.zeros((InfoTypes_n, pops_n), dtype = np.int64)
    for it in [InfoType_F, InfoType_T]:
        a[it] = [it, pop]

    return a
    
def make_InfoTypes():
    a = np.zeros(InfoTypes_n, dtype = np.int64)
    for it in [InfoType_F, InfoType_T]:
        a[it] = it

    return a

def make_SeedSet_F(n, k, seed):
    if not seed is None:
        nrd.seed(seed)
    S = np.zeros(n, dtype = np.int64)
    seed_index = nrd.permutation(n)[:k]
    S[seed_index] = 1

    return S

def make_SeedSet_T(SeedSet_F, k, seed):
    if not seed is None:
        nrd.seed(seed)
    n = len(SeedSet_F) - np.count_nonzero(SeedSet_F)
    S = np.zeros(n, dtype = np.int64)
    seed_index = nrd.permutation(n)[:k]
    S[seed_index] = 1
    for i in [i for i, x in enumerate(SeedSet_F) if x == 1]:
        S = np.insert(S, i, 0)
    S

    return S