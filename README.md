# IBM HR Analytics 员工流失数据集（汉化版）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的中文汉化版本。

原数据集包含1470名员工的信息，共35个字段，用于分析员工流失（Attrition）因素。

**本仓库已包含原始数据文件，无需额外下载。**

---

## 📊 数据说明

### 数据来源
- **原始数据集**: IBM HR Analytics Employee Attrition & Performance
- **来源平台**: [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **原始作者**: Pavan Subhash
- **原始许可证**: [Open Data Commons Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)
- **数据文件**: `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`

### 汉化字段对照表

| 英文原字段 | 中文字段名 | 说明 |
|-----------|-----------|------|
| Age | 年龄 | 员工年龄 |
| Attrition | 是否离职 | 目标变量（是/否）|
| BusinessTravel | 出差频率 | 出差情况 |
| Department | 部门 | 所属部门 |
| DistanceFromHome | 离家距离 | 通勤距离 |
| Education | 教育程度 | 学历水平 |
| EducationField | 教育领域 | 专业方向 |
| EnvironmentSatisfaction | 环境满意度 | 工作环境评价 |
| Gender | 性别 | 男/女 |
| JobInvolvement | 工作投入度 | 工作参与程度 |
| JobLevel | 职位等级 | 职级 |
| JobRole | 职位角色 | 具体岗位 |
| JobSatisfaction | 工作满意度 | 工作满意度评价 |
| MaritalStatus | 婚姻状况 | 单身/已婚/离异 |
| MonthlyIncome | 月收入 | 月薪金额 |
| NumCompaniesWorked | 曾工作公司数 | 工作经历 |
| OverTime | 是否加班 | 是/否 |
| PercentSalaryHike | 薪资涨幅百分比 | 涨薪比例 |
| PerformanceRating | 绩效评级 | 绩效评分 |
| RelationshipSatisfaction | 关系满意度 | 人际关系评价 |
| TotalWorkingYears | 总工作年限 | 工作经验 |
| WorkLifeBalance | 工作生活平衡 | 平衡度评价 |
| YearsAtCompany | 本公司工作年限 | 司龄 |
| YearsInCurrentRole | 现任职位年限 | 岗位年限 |
| YearsSinceLastPromotion | 上次晋升至今年限 | 晋升间隔 |

### 数据规模
- **样本数**: 1,470 条
- **特征数**: 35 个字段
- **目标变量**: 是否离职（237人离职，1233人留任）

---

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Windows/Mac/Linux

### 1. 克隆仓库（数据已包含，无需额外下载）

```bash
git clone https://github.com/zhongjinwen/IBM_HR_Analytics_Chinese.git
cd IBM_HR_Analytics_Chinese
```

&gt; **注意**：本仓库已包含原始数据文件 `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`，可直接使用。

### 2. 创建虚拟环境

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 检查目录结构

确保项目结构如下：
```
IBM-HR-Analytics-Chinese/
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv  ← 原始数据（已包含）
├── src/
│   └── translate_data.py
├── output/                                      ← 汉化结果（运行后生成）
├── venv/                                        ← 虚拟环境
├── requirements.txt
└── README.md
```

### 5. 运行汉化

```bash
python src/translate_data.py
```

**输出**: `output/IBM_HR_员工流失数据_汉化版.csv`

### 6. 使用数据

```python
import pandas as pd

# 读取汉化后的数据
df = pd.read_csv('output/IBM_HR_员工流失数据_汉化版.csv')

# 查看数据
print(df.head())
print(df.info())
```

---

## 📁 项目结构

```
├── data/                               # 原始数据（已包含，DbCL v1.0许可）
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── output/                             # 输出结果（运行后生成）
│   └── IBM_HR_员工流失数据_汉化版.csv
├── src/                                # 源代码
│   └── translate_data.py               # 汉化脚本
├── .gitignore                          # Git忽略配置
├── DATA_LICENSE.md                     # 数据来源声明
├── LICENSE                             # MIT License（汉化版本）
├── requirements.txt                    # 依赖列表
└── README.md                           # 项目说明
```

---

## 📈 简单分析示例

```python
import pandas as pd

# 读取数据
df = pd.read_csv('output/IBM_HR_员工流失数据_汉化版.csv')

# 离职率统计
attrition_rate = df['是否离职'].value_counts(normalize=True)
print(f"离职率: {attrition_rate['是']:.2%}")

# 按部门统计离职情况
pd.crosstab(df['部门'], df['是否离职'])

# 按性别统计
df.groupby('性别')['是否离职'].value_counts(normalize=True)
```

---

## 📝 技术细节

- **输出编码**: UTF-8 with BOM (`utf-8-sig`)，确保 Excel 打开中文不乱码
- **分隔符**: 逗号
- **行尾**: CRLF (Windows 格式)

---

## ❓ 常见问题

### Q: 提示 `FileNotFoundError: [Errno 2] No such file or directory`
**A**: 检查 `data/WA_Fn-UseC_-HR-Employee-Attrition.csv` 是否存在。如缺失，可从 [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 下载。

### Q: 提示 `ModuleNotFoundError: No module named 'pandas'`
**A**: 确保虚拟环境已激活（看到 `(venv)` 前缀），然后执行 `pip install -r requirements.txt`。

### Q: 汉化后的文件在哪里？
**A**: 在 `output/IBM_HR_员工流失数据_汉化版.csv`。

### Q: Excel 打开 CSV 中文乱码？
**A**: 本项目的输出使用 UTF-8 with BOM 编码，Excel 应能正常打开。如仍乱码，请使用记事本或 VS Code 打开。

---

## ⚠️ 使用声明

1. **数据来源**: 本数据集源自 Kaggle 公开数据集，原始许可证为 [Open Data Commons Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)
2. **汉化说明**: 字段名和分类变量已翻译为中文，数值型数据保持原值
3. **准确性**: 翻译力求准确，但可能存在歧义，建议对照原始数据使用
4. **使用范围**: 仅供学习和研究使用

---

## 📜 许可证

- **汉化版本**: [MIT License](LICENSE)
- **原始数据**: [Open Data Commons Database Contents License (DbCL) v1.0](DATA_LICENSE.md)

原始数据集版权归原作者所有。