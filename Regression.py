import math

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
    return math.sqrt(variance(data) / len(data))    
    
def xy_covariance(data):
    x_m = mean([d[0] for d in data])
    y_m = mean([d[1] for d in data])
    return (x_m, y_m, sum([(d[0] - x_m) * (d[1] - y_m) for d in data]))
    
# Linear regression y = bx + a
# Input data list with (x, y) tuples
# Calculates  Sum[(xi - x_mean)(yi - y_mean)] 
#            --------------------------------
#                 Sum[(xi - x_mean) ** 2]
# Output(x_mean, y_mean, b, a
def linear_regression(data):
    x_m, y_m, covar = xy_covariance(data)
    b = covar /variance([d[0] for d in data])
    return (x_m, y_m, b, y_m - b * x_m)
    
# Correlation coefficient
# Input list of (x,y) tuples
# Calculates      Sum[(xi - x_mean)(yi - y_mean)]
#            ------------------------------------------
#            Sqrt(Sum[(xi - x_mean)**2 (yi-y_mean)**2])
def correlation(data):
    x_m, y_m, covar = xy_covariance(data)
    r = covar / math.sqrt(variance([d[0] for d in data]) * variance([d[1] for d in data]))
    return (x_m, y_m, r)

# Return list of z-values for data
# Calculates xi - x_mean
#            -----------
#              sd(x)    
def z_values(data):
    m = mean(data)
    sd = stand_dev(data)
    return [(d - m) / sd for d in data]
    
    
testdata1 = [(6.,7.),(2.,3.),(1.,2.),(-1.,0.)]
testdata2 = [(3.,7.),
             (4.,8.),
             (5.,9.)]
testdata3 = [(0.,0.),
             (1.,0.),
             (2.,0.),
             (3.,0.),
             (4.,0.),
             (6.,0.),
             (7.,0.),
             (8.,0.),
             (9.,0.),
             (1000.,1000.)]
testdata4 = [(2.,8.),
             (4.,14.),
             (6.,26.),]

challenger = [(70,1),
              (57,1),  
              (63,1),  
              (70,1),  
              (53,2),  
              (75,2),  
              (58,1),  
             ] 
print len(challenger)           
print sum([d[0]*d[1] for d in challenger])

print round((574 - ((1600*9)/23.)) / (112400 - (1600**2/23.)), 4)
print round(9/23. - (574 - ((1600*9)/23.)) / (112400 - (1600**2/23.)) * 1600 / 23. , 4)
print -0.0475 * 36 + 3.698

print 0.7 * 0.5

print linear_regression([(0,0),(1,2),(2,2)])
print correlation(challenger)

