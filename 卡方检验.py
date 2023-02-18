# 导入第三方库
from scipy import stats
import pandas as pd

# 读入excel数据
students = pd.read_excel(r'D:\Documents\Code\DataAnalysis\Excel1.xlsx')

# 构造两个离散型变量之间的频次统计表（或列联表）
crosstable = pd.crosstab(students.Gender, students.Offer)
# 卡方检验
result = stats.chi2_contingency(crosstable)

# statistic统计值，pvalue概率P值
print(result)