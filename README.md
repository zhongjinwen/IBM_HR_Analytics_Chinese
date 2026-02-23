# IBM HR Analytics 员工流失数据集（汉化版 v4.0）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.5+-green.svg)

## 📋 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的**本土化优化汉化版**。

原数据集包含1470名员工的信息，共35个字段，用于分析员工流失（Attrition）因素。

**✨ v4.0 核心特性：**
- ✅ **完全对照官方定义**：所有翻译基于 Kaggle 原数据集官方说明
- ✅ **本土化表达优化**：采用更符合中文HR领域的术语
- ✅ **字段名全中文**：35个字段全部翻译为中文
- ✅ **变量值精准翻译**：分类变量的值按官方定义精准汉化
- ✅ **Excel 友好**：UTF-8 with BOM 编码，直接打开不乱码
- ✅ **完整版本追溯**：保留 v1.0、v2.0、v3.0、v4.0 完整版本

**本仓库已包含原始数据文件，无需额外下载。**

---

## 🔍 v4.0 本土化优化说明

| 字段 | v3.0 翻译 | **v4.0 优化** | 优化理由 |
|------|-----------|---------------|----------|
| JobRole | 职位角色 | **岗位** | HR领域常用术语 |
| JobLevel | 职位等级 | **职级** | 更简洁专业 |
| JobInvolvement | 工作投入度 | **敬业度** | HR常用术语 |
| JobSatisfaction | 工作满意度 | **工作满意** | 更简洁 |
| WorkLifeBalance | 工作生活平衡 | **工作与生活平衡** | 更完整表达 |
| PercentSalaryHike | 薪资涨幅百分比 | **调薪幅度** | HR常用术语 |
| StockOptionLevel | 股票期权等级 | **股权激励等级** | 更符合中文企业用语 |
| TotalWorkingYears | 总工作年限 | **总工龄** | 更简洁 |
| YearsAtCompany | 本公司工作年限 | **本企业工龄** | HR术语 |
| YearsInCurrentRole | 现任职位年限 | **现岗年限** | 更简洁 |
| YearsSinceLastPromotion | 上次晋升至今年限 | **晋升间隔** | 专业HR术语 |
| NumCompaniesWorked | 曾工作公司数 | **跳槽次数** | 更口语化 |
| EnvironmentSatisfaction | 环境满意度 | **环境满意** | 更简洁 |
| RelationshipSatisfaction | 关系满意度 | **人际关系满意** | 更完整 |
| TrainingTimesLastYear | 去年培训次数 | **年度培训次数** | 更规范 |

---

## 📊 数据说明

