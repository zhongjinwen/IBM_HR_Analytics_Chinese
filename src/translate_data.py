import pandas as pd
import os

# 读取原始数据
df = pd.read_csv('data/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# 列名汉化映射
column_mapping = {
    'Age': '年龄',
    'Attrition': '是否离职',
    'BusinessTravel': '出差频率',
    'DailyRate': '日薪',
    'Department': '部门',
    'DistanceFromHome': '离家距离',
    'Education': '教育程度',
    'EducationField': '教育领域',
    'EmployeeCount': '员工计数',
    'EmployeeNumber': '员工编号',
    'EnvironmentSatisfaction': '环境满意度',
    'Gender': '性别',
    'HourlyRate': '时薪',
    'JobInvolvement': '工作投入度',
    'JobLevel': '职位等级',
    'JobRole': '职位角色',
    'JobSatisfaction': '工作满意度',
    'MaritalStatus': '婚姻状况',
    'MonthlyIncome': '月收入',
    'MonthlyRate': '月费率',
    'NumCompaniesWorked': '曾工作公司数',
    'Over18': '是否满18岁',
    'OverTime': '是否加班',
    'PercentSalaryHike': '薪资涨幅百分比',
    'PerformanceRating': '绩效评级',
    'RelationshipSatisfaction': '关系满意度',
    'StandardHours': '标准工时',
    'StockOptionLevel': '股票期权等级',
    'TotalWorkingYears': '总工作年限',
    'TrainingTimesLastYear': '去年培训次数',
    'WorkLifeBalance': '工作生活平衡',
    'YearsAtCompany': '本公司工作年限',
    'YearsInCurrentRole': '现任职位年限',
    'YearsSinceLastPromotion': '上次晋升至今年限',
    'YearsWithCurrManager': '现任经理共事年限'
}

# 应用列名汉化
df.rename(columns=column_mapping, inplace=True)

# 关键字段内容汉化
df['是否离职'] = df['是否离职'].map({'Yes': '是', 'No': '否'})
df['性别'] = df['性别'].map({'Male': '男', 'Female': '女'})

travel_mapping = {
    'Non-Travel': '不出差',
    'Travel_Rarely': '偶尔出差',
    'Travel_Frequently': '经常出差'
}
df['出差频率'] = df['出差频率'].map(travel_mapping)

df['是否加班'] = df['是否加班'].map({'Yes': '是', 'No': '否'})

marital_mapping = {
    'Single': '单身',
    'Married': '已婚',
    'Divorced': '离异'
}
df['婚姻状况'] = df['婚姻状况'].map(marital_mapping)

# 保存汉化后的数据
output_path = 'output/IBM_HR_员工流失数据_汉化版.csv'
os.makedirs('output', exist_ok=True)
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print("✅ 汉化完成！")
print(f"数据形状：{df.shape}")
print(f"输出路径：{output_path}")