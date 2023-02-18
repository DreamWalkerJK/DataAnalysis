# 导入第三方库
from scipy import stats
import pandas as pd

# 读取数据
cars = pd.read_excel(r'D:\Documents\Code\DataAnalysis\Excel1.xlsx', sheet_name = 1)
result = stats.pearsonr(cars.speed, cars.dist)

# statistic相关系数，pvalue概率P值
print(result)