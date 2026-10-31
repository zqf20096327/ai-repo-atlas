# jzzh123/RC-Flow

⭐ 19 · Python · 推送 2026-01-29 · [GitHub](https://github.com/jzzh123/RC-Flow) · [官网](https://arxiv.org/abs/2601.15767) · 个人维护

**论文代码：基于流匹配的 MIMO 信道估计算法 RC-Flow**

论文《Recursive Flow: A Generative Framework for MIMO Channel Estimation》的 Python 实现仓库，属于生成式模型在信道估计中的应用。仓库提供训练流骨干网络的 train_flow.py、可直接运行得到结果的 test_rcflow.py、数据加载器 loaders.py、预训练模型目录 results 与信道数据目录 bin；信道数据需从外部仓库 score-based-channels 获取。附论文 PDF 与 BibTeX 引用信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供训练脚本 train_flow.py 与可直接运行的测试脚本 test_rcflow.py
- 附带预训练模型（results 目录）
- 基于流匹配（flow matching）的生成式信道估计框架

## 适用场景

- 复现 MIMO 信道估计论文实验结果
- 在预训练模型基础上做信道估计测试
- 研究流匹配方法在通信信道估计中的应用

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L2: This repository is the Python implementation of paper _"Recursive Flow: A Generative Framework for MIMO Channel Esti
> L11: `test_rcflow.py`: The test function. Can be directly run to get the results.

## 星数曲线

```mermaid
xychart-beta
    title "jzzh123/RC-Flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `87d5f8a135b7` · [字段定义](../../DATASET.md)*
