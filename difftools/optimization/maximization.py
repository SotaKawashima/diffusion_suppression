import difftools.diffusion.info as ddi
import difftools.optimization.optimization as doo

import numpy as np

def maximization(seed, k, sample_size, adj, SeedSet_F, prob_map, pop, interest_list, assum_list):
    n = adj.shape[0]
    S = np.zeros((ddi.InfoTypes_n, n), dtype = np.int64)
    S[ddi.InfoType_F] = SeedSet_F

    hist = np.zeros((k, ddi.InfoTypes_n, n), dtype = np.float64)

    for j in range(k):
        s_dist = np.zeros((ddi.InfoTypes_n, n), np.float64)

        for i in range(n):
            if np.sum(S[:, i]) == 0:
                Su = S.copy()
                Su[ddi.InfoType_T][i] = 1
                # print('Su\n', Su)
                dist = doo.infl_prop_exp(seed, sample_size, adj, Su, prob_map, pop, interest_list, assum_list)
                s_dist[ddi.InfoType_F][i] = dist[ddi.InfoType_F].sum()
                s_dist[ddi.InfoType_T][i] = dist[ddi.InfoType_T].sum()
                # print('\ns_dist\n', s_dist)

        S[ddi.InfoType_T][s_dist[ddi.InfoType_T].argmax()] = 1
        print('\ns_dist.argmax()：', s_dist[ddi.InfoType_T].argmax())
        hist[j] = s_dist

    return S, hist