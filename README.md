# IBM HR Analytics 员工流失数据集（汉化版 v3.0）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.5+-green.svg)

## 📋 项目简介

本项目是 [Kaggle IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) 数据集的**官方数据修正汉化版**。

原数据集包含1470名员工的信息，共35个字段，用于分析员工流失（Attrition）因素。

**✨ v3.0 核心特性：**
- ✅ **完全对照官方定义**：所有翻译基于 Kaggle 原数据集官方说明
- ✅ **字段名全中文**：35个字段全部翻译为中文
- ✅ **变量值精准翻译**：分类变量的值按官方定义精准汉化
- ✅ **Excel 友好**：UTF-8 with BOM 编码，直接打开不乱码
- ✅ **版本追溯**：保留 v1.0、v2.0、v3.0 完整版本

**本仓库已包含原始数据文件，无需额外下载。**

---

## 🔍 v3.0 重要修正说明

| 字段 | v2.0 翻译 | **v3.0 修正** | 官方定义 |
|------|-----------|---------------|----------|
| 教育程度 | 小学及以下/中学/专科/本科/硕士及以上 | **高中及以下/专科/本科/硕士/博士** | Below College, College, Bachelor, Master, Doctor |
| 环境满意度 | 非常不满意/不满意/一般/满意 | **低/中/高/非常高** | Low, Medium, High, Very High |
| 工作满意度 | 非常不满意/不满意/一般/满意 | **低/中/高/非常高** | Low, Medium, High, Very High |
| 关系满意度 | 非常不满意/不满意/一般/满意 | **低/中/高/非常高** | Low, Medium, High, Very High |
| 工作生活平衡 | 非常差/较差/一般/较好 | **差/好/更好/最好** | Bad, Good, Better, Best |
| 工作投入度 | 非常低/低/一般/高 | **低/中/高/非常高** | Low, Medium, High, Very High |
| 绩效评级 | 低/良好/优秀/卓越 | **低/良好/优秀/杰出** | Low, Good, Excellent, Outstanding |

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

### 汉化效果对比

| 原字段 | 原值 | v2.0 | **v3.0（官方修正）** |
|--------|------|------|---------------------|
| Education | 1 | 小学及以下 | **高中及以下** |
| Education | 5 | 硕士及以上 | **博士** |
| EnvironmentSatisfaction | 4 | 满意 | **非常高** |
| WorkLifeBalance | 1 | 非常差 | **差** |
| PerformanceRating | 4 | 卓越 | **杰出** |

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
运行 v3.0（推荐 - 官方修正版）
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
📁 项目结构
text
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv    # 原始数据（已包含）
├── src/
│   ├── translate_data_v1.py                      # v1.0 仅列名汉化
│   ├── translate_data_v2.py                      # v2.0 完整汉化
│   └── translate_data_v3.py                      # v3.0 官方修正版
├── output/                                        # 输出目录（运行后生成）
│   ├── IBM_HR_员工流失数据_汉化版.csv
│   ├── IBM_HR_员工流失数据_全汉化版.csv
│   └── IBM_HR_员工流失数据_官方修正版.csv
├── .gitignore
├── LICENSE                                       # MIT License
├── DATA_LICENSE.md                                # 数据来源声明
└── README.md                                      # 本文档
📈 数据分析示例
python
import pandas as pd

# 读取 v3.0 官方修正版数据
df = pd.read_csv('output/IBM_HR_员工流失数据_官方修正版.csv')

# 查看各教育程度的离职率
edu_attrition = df.groupby('教育程度')['是否离职'].value_counts(normalize=True).unstack()
print(edu_attrition)

# 查看工作生活平衡与离职的关系
balance_attrition = df.groupby('工作生活平衡')['是否离职'].value_counts(normalize=True).unstack()
print(balance_attrition)

# 绩效评级分布
print(df['绩效评级'].value_counts())
🔄 版本对比
特性	v1.0	v2.0	v3.0
字段名汉化	✅	✅	✅
变量值汉化	❌	✅	✅
基于官方定义	❌	❌	✅
教育程度准确定义	❌	❌	✅
满意度标准翻译	❌	❌	✅
Excel 友好编码	✅	✅	✅
❓ 常见问题
Q: 应该使用哪个版本？
A:

推荐 v3.0：基于官方定义，最准确

需要与英文原版对照：可用 v2.0 或 v1.0

教学演示：v3.0 更符合中文表达习惯

Q: v3.0 的修改依据是什么？
A: 完全依据 Kaggle 原数据集页面的官方说明：

IBM HR Analytics Employee Attrition & Performance

Q: 输出文件乱码怎么办？
A: 所有版本均使用 UTF-8 with BOM 编码，Excel 应能正常打开。如果仍有问题：

用记事本打开，另存为 ANSI 编码

或使用 VS Code 打开

Q: 提示找不到文件？
A: 确保 data/ 目录下有原始 CSV 文件。如缺失，可从 Kaggle 下载。

⚠️ 使用声明
数据来源: 本数据集源自 Kaggle 公开数据集，原始许可证为 DbCL v1.0

汉化说明: 字段名和分类变量已翻译为中文，数值型数据保持原值

准确性: v3.0 严格按照官方定义翻译，如有疑问请参考原始数据

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
⭐ 支持项目
如果这个项目对你有帮助，欢迎给一个 Star ⭐

也欢迎提 Issue 或 PR 来改进翻译质量！