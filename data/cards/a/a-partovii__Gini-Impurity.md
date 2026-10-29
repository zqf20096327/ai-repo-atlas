# a-partovii/Gini-Impurity

⭐ 80 · Python · 推送 2025-11-02 · [GitHub](https://github.com/a-partovii/Gini-Impurity) · 个人维护

**计算关系型数据各特征基尼不纯度的 Python 教学脚本**

提供两个版本的 Python 脚本：对给定关系型数据集的每个特征列及其取值计算基尼不纯度。Classic 版以数据集最后一列作为标签，仅支持 'yes'/'no' 标签；Evolved 版可指定任意特征及其取值作为标签目标。输入需为 Excel 或 CSV 文件，路径写入脚本内的 file_path 变量。依赖 Python 3.x 与 pandas、termcolor 库。本项目为大学课程的练习项目，README 声明不适用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对每个特征列及其取值计算基尼不纯度
- Classic 版支持 yes/no 二分类标签，Evolved 版支持用户指定目标标签
- 读取 Excel（.xlsx/.xls）与 CSV 文件

## 适用场景

- 特征选择与数据预处理时计算基尼不纯度
- 学习决策树构建中基尼指标的入门概念
- 基础数据分析课程练习

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This project provides implementations for calculating Gini Impurity. The scripts compute the Gini Impurity for each 
> L23: It is part of a practice project assigned by a university professor, designed to help students learn basic data ana

## 星数曲线

```mermaid
xychart-beta
    title "a-partovii/Gini-Impurity 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-29 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1d291e2b2765` · [字段定义](../../DATASET.md)*
