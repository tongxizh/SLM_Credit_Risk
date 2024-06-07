
"""
编写时间：2023年8月19日 15：00（修正版）

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from KDEpy import NaiveKDE

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = True
plt.rcParams["ytick.right"] = True


#---------------------a）利用Matplotlib的原生方法绘制的“山脊”图------------------------------

group_data = pd.read_csv(r"\分布类型图表\多类别核密度数据2.csv")
college = group_data.sort_index()
sord_index = [i for i in group_data.color.unique()]
sord_index = sorted(sord_index,key=str.lower)
test_data = group_data.loc[group_data["color"]=="H","depth"]

fig,ax = plt.subplots(figsize=(5.5,4.5),dpi=100,facecolor="w")
for i,index in zip(range(len(sord_index)),sord_index):
    data = group_data.loc[group_data["color"]==index,"depth"].values
    x,y = NaiveKDE(kernel="Gaussian",bw=.8).fit(data).evaluate()
    ax.plot(x,6*y+i, lw=.6,color="k",zorder=100 - i)
    ax.fill(x,6*y+i, lw=1,color="gray",alpha=.6,zorder=100 - i)
    #ax.axhline(i,ls="--",lw=.7,color="gray",zorder=100 - i)
    ax.grid(which="major",axis="y",ls="--",lw=.7,color="gray",zorder=-1)
    ax.set_xlim(50,72)
    ax.yaxis.set_tick_params(labelleft=True)
    ax.set_yticks(np.arange(len(sord_index)))
    ax.set_yticklabels(sord_index)
    ax.set_xlabel("Depth")
    ax.set_ylabel("Color")
    ax.tick_params(which ="both",top=False,right=False)
    ax.tick_params(which = "minor",axis="both",left=False,bottom=False)
    for spin in ["top","right","bottom","left"]:
        ax.spines[spin].set_visible(False)
fig.savefig('\单变量图表绘制\\图3-2-10 “山脊”图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\单变量图表绘制\\图3-2-10 “山脊”图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
            
            
#------------------------------b）利用JoyPyjoyplot绘制的“山脊”图-------------------------
import joypy

sord_index = [i for i in group_data.color.unique()]
sord_index = sorted(sord_index,key=str.lower)
sord_index = sord_index[::-1]

plt.rcParams["font.family"] = "Times New Roman"

fig, axes = joypy.joyplot(group_data, by="color", column="depth", labels=sord_index, 
                          grid="y", linewidth=1, figsize=(7,6),color="gray",
                          xlabelsize=15,ylabelsize=15)
fig.savefig('\单变量图表绘制\\图3-2-10 “山脊”图绘制示例_b.pdf',
            bbox_inches='tight')
fig.savefig('\单变量图表绘制\\图3-2-10 “山脊”图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)





















