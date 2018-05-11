import numpy as np

mx_week_weight = np.matrix('0.65, 0.75, 0.85; 0.70, 0.80, 0.90; 0.75, 0.85, 0.95')
max_weight = int(input('How many kilogram was your latest max for squat training?(e.g. 52.5)'))


first_month_weight = np.dot(mx_week_weight, max_weight)

print(mx_week_weight)
print('------weights----------')
print(first_month_weight)
