# 导入第三方包
from scipy import stats

# 读入数据
volumns = [4988, 5006, 5021, 4923, 4947, 4896, 5104, 4992, 5070, 5009, 4892, 4997]
# t检验
result = stats.ttest_1samp(a = volumns, popmean = 5000)

# statistic概率值 pvalue概率P值
print(result)
