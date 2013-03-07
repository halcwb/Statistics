import math as m
import random

# Combinations of k events in a total of n events
# Calculates n! / (k! * (n - k)!)
def combinations(k, n):
    num, den = 1, 1
    for i in range(k):
        num = (n  - i) * num
        den = (k - i) * den
    return num / den

def permutations(n, k):
    num = 1
    for i in range(k):
        num *= (n - i)  
    return num 
    
print permutations(7,3)

# P of k heads for n flips
def coin_flips(k, n, p):
    return combinations(k, n) * (p ** k) * ((1 - p) **(n - k))
    
# Pascals triangle to calculate
# combinations of k in n
def get_combinations(n, m):
    c = { 1: [1, 1] }
    
    for i in range(2, n + 1):
        c[i] = [1] + [ sum([ c[i - 1][k - j] for j in range(m + 1) ]) for k in range(1, len(c[i -1]))  ] + [1]
    
    return c

        
def binom_dist(n, pl):
    c = get_combinations(n, len(pl))
    
    for p in pl:
        for i in c:
            c[i] = [ (c[i][k] * (p ** (k))) * ((1 - p) ** (i - k)) for k in range(len(c[i])) ]
    
    return c  

# Calculates mean of list of data
def mean(data):
    return sum(data)/(len(data) - 0.)
     

# Variance of data
# Input data list
# Calculates Sum[(d - d_mean)**2]   
# Output variance
def variance(data):
    m = mean(data) 
    return sum([(d - m) ** 2 for d in data])
    
def stand_dev(data):
    return m.sqrt(variance(data) / (len(data) - 1))    

def normal_p(x, m, sd):
    return (1 / m.sqrt(2 * m.pi * sd **2)) * m.exp(((x - m) ** 2) / (-2 * sd ** 2))
    
def normal_dist(data):
    m = sum(data) / len(data)
    sd = stand_dev(data)
    return [ normal_p(d, m, sd) for d in data  ]

def cum_dist(data):
    cum = normal_dist(data)
    return [ sum([ cum[i] for i in range(j)]) for j in range(len(cum)) ]

def print_hist(dist, r):
    r = len(dist) / r
    x = 80. / (max(dist) * r)
    v, bar = 0, ''

    for k in range(len(dist)):
        if k % r != 0: v += dist[k]
        else: 
            bar = "*" * int(x * v)
            if bar != "": print k, bar
            v, bar = 0, ''

weight=[ 80.,85,200,85,69,65,68,66,85,72,85,82,65,105,75,80,
         70,74,72,70,80,60,80,75,80,78,63,88.65,90,89,91,
         75,75,90,80,75,86.54,67,70,92,70,76,81,93,
         70,85,75,76,79,89,80,73.6,80,80,120,80,70,110,65,80,
         250,80,85,81,80,85,80,90,85,85,82,83,80,160,75,75,
         80,85,90,80,89,70,90,100,70,80,77,95,120,250,60 ]
        
#print print_hist(binom_dist(1000, [0.99])[1000])
#test = [ random.randint(0,1) for i in range(10000)  ]

#print math.exp(0) / math.sqrt(2 * math.pi * (0.25) ** 2)

def relative_change(a, b):
    return (b - a) / a

distance = [ 0.79,
             0.7,
             0.73,
             0.66,
             0.65,
             0.7,
             0.74,
             0.81,
             0.71,            
             0.7
           ]
        
print round(0.009 / (0.009 + 0.198), 3)