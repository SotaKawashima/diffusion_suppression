import networkx as nx
import matplotlib.pyplot as plt

def main():
    n = 10
    seed = 0
    G = make_random_graph(n, seed)
    calculate_features(G)
    to_np_adjmat(G)
    show_graph(G)

def make_random_graph(n, seed):
    G = nx.scale_free_graph(n, seed = seed).reverse() # n個の頂点からなるスケールフリーの有向グラフ(MultiDiGraph)
    G.remove_edges_from(nx.selfloop_edges(G))   # 自己ループ削除
    H = nx.DiGraph(G)   # 多重辺削除

    return H

def to_np_adjmat(G):
    np_adjmat = nx.to_numpy_array(G)
    # print(np_adjmat)

    return np_adjmat

def calculate_features(G):
    print('平均最短経路長', nx.average_shortest_path_length(G))
    # print('クラスター係数', nx.average_clustering(G))
    print('密度', nx.density(G))
    # bins = range(1,12)
    # plt.hist([x[1] for x in list(G.degree())], bins=bins)
    # plt.show()

def show_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    plt.show()

if __name__ == '__main__':
    main()