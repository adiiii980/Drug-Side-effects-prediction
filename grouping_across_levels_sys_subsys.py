#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

dfs1=pd.read_excel('/Users/adityaankush/Desktop/mod_data/subsystem-2.xlsx')#,sheet_name=None)
dfs2=pd.read_excel('/Users/adityaankush/Desktop/mod_data/system-2.xlsx')#,sheet_name=None)


# In[6]:


print((dfs1.columns))
#dfs1=dfs1.dropna()
#dfs2=dfs2.dropna()
print(dfs2)


# In[7]:


sub_sys=list(dfs1.columns)
sys=list(dfs2.columns)
se_sub={}
d1=dfs1.as_matrix()
for i in d1:
    for j in range(len(i)):
        if i[j] not in se_sub:
            se_sub[i[j]]=[]
            se_sub[i[j]].append(sub_sys[j])
        else:
            print("problem")
            print(i[j]),
            print(sub_sys[j])
            se_sub[i[j]].append(sub_sys[j])
print(se_sub)
print(len(se_sub.keys()))

l=[[1,2],[3,4,5]]
l=pd.DataFrame(l)
l1=l.as_matrix()
l1=l1.tolist()
print(l1)
for i in l1:
    print(len(i))
# In[8]:


sub_lev={}
for i in sub_sys:
    #print(i)
    d=dfs1[i]
    d=pd.DataFrame(d)
    d=d.dropna()
    s_l=d[i]
    s_l=s_l.tolist()
    for j in s_l:
        if j not in sub_lev:
            sub_lev[j]=[]
            sub_lev[j].append(i)
        else:
            print("----------")
            print(j)
            print(i)
            sub_lev[j].append(i)
            print(sub_lev[j])
print(len(sub_lev.keys()))
print(sub_lev)


# In[ ]:


sys_lev={}
se_seen={}
for i in sys:
    sys_lev[i]=[]
    d=dfs2[i]
    d=pd.DataFrame(d)
    d=d.dropna()
    s_l=d[i]
    #print(s_l)
    s_l=s_l.tolist()
    for j in s_l:
        try:
            sys_lev[i]+=sub_lev[j]
        except:
            print(j)
for i in sys_lev:
    sys_lev[i]=np.asarray(sys_lev[i])
    sys_lev[i]=np.unique(sys_lev[i])
    sys_lev[i]=sys_lev[i].tolist()
print(sys_lev)
#system=pd.DataFrame(sys_lev)
'''l=[]
for i in sys_lev:
    l.append(sys_lev[i])
system=pd.DataFrame(l)
print(system)'''


# In[ ]:


l=[[0,1],[1,0],[0,0]]
l=pd.DataFrame(l)
col=list(l.columns)
tt=[]
for i in col:
    tt.append(l[i])
ans=[0]*tt[0].size
print(ans)
ans=pd.Series(ans)
for i in range(len(tt)):
    ans=ans|tt[i]
print(ans)
#ls=l[0] | l[1]
#print(ls)
#print(type(ls))


# In[ ]:


maxx=-1
for i in sys_lev:
    if(len(sys_lev[i])>maxx):
        maxx=len(sys_lev[i])
print(maxx)
l=[-1]*maxx
dat=pd.DataFrame(l)
for i in sys_lev:
    dat[i]=pd.DataFrame(sys_lev[i])
dat=dat.drop(dat.columns[[0]],axis=1)
print(dat)


# In[ ]:


col1=list(dat.columns)
fname='/Users/adityaankush/Desktop/mod_data/sys_sub_sys_2.xlsx'
writer = pd.ExcelWriter(fname)
dat.to_excel(writer,sheet_name='sub_sys',columns=col1)
writer.save()

dfs1=pd.read_excel('/Users/adityaankush/Desktop/sys_sub_sys.xlsx',sheet_name=None)

#print(dfs1.keys())
print(dfs1['sys_sub_sys'].columns)
# In[ ]:




