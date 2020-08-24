import pandas as pd
import os

# data = pd.read_csv('data.csv')
# with open('1_demand.txt','a+') as f:
#     for line in data.values:
#         # if (line[1] == 3 or line[1] == 6 or line[1] == 9) and (line[0] >= 3170 and line[0] < 3201):
#         if line[1] == 7:
#             # f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(round(line[2]*0.1,2))+'\t'+str(round(line[3]*0.1,2))+'\n'))
#             f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(round(line[2]))+'\t'+str(round(line[3]))+'\n'))

# data = pd.read_table('3_defender.txt')
# data_d = pd.read_table('3_demand.txt')
# with open('disappearing time 3.txt','a+') as f:
#     for i in range(4998): # index of the last line minus 1
#         if (abs(data.iloc[i+1][2] - data.iloc[i][2]) > 10):
#             f.write(str(data.iloc[i+1][0]) + '\n')
#         if (abs(data_d.iloc[i+1][2] != data_d.iloc[i][2])):
#             f.write(str(data_d.iloc[i+1][0]) + '\n')

ref = pd.read_table('tictoc.txt')
data = pd.read_csv('data.csv')

# i = 0
# while(1):
#     i = i + 1
#     with open('./3/data_3_{}.txt'.format(i),'a+') as f:
#         for line in data.values:
#             if (line[1] == 3 or line[1] == 6 or line[1] == 9) and \
#                     (line[0] >= ref.iloc[i-1][0] and line[0] < ref.iloc[i][0] and ref.iloc[i][0] - ref.iloc[i-1][0] >= 16):
#                 f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(round(line[2]))+'\t'+str(round(line[3]))+'\n'))

i = -2
while(1):
    i = i + 2
    with open('./multiagent/data_compli_{}.txt'.format(i),'a+') as f:
        for line in data.values:
            if (line[0]>=3906 and line[0] >= ref.iloc[i][0] and line[0] < ref.iloc[i+1][0]):
                f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(round(line[2]))+'\t'+str(round(line[3]))+'\n'))