### 数据来源
- **原始数据集**: IBM HR Analytics Employee Attrition & Performance
- **来源平台**: [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **原始作者**: Pavan Subhash
- **原始许可证**: [Open Data Commons Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)
- **数据文件**: `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`

### 数据规模
- **样本数**: 1,470 条
- **特征数**: 35 个字段
- **目标变量**: 是否离职（237人离职，1233人留任）

### 翻译效果示例

| 原字段 | 原值 | **v4.0 翻译** |
|--------|------|---------------|
| Attrition | Yes | 是否离职: **是** |
| JobRole | Sales Executive | 岗位: **销售主管** |
| JobInvolvement | 3 | 敬业度: **高** |
| WorkLifeBalance | 1 | 工作与生活平衡: **差** |
| PercentSalaryHike | 15 | 调薪幅度: **15%** |
| NumCompaniesWorked | 3 | 跳槽次数: **3次** |

---

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Windows/Mac/Linux

### 1. 克隆仓库

```bash
git clone https://github.com/zhongjinwen/IBM_HR_Analytics_Chinese.git
cd IBM_HR_Analytics_Chinese
注意：本仓库已包含原始数据文件 data/WA_Fn-UseC_-HR-Employee-Attrition.csv，可直接使用。

2. 创建虚拟环境
bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. 安装依赖
bash
pip install pandas
4. 选择版本运行
运行 v4.0（推荐 - 本土化优化版）
bash
python src/translate_data_v4.py
运行 v3.0（官方修正版）
bash
python src/translate_data_v3.py
运行 v2.0（增强汉化版）
bash
python src/translate_data_v2.py
运行 v1.0（基础版）
bash
python src/translate_data_v1.py
5. 输出文件
版本	输出文件	说明
v1.0	output/IBM_HR_员工流失数据_汉化版.csv	仅列名汉化
v2.0	output/IBM_HR_员工流失数据_全汉化版.csv	列名+变量值汉化
v3.0	output/IBM_HR_员工流失数据_官方修正版.csv	基于官方定义的精准汉化
v4.0	output/IBM_HR_员工流失数据_本土化版.csv	官方定义 + 本土化表达优化
📁 项目结构
text
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv    # 原始数据（已包含）
├── src/
│   ├── translate_data_v1.py                      # v1.0 仅列名汉化
│   ├── translate_data_v2.py                      # v2.0 完整汉化
│   ├── translate_data_v3.py                      # v3.0 官方修正版
│   └── translate_data_v4.py                      # v4.0 本土化优化版
├── output/                                        # 输出目录（运行后生成）
│   ├── IBM_HR_员工流失数据_汉化版.csv
│   ├── IBM_HR_员工流失数据_全汉化版.csv
│   ├── IBM_HR_员工流失数据_官方修正版.csv
│   └── IBM_HR_员工流失数据_本土化版.csv
├── .gitignore
├── LICENSE                                       # MIT License
├── DATA_LICENSE.md                                # 数据来源声明
└── README.md                                      # 本文档
📈 数据分析示例
python
import pandas as pd

# 读取 v4.0 本土化版数据
df = pd.read_csv('output/IBM_HR_员工流失数据_本土化版.csv')

# 查看不同岗位的离职率
job_attrition = df.groupby('岗位')['是否离职'].value_counts(normalize=True).unstack()
print(job_attrition)

# 查看敬业度与离职的关系
engagement_attrition = df.groupby('敬业度')['是否离职'].value_counts(normalize=True).unstack()
print(engagement_attrition)

# 查看跳槽次数分布
print(df['跳槽次数'].value_counts().sort_index())

# 查看调薪幅度与离职的关系
salary_hike_attrition = df.groupby('调薪幅度')['是否离职'].value_counts(normalize=True).unstack()
print(salary_hike_attrition)
🔄 版本对比
版本	字段名汉化	变量值汉化	基于官方定义	本土化表达	Excel友好
v1.0	✅	❌	❌	❌	✅
v2.0	✅	✅	❌	❌	✅
v3.0	✅	✅	✅	❌	✅
v4.0	✅	✅	✅	✅	✅
❓ 常见问题
Q: 应该使用哪个版本？
A:

推荐 v4.0：基于官方定义 + 本土化表达，最适合中文用户

v3.0：需要与英文原版严格对应时使用

v2.0：需要更完整汉化但不在意官方定义时使用

v1.0：只需要列名汉化时使用

Q: v4.0 的优化依据是什么？
A:

基于 Kaggle 原数据集官方定义保证数据准确性

参考国内HR领域的常用术语进行本土化优化

兼顾专业性和可读性

Q: 输出文件乱码怎么办？
A: 所有版本均使用 UTF-8 with BOM 编码，Excel 应能正常打开。如果仍有问题：

用记事本打开，另存为 ANSI 编码

或使用 VS Code 打开

Q: 提示找不到文件？
A: 确保 data/ 目录下有原始 CSV 文件。如缺失，可从 Kaggle 下载。

⚠️ 使用声明
数据来源: 本数据集源自 Kaggle 公开数据集，原始许可证为 DbCL v1.0

汉化说明: 字段名和分类变量已翻译为中文，数值型数据保持原值

准确性: v4.0 在保证官方定义准确性的基础上进行本土化优化

使用范围: 仅供学习和研究使用

📜 许可证
汉化版本: MIT License

原始数据: Open Data Commons Database Contents License (DbCL) v1.0

原始数据集版权归原作者所有。

📝 版本历史
版本	更新内容
v1.0	初始版本，列名汉化
v2.0	增加变量值汉化
v3.0	基于官方定义修正
v4.0	本土化表达优化
⭐ 支持项目
如果这个项目对你有帮助，欢迎给一个 Star ⭐

也欢迎提 Issue 或 PR 来改进翻译质量！