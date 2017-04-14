from __future__ import division

def loadAfinn(filename):
    f=open(filename,'r')
    afinn={}
    line=f.readline()
    nbr=0
    while line:
        nbr+=1
        l=line[:-1].split('\t')
        afinn[l[0]]=float(l[1])/4 
        line=f.readline()

    return afinn

def afinnPolarity(tweet,afinn):
    p=0.0
    nbr=0
    for w in tweet.split():
        if w in afinn.keys():
            nbr+=1
            p+=afinn[w]
    if (nbr != 0):
        return p/nbr
    else:
        return 0.0

