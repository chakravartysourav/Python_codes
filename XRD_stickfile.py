# -*- coding: utf-8 -*-
import numpy as np
#import seaborn as sbs
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


mpl.rcParams['pdf.fonttype']=42
df = pd.read_excel (r'C:\Users\sourav93\Desktop\xrd_sapo34_pdf.xlsx');
x_data=df['2-theta'];
y_data=df['intensity-1']
y_low=df['intensity_low']
fig=plt.figure(1,figsize = (10, 7))


plt.vlines(x_data,y_low,y_data,colors='r',linestyles='solid')
plt.gca().set_ylim(bottom=0) #setting y lower limit
plt.gca().set_xlim(right=60) # setting xupper limit
plt.gca().set_xlim(left=5)# setting xlower limit

plt.xlabel('2$\\theta$',fontsize =14)
plt.ylabel("Intensity (a.u)",fontsize =14)
plt.tick_params(labelsize=15)
ax = plt.gca()
ax.tick_params(axis='y', direction = 'in',length=12)
ax.tick_params(axis='x',length=10)
plt.gca
plt.gca().yaxis.set_ticklabels([]) # remove the y tick labels
plt.legend(['sapo-34'],frameon=False,fontsize=14);
#plt.savefig(r'C:\Users\sourav93\Desktop\sapo34.png',dpi=300,bbox_inches="tight")
#plt.savefig(r'C:\Users\sourav93\Desktop\sapo34.pdf',dpi=300,bbox_inches="tight")
#fig.show()