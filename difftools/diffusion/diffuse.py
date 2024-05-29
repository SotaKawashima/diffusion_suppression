import difftools.diffusion.info as ddi

import numpy as np
import numpy.random as nrd

def count_nonzero(current, InfoTypes):
    c = 0
    for it in InfoTypes:
        c += np.count_nonzero(current[it])
    return c

def adjmat(adj, SeedSet, seed, prob_map, pop_list, interest_list, assum_list):
    n = adj.shape[0]

    InfoTypes = ddi.make_InfoTypes()

    if not seed is None:
        nrd.seed(seed)

    # The pair of active node groups (currently activated)
    current = SeedSet.copy()

    # The pair of total active node groups (activated)
    total = current.copy()

    # history
    hist = [(current.copy(), total.copy())]

    while count_nonzero(current, InfoTypes) > 0:
        # init new active groups
        J = np.zeros((ddi.InfoTypes_n, n), np.int64)

        # iterate user i from a current active group
        for i in range(n):
            # make the sequence of received information
            rs = np.zeros(0, dtype = np.int64)
            for it in InfoTypes:
                if current[it][i] == 1:
                    rs = np.append(rs, it)

            rs = np.unique(rs) # remove duplicates
            rs_n = len(rs)

            if rs_n != 1: # If not received, or if two pieces of information are received, do nothing
                continue
            else:
                info = rs[0]
                pop = pop_list[info]
                interest = interest_list[i][pop]
                assum = assum_list[i][info]
                p = prob_map[pop][info][interest][assum]

                for j in range(n):
                    # j should be a successor of i and not active
                    # note: a_ij = 0 if and only if an edge (i, j) does not exist in a graph
                    if adj[i, j] == 0 or np.sum(total[:, j]) > 0 or np.sum(J[:, j]) > 0:
                        continue

                    # j should not be activated if p = 0, and j should be activated if p = 1
                    if p == 1 or p > nrd.random():
                        # activate j with a probability
                        J[info][j] = 1

        # replace old active groups to new ones
        current = J.copy() #.astype(np.int64)
        # add new active nodes to the total group
        # note: for all j, the proposition J_j = 1 & total_j = 0 holds, so every component of total + J is at most 1
        total += J

        hist.append((current.copy(), total.copy()))

    hist_n = len(hist)
    Cs = np.zeros((ddi.InfoTypes_n, hist_n, n), dtype = np.int64)
    Ts = np.zeros((ddi.InfoTypes_n, hist_n, n), dtype = np.int64)

    for it in InfoTypes:
        for i, h in enumerate(hist):
            Cs[it][i] = h[0][it]
            Ts[it][i] = h[1][it]

    return total, Cs, Ts