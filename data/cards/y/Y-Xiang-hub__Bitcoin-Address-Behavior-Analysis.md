# Y-Xiang-hub/Bitcoin-Address-Behavior-Analysis

⭐ 31 · Python · Apache-2.0 · 推送 2026-03-03 · [GitHub](https://github.com/Y-Xiang-hub/Bitcoin-Address-Behavior-Analysis) · [官网](https://doi.org/10.1109/TIFS.2023.3347894) · 组织维护

**比特币地址行为数据集 BABD-13 的构建与分析代码**

IEEE TIFS 论文 BABD 的配套源码：从 BTC.com 采集比特币账本数据（并共享高度 60 万至 60.6 万的 JSON 部分数据于 Kaggle），经 WalletExplorer API 获取带标签地址，用 graph-tool 生成交易图并抽取统计特征与局部结构特征（并行计算加速），预处理后合成 BABD-13.csv，再用 scikit-learn 与 xgboost 做特征选择与分类分析。面向区块链行为模式研究人员，运行依赖多个 Python 脚本与 notebook，README 未给出统一安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 账本采集→交易图生成→特征抽取→预处理→机器学习分析的完整流水线
- 统计特征与局部结构特征（子图）两类特征抽取，含并行计算
- 含 PAI/PDI/PTI/CI 四类地址行为指标定义（对应论文 Table II/III）
- 另提供 NetworkX 测试版以在小图上验证方法

## 适用场景

- 复现论文中 BABD-13 数据集的构建流程
- 基于比特币地址特征做分类与行为模式研究
- 扩展研究新的地址行为指标或图结构分析

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This project provides the source code for building BABD-13, accessible on Kaggle. The research paper, titled BABD: A
> L18: In the `data_collection` folder, `Bitcoin_Ledger_Reader_V3.1.py` is implemented for collecting Bitcoin ledger data 
> L38: We utilize the tools and models provided by scikit-learn and xgboost to analyze and study our data, i.e., `BABD-13.

## 星数曲线

```mermaid
xychart-beta
    title "Y-Xiang-hub/Bitcoin-Address-Behavior-Analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `74301f771c37` · [字段定义](../../DATASET.md)*
