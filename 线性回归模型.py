# 导入第三方库
import pandas as pd
import statsmodels.formula.api as smf

# 读入商品利润数据
profit = pd.read_excel(r'D:\Documents\Code\DataAnalysis\Excel1.xlsx', sheet_name = 2)

# 创建多元线性回归模型
lm = smf.ols('Profit ~ RD_Spend + Administration + Marketing_Spend', data  = profit).fit()

# 返回模型概览
print(lm.summary())