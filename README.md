# IBM HR Analytics 员工流失数据集（汉化版 v4.0）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.5+-green.svg)

## 📋 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的**本土化优化汉化版**。

原数据集包含1470名员工的信息，共35个字段，用于分析员工流失（Attrition）因素。

免责声明：本代码处理的是公开数据集，不涉及真实员工信息。

**✨ v4.0 核心特性：**
- ✅ **完全对照官方定义**：所有翻译基于 Kaggle 原数据集官方说明
- ✅ **本土化表达优化**：采用更符合中文HR领域的术语
- ✅ **字段名全中文**：35个字段全部翻译为中文
- ✅ **变量值精准翻译**：分类变量的值按官方定义精准汉化
- ✅ **Excel 友好**：UTF-8 with BOM 编码，直接打开不乱码

**本仓库已包含原始数据文件，无需额外下载。**

---

## 🔍 v4.0 本土化优化说明

| 原字段 | v3.0 翻译 | v4.0 优化 | 优化理由 |
|:--------|:-----------|:-----------|:----------|
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

| 原字段 | 原值 | v4.0 翻译 |
|:--------|:------|:-----------|
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
版本	命令	说明
v4.0	python src/translate_data_v4.py	推荐：本土化优化版
v3.0	python src/translate_data_v3.py	官方修正版
v2.0	python src/translate_data_v2.py	增强汉化版
v1.0	python src/translate_data_v1.py	基础版
5. 输出文件
版本	输出文件	说明
v1.0	output/IBM_HR_员工流失数据_汉化版.csv	仅列名汉化
v2.0	output/IBM_HR_员工流失数据_全汉化版.csv	列名+变量值汉化
v3.0	output/IBM_HR_员工流失数据_官方修正版.csv	基于官方定义
v4.0	output/IBM_HR_员工流失数据_本土化版.csv	官方定义+本土化优化
📁 项目结构
text
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── src/
│   ├── translate_data_v1.py
│   ├── translate_data_v2.py
│   ├── translate_data_v3.py
│   └── translate_data_v4.py
├── output/
├── .gitignore
├── LICENSE
├── DATA_LICENSE.md
└── README.md
📈 数据分析示例
python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 v4.0 数据
df = pd.read_csv('output/IBM_HR_员工流失数据_本土化版.csv')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 不同岗位的离职率
print("=== 各岗位离职率 ===")
job_attrition = df.groupby('岗位')['是否离职'].value_counts(normalize=True).unstack()
print(job_attrition)

# 2. 敬业度与离职的关系
print("\n=== 敬业度与离职 ===")
engagement_attrition = df.groupby('敬业度')['是否离职'].value_counts(normalize=True).unstack()
print(engagement_attrition)

# 3. 跳槽次数分布
print("\n=== 跳槽次数分布 ===")
print(df['跳槽次数'].value_counts().sort_index())

# 4. 调薪幅度与离职
print("\n=== 调薪幅度与离职 ===")
hike_attrition = df.groupby('调薪幅度')['是否离职'].value_counts(normalize=True).unstack()
print(hike_attrition)

# 5. 可视化：工作与生活平衡 vs 离职
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='工作与生活平衡', hue='是否离职')
plt.title('工作与生活平衡与离职关系')
plt.show()
## 🔄 版本功能对比

### 📊 各版本功能一览

**v1.0（基础版）**
- ✨ 字段名汉化：✅
- 🔤 变量值汉化：❌
- 📖 基于官方定义：❌
- 🎯 本土化优化：❌
- 📁 Excel友好：✅

**v2.0（增强汉化版）**
- ✨ 字段名汉化：✅
- 🔤 变量值汉化：✅
- 📖 基于官方定义：❌
- 🎯 本土化优化：❌
- 📁 Excel友好：✅

**v3.0（官方修正版）**
- ✨ 字段名汉化：✅
- 🔤 变量值汉化：✅
- 📖 基于官方定义：✅
- 🎯 本土化优化：❌
- 📁 Excel友好：✅

**v4.0（本土化优化版）- ⭐ 推荐**
- ✨ 字段名汉化：✅
- 🔤 变量值汉化：✅
- 📖 基于官方定义：✅
- 🎯 本土化优化：✅
- 📁 Excel友好：✅

---

### 💡 版本选择建议

#### 🔹 中文用户日常分析
**推荐版本：v4.0**
- 最符合中文HR用语习惯
- 既有官方定义的准确性，又进行了本土化优化

#### 🔹 需要严格对照英文原版
**推荐版本：v3.0**
- 完全基于官方定义
- 术语准确，便于中英文对照

#### 🔹 只需要字段名是中文
**推荐版本：v2.0**
- 变量值保留英文
- 适合教学中让学生对照学习

#### 🔹 基础教学演示
**推荐版本：v1.0**
- 简单明了
- 适合展示基本的列名汉化功能

---

### 📋 功能对比总结

| 版本 | 字段名汉化 | 变量值汉化 | 官方定义依据 | 本土化优化 | Excel友好 |
|:----:|:----------:|:----------:|:------------:|:----------:|:---------:|
| v1.0 |     ✓      |     ✗      |      ✗       |     ✗      |     ✓     |
| v2.0 |     ✓      |     ✓      |      ✗       |     ✗      |     ✓     |
| v3.0 |     ✓      |     ✓      |      ✓       |     ✗      |     ✓     |
| v4.0 |     ✓      |     ✓      |      ✓       |     ✓      |     ✓     |

✓ 支持　✗ 不支持

### ⭐ 总结
- **日常使用**：选择 v4.0
- **对照学习**：选择 v3.0
- **教学演示**：选择 v2.0 或 v1.0
❓ 常见问题
Q: 应该使用哪个版本？
A: 根据您的需求选择：

v4.0（推荐）：最适合中文用户，既有官方定义的准确性，又符合国内HR用语习惯

v3.0：需要与英文原版严格对照时使用

v2.0：只需要完整汉化，不关心官方定义时使用

v1.0：只需要列名是中文，变量值保持英文时使用

Q: v4.0 相比 v3.0 有哪些优化？
A: v4.0 在 v3.0 的基础上进行了本土化表达优化：

优化项	v3.0	v4.0
JobRole	职位角色	岗位
JobLevel	职位等级	职级
JobInvolvement	工作投入度	敬业度
JobSatisfaction	工作满意度	工作满意
WorkLifeBalance	工作生活平衡	工作与生活平衡
PercentSalaryHike	薪资涨幅百分比	调薪幅度
StockOptionLevel	股票期权等级	股权激励等级
TotalWorkingYears	总工作年限	总工龄
YearsAtCompany	本公司工作年限	本企业工龄
YearsInCurrentRole	现任职位年限	现岗年限
YearsSinceLastPromotion	上次晋升至今年限	晋升间隔
NumCompaniesWorked	曾工作公司数	跳槽次数
EnvironmentSatisfaction	环境满意度	环境满意
RelationshipSatisfaction	关系满意度	人际关系满意
TrainingTimesLastYear	去年培训次数	年度培训次数
Q: 输出文件乱码怎么办？
A: 所有版本均使用 UTF-8 with BOM 编码，Excel 可直接打开。如仍有问题：

用记事本打开，另存为 ANSI 编码

或使用 VS Code、记事本++等编辑器打开

Q: 提示找不到文件？
A: 确保目录结构正确：

text
项目根目录/
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
└── src/
    └── translate_data_v4.py
如缺失数据文件，可从 Kaggle 下载。

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