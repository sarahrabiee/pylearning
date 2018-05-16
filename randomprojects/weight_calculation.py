import numpy as np

mx_week_weight = np.matrix('0.65, 0.75, 0.85; 0.70, 0.80, 0.90; 0.75, 0.85, 0.95; 0.40, 0.50, 0.60')
max_weight = float(input('How many kilogram(s) was your latest max for squat training?(e.g. 52.5)'))


first_month_weight = np.dot(mx_week_weight, max_weight)

print(mx_week_weight)
print('------weights----------')
print(first_month_weight)
