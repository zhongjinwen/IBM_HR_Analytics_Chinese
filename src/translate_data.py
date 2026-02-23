# -*- coding: utf-8 -*-
"""
IBM HR 员工流失数据集 - 汉化脚本 v2.0
======================================
功能：
1. 将35个字段名翻译为中文
2. 将分类变量的值翻译为中文
3. 输出 UTF-8 with BOM 编码，Excel 直接打开不乱码
"""

import pandas as pd
import os
from pathlib import Path

# ==================== 配置区域 ====================
INPUT_FILE = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "IBM_HR_员工流失数据_全汉化版.csv")

# ==================== 1. 字段名翻译映射 ====================
COLUMN_TRANSLATION = {
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
    'MonthlyRate': '月薪',
    'NumCompaniesWorked': '曾工作公司数',
    'Over18': '是否成年',
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
    'YearsWithCurrManager': '与现任经理共事年限'
}

# ==================== 2. 分类变量值翻译映射 ====================
VALUE_TRANSLATION = {
    # 二元变量
    '是否离职': {'Yes': '是', 'No': '否'},
    '是否加班': {'Yes': '是', 'No': '否'},
    '是否成年': {'Y': '是', 'N': '否'},
    
    # 出差频率
    '出差频率': {
        'Non-Travel': '不出差',
        'Travel_Rarely': '偶尔出差',
        'Travel_Frequently': '频繁出差'
    },
    
    # 部门
    '部门': {
        'Sales': '销售部',
        'Research & Development': '研发部',
        'Human Resources': '人力资源部'
    },
    
    # 教育程度
    '教育程度': {
        1: '小学及以下',
        2: '中学',
        3: '专科',
        4: '本科',
        5: '硕士及以上'
    },
    
    # 教育领域
    '教育领域': {
        'Life Sciences': '生命科学',
        'Medical': '医学',
        'Marketing': '市场营销',
        'Technical Degree': '工程技术',
        'Human Resources': '人力资源',
        'Other': '其他'
    },
    
    # 环境满意度
    '环境满意度': {
        1: '非常不满意',
        2: '不满意',
        3: '一般',
        4: '满意'
    },
    
    # 性别
    '性别': {'Male': '男', 'Female': '女'},
    
    # 工作投入度
    '工作投入度': {
        1: '非常低',
        2: '低',
        3: '一般',
        4: '高'
    },
    
    # 职位角色
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
    },
    
    # 工作满意度
    '工作满意度': {
        1: '非常不满意',
        2: '不满意',
        3: '一般',
        4: '满意'
    },
    
    # 婚姻状况
    '婚姻状况': {
        'Single': '单身',
        'Married': '已婚',
        'Divorced': '离异'
    },
    
    # 绩效评级
    '绩效评级': {
        1: '低',
        2: '良好',
        3: '优秀',
        4: '卓越'
    },
    
    # 关系满意度
    '关系满意度': {
        1: '非常不满意',
        2: '不满意',
        3: '一般',
        4: '满意'
    },
    
    # 工作生活平衡
    '工作生活平衡': {
        1: '非常差',
        2: '较差',
        3: '一般',
        4: '较好'
    },
    
    # 股票期权等级
    '股票期权等级': {
        0: '无',
        1: '低级',
        2: '中级',
        3: '高级'
    }
}


def translate_values(df, translation_dict):
    """翻译分类变量的值"""
    df_translated = df.copy()
    translated_count = 0
    
    for col in df_translated.columns:
        if col in translation_dict:
            mapping = translation_dict[col]
            df_translated[col] = df_translated[col].map(mapping).fillna(df_translated[col])
            print(f"  ✓ 翻译列: {col}")
            translated_count += 1
    
    print(f"  共翻译了 {translated_count} 列的分类变量")
    return df_translated


def main():
    print("="*50)
    print("IBM HR 员工流失数据集 - 汉化工具 v2.0")
    print("="*50)
    
    # 检查输入文件
    if not os.path.exists(INPUT_FILE):
        print(f"❌ 错误: 找不到输入文件 {INPUT_FILE}")
        print("请确保 data/ 目录下存在原始数据文件")
        return
    
    # 创建输出目录
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    
    # 读取数据
    print(f"\n📖 读取数据: {INPUT_FILE}")
    df = pd.read_csv(INPUT_FILE)
    print(f"✅ 读取成功: {len(df)} 行, {len(df.columns)} 列")
    
    # 翻译列名
    print("\n🔄 翻译列名...")
    df.rename(columns=COLUMN_TRANSLATION, inplace=True)
    print("✅ 列名翻译完成")
    
    # 翻译变量值
    print("\n🔄 翻译分类变量值...")
    df = translate_values(df, VALUE_TRANSLATION)
    
    # 保存结果
    print(f"\n💾 保存文件: {OUTPUT_FILE}")
    df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
    print("✅ 保存成功!")
    
    # 预览
    print("\n📊 数据预览 (前5行):")
    print("="*60)
    preview_cols = ['年龄', '性别', '部门', '是否离职', '月收入']
    available_cols = [c for c in preview_cols if c in df.columns]
    print(df[available_cols].head().to_string())
    print("="*60)
    
    print(f"\n✨ 完成！输出文件: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()