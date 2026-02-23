# IBM HR Analytics 员工流失数据集（汉化版 v2.0）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.5+-green.svg)

## 📋 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的**完整汉化版本**。

原数据集包含1470名员工的信息，共35个字段，用于分析员工流失（Attrition）因素。

**✨ v2.0 增强特性：**
- ✅ **字段名全中文**：35个字段全部翻译为中文
- ✅ **变量值全翻译**：分类变量的值也翻译为中文（如 `Yes/No` → `是/否`）
- ✅ **Excel 友好**：UTF-8 with BOM 编码，直接打开不乱码
- ✅ **一键运行**：提供完整的 Python 脚本，自动生成汉化文件

**本仓库已包含原始数据文件，无需额外下载。**

---

## 📊 数据说明

### 数据来源
- **原始数据集**: IBM HR Analytics Employee Attrition & Performance
- **来源平台**: [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **原始作者**: Pavan Subhash
- **原始许可证**: [Open Data Commons Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)
- **数据文件**: `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`

### 汉化效果示例

| 原字段 | 原值 | v2.0 汉化结果 |
|--------|------|---------------|
| Attrition | Yes | 是否离职: **是** |
| BusinessTravel | Travel_Rarely | 出差频率: **偶尔出差** |
| Education | 1 | 教育程度: **小学及以下** |
| Gender | Male | 性别: **男** |
| OverTime | Yes | 是否加班: **是** |

### 数据规模
- **样本数**: 1,470 条
- **特征数**: 35 个字段
- **目标变量**: 是否离职（237人离职，1233人留任）

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
4. 运行汉化脚本（v2.0）
bash
python src/translate_data_v2.py
输出文件: output/IBM_HR_员工流失数据_全汉化版.csv

5. 使用数据
python
import pandas as pd

# 读取汉化后的数据
df = pd.read_csv('output/IBM_HR_员工流失数据_全汉化版.csv')

# 查看数据
print(df.head())
print(df.info())
📁 项目结构
text
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv    # 原始数据（已包含）
├── src/
│   ├── translate_data_v1.py                      # 初版脚本（列名汉化）
│   └── translate_data_v2.py                      # v2.0 脚本（完整汉化）
├── output/                                        # 输出目录（运行后生成）
│   └── IBM_HR_员工流失数据_全汉化版.csv
├── .gitignore
├── LICENSE                                       # MIT License
├── DATA_LICENSE.md                                # 数据来源声明
└── README.md                                      # 本文档
📈 简单分析示例
python
import pandas as pd

df = pd.read_csv('output/IBM_HR_员工流失数据_全汉化版.csv')

# 离职率统计
attrition_rate = df['是否离职'].value_counts(normalize=True)
print(f"离职率: {attrition_rate['是']:.2%}")

# 按部门统计离职情况
print(pd.crosstab(df['部门'], df['是否离职']))

# 按性别统计
print(df.groupby('性别')['是否离职'].value_counts(normalize=True))
🔄 版本说明
v2.0 (当前版本)
字段名汉化：35个字段全部翻译为中文

变量值汉化：所有分类变量的值均翻译为中文

Excel友好：UTF-8 with BOM 编码

完整脚本：提供一键运行脚本

v1.0
基础版本，仅翻译列名

变量值保持原样

❓ 常见问题
Q: 提示找不到文件？
A: 确保 data/ 目录下有原始 CSV 文件。如缺失，可从 Kaggle 下载。

Q: 如何区分 v1.0 和 v2.0？
A:

translate_data_v1.py: 仅翻译列名

translate_data_v2.py: 同时翻译列名和变量值

Q: Excel 打开乱码？
A: v2.0 输出使用 UTF-8 with BOM 编码，Excel 应能正常打开。如仍乱码，请用记事本或 VS Code 打开。

Q: 提示 ModuleNotFoundError: No module named 'pandas'
A: 确保虚拟环境已激活（看到 (venv) 前缀），然后执行 pip install pandas。

⚠️ 使用声明
数据来源: 本数据集源自 Kaggle 公开数据集，原始许可证为 DbCL v1.0

汉化说明: 字段名和分类变量已翻译为中文，数值型数据保持原值

准确性: 翻译力求准确，但可能存在歧义，建议对照原始数据使用

使用范围: 仅供学习和研究使用

📜 许可证
汉化版本: MIT License

原始数据: Open Data Commons Database Contents License (DbCL) v1.0

原始数据集版权归原作者所有。

⭐ 支持项目
如果这个项目对你有帮助，欢迎给一个 Star ⭐

也欢迎提 Issue 或 PR 来改进翻译质量！

