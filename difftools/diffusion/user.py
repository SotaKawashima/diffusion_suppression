from .info import *

import numpy as np
import numpy.random as nrd

interest_low = 0
interest_high = 1
intersts_n = 2

assum_F = 0
assum_T = 1
assums_n = 2

def make_interest_list(n, seed):
    if not seed is None:
        nrd.seed(seed)
    interest_list = np.zeros((n, InfoTypes_n), dtype = np.int64)
    for i in range(n):
        interest_list[i][InfoType_F] = nrd.randint(2)
        interest_list[i][InfoType_T] = nrd.randint(2)

    return interest_list

def make_assum_list(n, seed):
    if not seed is None:
        nrd.seed(seed)
    assum_list = np.zeros((n, InfoTypes_n), dtype = np.int64)
    for i in range(n):
        assum_list[i][pop_low] = nrd.randint(2)
        assum_list[i][pop_high] = nrd.randint(2)

    return assum_list

def map_probability(
    prob_1011, prob_1111, prob_0011, prob_0111,
    prob_1001, prob_1101, prob_0001, prob_0101,
    prob_1000, prob_1100, prob_0000, prob_0100,
    prob_1010, prob_1110, prob_0010, prob_0110
    ):
    a = np.zeros((pops_n, InfoTypes_n, intersts_n, assums_n), dtype = np.float64)
    a[pop_low][InfoType_F][interest_low][assum_F] = prob_0000
    a[pop_low][InfoType_F][interest_low][assum_T] = prob_0001
    a[pop_low][InfoType_F][interest_high][assum_F] = prob_0010
    a[pop_low][InfoType_F][interest_high][assum_T] = prob_0011
    a[pop_low][InfoType_T][interest_low][assum_F] = prob_0100
    a[pop_low][InfoType_T][interest_low][assum_T] = prob_0101
    a[pop_low][InfoType_T][interest_high][assum_F] = prob_0110
    a[pop_low][InfoType_T][interest_high][assum_T] = prob_0111
    a[pop_high][InfoType_F][interest_low][assum_F] = prob_1000
    a[pop_high][InfoType_F][interest_low][assum_T] = prob_1001
    a[pop_high][InfoType_F][interest_high][assum_F] = prob_1010
    a[pop_high][InfoType_F][interest_high][assum_T] = prob_1011
    a[pop_high][InfoType_T][interest_low][assum_F] = prob_1100
    a[pop_high][InfoType_T][interest_low][assum_T] = prob_1101
    a[pop_high][InfoType_T][interest_high][assum_F] = prob_1110
    a[pop_high][InfoType_T][interest_high][assum_T] = prob_1111

    return a

def make_probability():
    x = np.arange(1, 17)/16
    a = np.power(10, -x)

    return a