import numpy as np
monthly_sales = np.array([
    2500, 2700, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4500, 4800, 5000,  # Year 1
    5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400   # Year 2
])
print('Total sales',np.sum(monthly_sales))
print('Median sale',np.median(monthly_sales))
print('Std deviation',np.std(monthly_sales))
print('mean ',np.mean(monthly_sales))
print('sale difference ',np.diff(monthly_sales))