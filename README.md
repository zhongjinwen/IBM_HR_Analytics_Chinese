# IBM HR Analytics 员工流失数据集（汉化版 v5.0）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-2.2+-green.svg)
![Openpyxl](https://img.shields.io/badge/openpyxl-3.1+-orange.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/zhongjinwen/IBM_HR_Analytics_Chinese)
![GitHub repo size](https://img.shields.io/github/repo-size/zhongjinwen/IBM_HR_Analytics_Chinese)

---

## 📋 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的**本土化优化汉化版 v5.0**。原数据集由 IBM 数据科学家创建，包含 1470 名员工的信息，共 35 个字段，用于分析员工流失因素。

> **重要声明**：本数据集为**完全虚构数据**，不涉及任何真实员工个人信息，可安全用于学习和研究。

**本仓库已包含原始数据文件**（`data/WA_Fn-UseC_-HR-Employee-Attrition.csv`），您无需额外下载。根据原始数据的 [DbCL v1.0 许可证](https://opendatacommons.org/licenses/dbcl/1-0/)，您可以自由使用、分享此数据（包括商业用途），但需遵守许可证条款。

---

## ✨ v5.0 核心特性

| 特性 | 说明 |
|:-----|:-----|
| ✅ **完全对照官方定义** | 所有翻译基于 Kaggle 原数据集官方说明 |
| ✅ **本土化表达优化** | 采用更符合中文HR领域的术语（“岗位”替代“职位角色”、“专业”替代“教育领域”） |
| ✅ **字段名全中文** | 35个字段全部翻译为中文 |
| ✅ **变量值精准翻译** | 分类变量按官方定义精准汉化（教育程度：1→大专以下，2→大专，3→本科，4→硕士，5→博士） |
| ✅ **Excel 友好** | 输出为格式化的 Excel 文件，包含：<br>• 数据自动转换为**超级表**（表格名称 `HRDATA`），支持筛选和样式<br>• **蓝色主题**：标题行深蓝背景、白色加粗微软雅黑，数据行微软雅黑居中<br>• **自动列宽**：根据内容自适应，最大宽度 30<br>• **编码列**：为所有数值型分类变量保留原始数值编码列（如“教育程度编码”），便于 Excel 透视和建模<br>• **列顺序优化**：按国内HR阅读习惯排列，员工编号为首列 |

---

## 🚀 快速开始

### 环境要求

- Python 3.9 或更高版本
- 依赖库：pandas、openpyxl

### 安装依赖

```bash
pip install pandas openpyxl

使用步骤
克隆仓库

bash
git clone https://github.com/zhongjinwen/IBM_HR_Analytics_Chinese.git
cd IBM_HR_Analytics_Chinese

运行汉化脚本

bash
python src/translate_data_v5.py

获取输出文件

脚本运行后，在 output/ 目录下生成：

IBM_HR_员工流失数据_本土化版.xlsx —— 可直接用 Excel 打开的汉化数据集

📁 项目结构
text
.
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv    # 原始数据文件
├── src/
│   └── translate_data_v5.py                      # 汉化脚本 v5.0
├── output/
│   └── IBM_HR_员工流失数据_本土化版.xlsx         # 生成的 Excel 文件
├── .gitignore                                     # Git 忽略配置
├── LICENSE                                        # MIT 许可证
├── DATA_LICENSE.md                                # 原始数据许可证（DbCL v1.0）
└── README.md                                      # 本文件

📊 数据说明
数据规模
样本数：1,470 条

特征数：35 个字段

目标变量：是否离职（237人离职，1233人留任）

翻译效果示例
原字段	原值	v5.0 翻译
Attrition	Yes	是否离职: 是
JobRole	Sales Executive	岗位: 销售主管
Education	1	教育程度: 大专以下
EducationField	Life Sciences	专业: 生命科学
WorkLifeBalance	1	工作与生活平衡: 差
PercentSalaryHike	15	调薪幅度: 15%
NumCompaniesWorked	3	跳槽次数: 3次
生成的 Excel 文件中，超级表 HRDATA 包含所有汉化字段及编码列，可直接用于数据透视、图表分析和机器学习建模。

🔄 版本历史
版本	主要更新
v5.0	输出格式化 Excel（超级表、蓝色主题、自动列宽、编码列），教育程度 1→大专以下，教育领域→专业，员工编号首列
v4.0	本土化表达优化
v3.0	基于官方定义修正
v2.0	增加变量值汉化
v1.0	初始版本，列名汉化

⚠️ 使用声明
免责声明
数据虚构性：本数据集由 IBM 数据科学家创建，完全为虚构数据，不涉及任何真实员工个人信息，可安全用于学习、研究和演示。

原始数据来源：数据集源自 Kaggle 公开平台，原始版权归原作者所有。

汉化版本：本仓库提供的汉化脚本和文档仅出于方便中文用户的目的，不保证翻译的绝对准确性，使用者应自行核对。

许可证
汉化版本（脚本与文档）：遵循 MIT License

原始数据：遵循 Open Data Commons Database Contents License (DbCL) v1.0

根据此许可证，您可以自由使用、修改和分享数据内容（包括商业用途），但必须遵守许可证条款。

⭐ 支持项目
如果这个项目对你有帮助，欢迎给一个 Star ⭐，也欢迎提 Issue 或 PR 来改进翻译质量！

📌 后续计划
v6.0 将基于此汉化数据集开发一系列分析代码，包括：

员工基本画像分析（年龄、性别、婚姻、教育分布）

不同分类的流失分析（部门、岗位、教育等维度）

薪酬公平性分析（月收入与岗位、职级的关系）

员工生命周期价值分析（工龄与薪酬、晋升的关联）

职业发展路径分析（培训次数、晋升间隔对离职的影响）

离职预测决策系统（机器学习建模及可视化报告）

敬请期待！