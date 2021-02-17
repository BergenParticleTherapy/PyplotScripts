
######################################################################
#
#    Enkelt plotteskript som plotter forskjellen i median av mediandoser til flere pasienter 
#    beregnet med to ulike beregningsmetoder, sammen med D50 range, per struktur. Alt som 
#    plottes er allerede regnet ut og gitt i et excelark.  
#    Brukt i Christoffer sin masteroppgave.
#
######################################################################

from matplotlib.pyplot import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# Reading an excel file using Python
import xlrd
 
# Give the location of the file
loc = r'H:\data\Python\Christoffer\\'

 
# To open Workbook
wb_D50 = xlrd.open_workbook(loc+r'D50_median_range_OAR_target_volume.xlsx')
sheet_wb_D50 = wb_D50.sheet_by_index(0)
 
target_D50 = []
D50_VMAT_median= []
D50_VMAT_min = []
D50_VMAT_max = []

D50_IMPT_median= []
D50_IMPT_min = []
D50_IMPT_max = []

for i in range(sheet_wb_D50.nrows):
    target_D50.append(sheet_wb_D50.cell_value(i, 0))
    D50_VMAT_median.append(sheet_wb_D50.cell_value(i, 1))
    D50_VMAT_min.append(sheet_wb_D50.cell_value(i, 2))
    D50_VMAT_max.append(sheet_wb_D50.cell_value(i, 3))
    D50_IMPT_median.append(sheet_wb_D50.cell_value(i, 4))
    D50_IMPT_min.append(sheet_wb_D50.cell_value(i, 5))    
    D50_IMPT_max.append(sheet_wb_D50.cell_value(i, 6))    

x_axis = range(len(target_D50[1:]))

x_labels =target_Dmean[1:]
x_labels.append('')
x_labels.insert(0,'')

#Plot figure
figuresize=[13,4]   
left = 0.07
bottom = 0.305
right = 0.98
top = 0.983
wspace = 0.33
hspace = 0.45

fig = plt.figure(figsize=(figuresize[0],figuresize[1]))
fig.subplots_adjust(left=left,right=right,bottom=bottom,top=top, wspace = wspace, hspace = hspace)
#plt.style.use('classic')

ax = fig.add_subplot(111)

yerror_D50_VMAT = [np.array(D50_VMAT_median[1:])-np.array(D50_VMAT_min[1:]),np.array(D50_VMAT_max[1:])-np.array(D50_VMAT_median[1:])]
yerror_D50_IMPT = [np.array(D50_IMPT_median[1:])-np.array( D50_IMPT_min[1:]),np.array(D50_IMPT_max[1:])-np.array(D50_IMPT_median[1:])]



#For aa skifte navn i legend endrer du det som staar i teksten etter label = '... :) 
ax.errorbar(np.array(x_axis)+0.9,D50_VMAT_median[1:],yerr=yerror_D50_VMAT,color = 'black',linestyle = '', marker = 'o',capsize=4, label = 'D50_VMAT_median')
ax.errorbar(np.array(x_axis)+1.1,D50_IMPT_median[1:],yerr=yerror_D50_IMPT,color = 'blue',linestyle = '', marker = 'o',capsize=4, label = 'D50_IMPT_median')


#Legend: ncol = antall kolonner, loc = plassering
plt.legend(loc = 'lower right',ncol = 3,shadow = False,prop={'size':11},handlelength=1.3,frameon = True,handletextpad=1,borderpad=0.5,labelspacing = 1.2)#,columnspacing=cs)

ax.set_xticks(range(len(x_labels)))
print(x_labels)
plt.ylim([-20,22])
plt.xlim([0.5,18])
ax.set_xticklabels(x_labels, minor=False, rotation=30,size=14)

ylabel(r'Dose difference [Gy]', size = 14)

#------------------------------------------------------------------------------------------#


plt.show()
