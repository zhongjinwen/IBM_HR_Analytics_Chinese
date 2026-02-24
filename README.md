# IBM HR Analytics 员工流失数据集（汉化版 v5.0）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.2+-green.svg)](https://pandas.pydata.org/)

---

## 目录

- [项目简介](#项目简介)
- [核心特性](#核心特性)
- [快速开始](#快速开始)
- [项目结构](#项目结构)
- [数据说明](#数据说明)
- [版本历史](#版本历史)
- [使用声明](#使用声明)
- [许可证](#许可证)
- [贡献与支持](#贡献与支持)
- [后续计划](#后续计划)

---

## 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的本土化优化汉化版本。

原数据集包含 **1,470 名员工**的信息，共 **35 个字段**，用于分析员工流失因素。这是由 IBM 数据科学家创建的**虚构数据集**，不涉及任何真实员工信息，可放心用于学习和研究。

> **注意**：本仓库已包含原始数据文件（`data/WA_Fn-UseC_-HR-Employee-Attrition.csv`），无需额外下载。

根据原始数据的 [DbCL v1.0 许可证](https://opendatacommons.org/licenses/dbcl/1-0/)，您可以自由使用、分享此数据（包括商业用途），但需遵守许可证条款。

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **官方定义对照** | 所有翻译基于 Kaggle 原数据集官方说明 |
| **本土化表达** | 采用符合中文 HR 领域的术语，如"岗位"替代"职位角色"、"学历"替代"教育程度" |
| **字段全中文** | 35 个字段全部翻译为中文 |
| **变量值精准翻译** | 分类变量按官方定义精准汉化（学历：1→大专以下，2→大专，3→本科，4→硕士，5→博士） |
| **智能编码列** | 为不同类型变量添加编码列：<br>- 有序分类变量（学历、满意度等）保留原始数值编码列<br>- 二元变量（是否离职、是否加班）添加 0/1 编码列<br>- 无序分类变量（婚姻状况、出差频率）添加因子化编码列<br>- 职级（数值型）和是否成年（常数列）不添加编码列 |
| **百分比格式** | 调薪幅度除以 100 并设置为不带小数的百分比格式（如 11%） |
| **Excel 友好** | 输出为格式化的 Excel 文件，包含：<br>- 数据自动转换为**超级表**（表格名称 `HRDATA`），支持筛选和样式<br>- **蓝色主题**：标题行深蓝背景、白色加粗微软雅黑，数据行微软雅黑居中<br>- **自动列宽**：根据内容自适应，最大宽度 30<br>- **列顺序优化**：按国内 HR 阅读习惯排列，员工编号为首列 |

---

## 快速开始

### 环境要求

- Python 3.9 或更高版本

### 安装依赖

**基础功能（数据汉化）**：

```bash
pip install pandas openpyxl
```

**完整分析功能（含机器学习建模、可视化及报告生成）推荐使用国内镜像加速**：

```bash
pip install pandas openpyxl plotly kaleido matplotlib seaborn scikit-learn python-docx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

或使用项目提供的 `requirements.txt` 一键安装：

```bash
pip install -r requirements.txt
```

### 使用步骤

1. **克隆仓库**

   ```bash
   git clone https://github.com/zhongjinwen/IBM_HR_Analytics_Chinese.git
   cd IBM_HR_Analytics_Chinese
   ```

2. **运行汉化脚本（v5.0）**

   ```bash
   python src/translate_data_v5.py
   ```

3. **运行分析脚本（可选）**

   ```bash
   cd analysis/src
   python full_analysis_report.py
   ```

4. **获取输出文件**

   - 汉化数据集：`output/IBM_HR_员工流失数据_本土化版.xlsx`
   - 分析结果：`analysis/output/` 目录下的图表、Word 报告、Excel 风险表

---

## 项目结构

```
.
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv      # 原始数据文件
├── src/
│   └── translate_data_v5.py                       # 汉化脚本 v5.0
├── analysis/                                      # 分析代码（v6.0+）
│   └── src/
│       └── full_analysis_report.py                # 综合分析脚本
├── output/                                        # 汉化生成的 Excel 文件
│   └── IBM_HR_员工流失数据_本土化版.xlsx
├── .gitignore                                     # Git 忽略配置
├── LICENSE                                        # MIT 许可证
├── DATA_LICENSE.md                                # 原始数据许可证（DbCL v1.0）
├── README.md                                      # 本文件
└── requirements.txt                               # 依赖列表
```

---

## 数据说明

### 数据规模

| 指标 | 数值 |
|------|------|
| 样本数 | 1,470 条 |
| 特征数 | 35 个字段 |
| 目标变量 | 是否离职（237 人离职，1,233 人留任） |

生成的 Excel 文件中，超级表 `HRDATA` 包含所有汉化字段及编码列，可直接用于数据透视、图表分析和机器学习建模。

### 翻译效果示例

| 原字段 | 原值 | v5.0 翻译 |
|--------|------|-----------|
| `Attrition` | Yes | 是否离职: 是 |
| `JobRole` | Sales Executive | 岗位: 销售主管 |
| `Education` | 1 | 学历: 大专以下 |
| `EducationField` | Life Sciences | 专业: 生命科学 |
| `WorkLifeBalance` | 1 | 工作与生活平衡: 差 |
| `PercentSalaryHike` | 15 | 调薪幅度: 15% |
| `NumCompaniesWorked` | 3 | 跳槽次数: 3 次 |
| `MaritalStatus` | Married | 婚姻状况: 已婚（编码列对应数值） |
| `BusinessTravel` | Travel_Rarely | 出差频率: 偶尔出差（编码列对应数值） |

---

## 版本历史

| 版本 | 主要更新 |
|------|----------|
| **v5.0** | 输出格式化 Excel，优化术语，智能编码列，调薪幅度百分比格式，员工编号首列 |
| v4.0 | 本土化表达优化 |
| v3.0 | 基于官方定义修正 |
| v2.0 | 增加变量值汉化 |
| v1.0 | 初始版本，列名汉化 |

---

## 使用声明

### 免责声明

- **数据虚构性**：本数据集由 IBM 数据科学家创建，完全为虚构数据，不涉及任何真实员工个人信息，可安全用于学习、研究和演示。
- **原始数据来源**：数据集源自 Kaggle 公开平台，原始版权归原作者所有。
- **汉化版本**：本仓库提供的汉化脚本和文档仅出于方便中文用户的目的，不保证翻译的绝对准确性，使用者应自行核对。

---

## 许可证

| 项目 | 许可证 |
|------|--------|
| 汉化版本（脚本与文档） | [MIT License](./LICENSE.md) |
| 原始数据 | [Open Data Commons Database Contents License (DbCL) v1.0](./DATA_LICENSE.md) |

根据此许可证，您可以自由使用、修改和分享数据内容（包括商业用途），但必须遵守许可证条款。

---

## 贡献与支持

欢迎通过以下方式参与本项目：

- **提交 Issue**：报告问题或提出改进建议
- **提交 Pull Request**：改进翻译质量或添加新功能
- **Star 支持**：如果本项目对您有帮助，欢迎点亮 Star

---

## 后续计划

**v6.0** 将基于此汉化数据集开发一系列分析代码，包括：

- 员工基本画像分析（年龄、性别、婚姻、学历分布）
- 不同分类的流失分析（部门、岗位、学历等维度）
- 薪酬公平性分析（月收入与岗位、职级的关系）
- 员工生命周期价值分析（工龄与薪酬、晋升的关联）
- 职业发展路径分析（培训次数、晋升间隔对离职的影响）
- 离职预测决策系统（机器学习建模及可视化报告）

分析脚本位于 `analysis/src/full_analysis_report.py`，可生成完整的 Word 报告和 Excel 风险表。

---

<p align="center"><a href="#目录">返回顶部</a></p>
