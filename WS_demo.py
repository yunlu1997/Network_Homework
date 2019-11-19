import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def ws_and_pos(n=100,k=5,p=0.1):
  WS = nx.random_graphs.watts_strogatz_graph(n, k, p)
  pos = nx.circular_layout(WS)
  return WS ,pos

def LandC_ws(p_,n=1000, k=20):
    L = []
    C = []

    for p in p_:

        WS = nx.random_graphs.watts_strogatz_graph(n, k, p)
        L.append(nx.average_shortest_path_length(WS))
        C.append(nx.average_clustering(WS))

    L = np.array(L)
    C = np.array(C)
    L_ = L/ L[0]
    C_ = C/ C[0]
    return L_,C_



if __name__=='__main__':
    # 画出规则网络、小世界网络、随机网络
    i=1
    p_=[0,0.1,1]
    for p in p_:
        WS, pos = ws_and_pos(n=100, k=10, p=p)
        plt.subplot(1,len(p_),i)
        plt.title('p='+str(p),fontsize='24')
        nx.draw(WS, pos, with_labels=False, node_size=30)
        i = i+1
    plt.show()
    # 计算不同的p所对应的 L和C
    p_ = [0, 0.001, 0.01,0.1,0.4,0.8, 1]
    for p in p_:
        WS, pos = ws_and_pos(n=100, k=10, p=p)
        print('p=',p)
        print('聚类系数：',nx.average_clustering(WS))
        print('平均最短路径', nx.average_shortest_path_length(WS))

    # 绘制L 和 C 随 p变化的趋势图
    p_ = np.array([0.00001, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    L_, C_ = LandC_ws(p_,n=1000,k=20)
    plt.semilogx(p_, L_, c='blue', label='L(p)/L(0)')
    plt.semilogx(p_, C_, c='red', label='C(p)/C(0)')
    plt.legend()
    plt.title('n=1000, k=20')
    plt.show()
