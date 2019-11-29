import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

BA=nx.barabasi_albert_graph(500,1)
BA_1 = nx.barabasi_albert_graph(1000,1)

ps=nx.spring_layout(BA) #布置框架

degree =  nx.degree_histogram(BA)          #返回图中所有节点的度分布序列
degree_1 =  nx.degree_histogram(BA_1)

x = range(len(degree))                             #生成x轴序列，从1到最大度
y = [z / float(sum(degree)) for z in degree] #将频次转换为频率
x1 = range(len(degree_1))                             #生成x轴序列，从1到最大度
y1 = [z / float(sum(degree_1)) for z in degree_1] #将频次转换为频率

plt.loglog(x,y,"ro",color='red',label='n=500')
plt.loglog(x1,y1,"ro",color = 'green',label='n=1000')
plt.ylabel('p(k)',fontsize=14)
plt.xlabel('k',fontsize=14)         #在双对数坐标轴上绘制度分布曲线

x_= range(1,len(degree)+1)
y_ = [math.pow(z,-3) for z in x_]
y_1 = [math.pow(z,-2) for z in x_]
plt.loglog(x_,y_,linewidth=1,label='k^-3',linestyle="--")
plt.loglog(x_,y_1,linewidth=1,label='k^-2',linestyle="--")
plt.legend()
plt.show()

#显示图表
nx.draw(BA,ps,with_labels=False,node_size=30)

plt.show()