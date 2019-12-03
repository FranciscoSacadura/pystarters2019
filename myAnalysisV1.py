import os
import pandas as pd
import matplotlib.pyplot as plt
from myPlotPanel import plotPanel
from myutils import mySaveFig

dataFilename = "data/All_three_exp_conditions_3.csv"
figFilename = "myfigures/my_absSpeedVsSpikesV1.png"
data = pd.read_csv(dataFilename, index_col=0)

print(data.columns.values)
# 'Expt #', 'Cell #', 'Speed', 'Bin(i)', 'Bin(i+1)', 'Bin(i+2)', 'Bin(i+3)', 
# 'Bin(i+4)', 'Bin(i+5)', 'Trial Condition', 'Region', 'Layer', 'Cell Type'

trialConditions = data.loc[:, "Trial Condition"].unique()
print(trialConditions)
# ['Vestibular' 'VisVes' 'Visual']

regions = data.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd' 'Hip']

# We will make a figure with len(trialConditions)==3 panels
f, axes = plt.subplots(1, len(trialConditions), sharey=True)

# Plot 3 pannels
[plotPanel(data,axes[i],trialConditions[i]) for i in range(len(trialConditions))]
axes[1].set_xlabel("Abs(Speed)")
axes[0].set_ylabel("Spike Count")

mySaveFig(figFilename)

f.show()
