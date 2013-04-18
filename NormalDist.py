import math as M
import collections as C
#import numpy as np

def mean(data):
	return sum(data)/float(len(data))

def deviations(data):
	return [d - mean(data) for d in data]
	
def stand_dev(data):	
	return M.sqrt(sum([ d**2 for d in deviations(data)]) / len(data))

def sem(data):
	return stand_dev(data) / M.sqrt(len(data))

def median(data):
	data.sort()
	dlen = len(data)
	return data[dlen/2] if dlen % 2 == 1 else mean([data[dlen/2]] + [data[dlen/2 - 1]])
	
	
def interquartiles(data):
	q1 = median([d for d in data if d < median(data)])
	q3 = median([d for d in data if d > median(data)])
	return (q1, q3)
	
def outliers(data):
	q1, q3 = interquartiles(data)
	iqr = q3 - q1
	return [d for d in data if d < (q1 - 1.5 * iqr) or (d > q3 + 1.5 * iqr)]
	
	
def pdf(m, s, x):
	return M.exp(- (x - m)**2 / (2 * s**2)) / (s * M.sqrt(2 * M.pi))

def phi(z):
    return 0.5 * (1.0 + M.erf(z/M.sqrt(2)))

# Calculate the probability for a range 
# m = mean, s = stand dev, low = lower bound, up = upper bound
# for low = - infinity use low = None
# for up  = + infinity use up = None
def prob_phi(m, s, low, up):
    s = float(s)

    ur = phi((up - m)/s)  if not up == None else 1.0
    lr = phi((low - m)/s) if not low == None else 0.0

    return round(ur - lr, 4)

def map2(f, list1, list2):
	return [f(list1[i], list2[i]) for i in range(len(list1))]

def map3(f, list1, list2):
	return [ map2(f, [i for j in range(len(list1))], list2) for i in list1 ]

for lst in  map3(lambda a,b: (a + b) / 2., [1,2,3,4], [1,2,3,4]):
	print lst
	
def flatten_list(lst):
	flat = []
	for e in lst:
		flat += [e] if not isinstance(e, list) else flatten_list(e)
	return flat
	
def hist_data(data):
	hist = {}
	for d in data:
		if not d in hist:
			hist[d] = 0
		hist[d] += 1
	return C.OrderedDict(sorted(hist.items()))
	
def print_hist(data):
	hist = hist_data(data)
	f = 80. / max(hist.values())
	for k,v in hist.items():
		print k, "*" * v * int(f)
		
data = flatten_list(map3(lambda a,b: (a + b) / 2., [1,2,3,4], [1,2,3,4]))
print prob_phi(37.72, (16.0366584219084 / M.sqrt(250)), 40, None)
print (40 - 37.72) / (16.0366584219084 / M.sqrt(250)) 