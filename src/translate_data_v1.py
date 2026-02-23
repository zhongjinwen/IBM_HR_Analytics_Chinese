"""
IBM HR数据集汉化工具
"""

import pandas as pd
from pathlib import Path


def translate_hr_data():
    """汉化HR数据"""
    project_root = Path(__file__).parent.parent
    
    # 路径设置
    input_file = project_root / "data" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
    output_file = project_root / "output" / "IBM_HR_中文完整版.csv"
    
    # 确保输出目录存在
    output_file.parent.mkdir(exist_ok=True)
    
    # 检查输入文件
    if not input_file.exists():
        print(f"❌ 错误：找不到文件 {input_file}")
        print("请将原始CSV文件放入 data/ 文件夹")
        return
    
    # 读取数据
    print(f"📖 读取数据：{input_file}")
    df = pd.read_csv(input_file)
    print(f"✅ 读取成功：{df.shape[0]}行 × {df.shape[1]}列")
    
    # 列名映射（完整版）
    column_mapping = {
        'Age': '年龄',
        'Attrition': '是否离职',
        'BusinessTravel': '出差频率',
        'Department': '部门',
        'DistanceFromHome': '通勤距离',
        'Education': '教育程度',
        'EducationField': '专业领域',
        'EmployeeNumber': '员工编号',
        'EnvironmentSatisfaction': '环境满意度',
        'Gender': '性别',
        'HourlyRate': '时薪',
        'JobInvolvement': '工作投入度',
        'JobLevel': '职位级别',
        'JobRole': '职位角色',
        'JobSatisfaction': '工作满意度',
        'MaritalStatus': '婚姻状况',
        'MonthlyIncome': '月收入',
        'MonthlyRate': '月费率',
        'NumCompaniesWorked': '曾任职公司数',
        'Over18': '是否成年',
        'OverTime': '是否加班',
        'PercentSalaryHike': '加薪比例',
        'PerformanceRating': '绩效评级',
        'RelationshipSatisfaction': '关系满意度',
        'StandardHours': '标准工时',
        'StockOptionLevel': '股票期权级别',
        'TotalWorkingYears': '总工作年限',
        'TrainingTimesLastYear': '去年培训次数',
        'WorkLifeBalance': '工作生活平衡',
        'YearsAtCompany': '司龄',
        'YearsInCurrentRole': '现任职位年限',
        'YearsSinceLastPromotion': '距上次晋升年数',
        'YearsWithCurrManager': '与现任经理共事年数',
        'DailyRate': '日薪',
        'EmployeeCount': '员工计数',
    }
    
    # 值映射
    value_mappings = {
        '是否离职': {'Yes': '是', 'No': '否'},
        '性别': {'Male': '男', 'Female': '女'},
        '是否加班': {'Yes': '是', 'No': '否'},
        '婚姻状况': {'Single': '未婚', 'Married': '已婚', 'Divorced': '离异'},
        '部门': {
            'Sales': '销售部',
            'Research & Development': '研发部',
            'Human Resources': '人力资源部'
        },
        '出差频率': {
            'Non-Travel': '不出差',
            'Travel_Rarely': '偶尔出差',
            'Travel_Frequently': '经常出差'
        },
        '专业领域': {
            'Life Sciences': '生命科学',
            'Medical': '医学',
            'Marketing': '市场营销',
            'Technical Degree': '技术学位',
            'Human Resources': '人力资源',
            'Other': '其他'
        },
        '职位角色': {
            'Sales Executive': '销售主管',
            'Research Scientist': '研究科学家',
            'Laboratory Technician': '实验室技术员',
            'Manufacturing Director': '制造总监',
            'Healthcare Representative': '医疗代表',
            'Manager': '经理',
            'Sales Representative': '销售代表',
            'Research Director': '研究总监',
            'Human Resources': '人力资源专员'
        }
    }
    
    # 执行转换
    print("\n🔄 转换列名...")
    df.rename(columns=column_mapping, inplace=True)
    
    print("🔄 转换分类值...")
    for col, mapping in value_mappings.items():
        if col in df.columns:
            df[col] = df[col].map(mapping)
    
    # 删除无用列
    useless = ['员工计数', '是否成年', '标准工时']
    df.drop(columns=[c for c in useless if c in df.columns], inplace=True)
    
    # 保存
    print(f"\n💾 保存到：{output_file}")
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    # 统计
    print("\n" + "=" * 50)
    print("✅ 汉化完成！")
    print(f"总行数：{len(df)}")
    print(f"总列数：{len(df.columns)}")
    print(f"\n输出文件：{output_file}")
    print("=" * 50)


if __name__ == "__main__":
    translate_hr_data()