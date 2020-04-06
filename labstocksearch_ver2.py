import pandas as pd  
import numpy as np
import os
import sys

data = pd.read_csv("Mat_a_obs.csv")
df = pd.DataFrame(data)
#print(df.isnull().sum())
df["Plate"] = df["Plate"].fillna(0)
df["Plate"] = df["Plate"].astype(int)

df["Col"] = df["Col"].fillna(0)
df["Col"] = df["Col"].astype(int)

df["record no."] = df["record no."].fillna(0)
df["record no."] = df["record no."].astype(int)
df = df.drop(["Comment"],axis = 1)
#df["record no."] = df["record no."].astype(str)

#print(df.head())

df["Plate"] = df["Plate"].astype(str)
df["Row"] = df["Row"].astype(str)    
df["Col"] = df["Col"].astype(str)

#print("after\n",df.head())

df["Position"] = df["Plate"]+"-"+df["Row"]+df["Col"]
#print(df.head())

drop_list = ["Plate","Row","Col","Strain","Batch"]
df = df.drop(drop_list,axis = 1)
print(df.head())

f = open("input_labstocksearch.txt","r")
input_file = f.readlines()
gene = []
for i in input_file:
    gene.append(i.strip())
print(gene)
f.close()

cols = ["record no.","ORF name","Position"]
ans = pd.DataFrame(index=[], columns=cols)

for j in gene:
    tmp = df[df["ORF name"] == j ]
    ans = ans.append(tmp,ignore_index = True)
print(ans)

ans.to_csv("output_labstocksearch.txt",sep ="\t",index = False,header = False)