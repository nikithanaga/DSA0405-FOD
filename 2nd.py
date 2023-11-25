from scipy import stats
import numpy as np


data_A = np.array([0.12, 0.15, 0.18, 0.2,0.22])
data_B = np.array([0.1, 0.13, 0.16, 0.19, 0.21])


t_statistic, p_value = stats.ttest_ind(data_A, data_B, equal_var=True)  


alpha = 0.05


print("t-statistic:", t_statistic)
print("p-value:", p_value)


if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference.")
