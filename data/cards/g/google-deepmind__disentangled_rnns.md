# google-deepmind/disentangled_rnns

⭐ 46 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/google-deepmind/disentangled_rnns) · [官网](https://openreview.net/pdf?id=SOEF0i0G1z) · 组织维护

**面向科研的 DisRNN 认知模型发现代码库：拟合行为与神经数据**

Disentangled RNN（DisRNN）是一种循环神经网络架构，用于发现与数据集一致的、可解释的动力学系统：通过少量携带独立信息、稀疏更新的潜变量来鼓励模型简单性。代码支持生成合成数据集、打包实验室数据、以不同超参数训练 DisRNN 与标准 RNN，并检查拟合后的网络；另提供多被试 DisRNN 拟合个体策略异同。以 JAX/Haiku 实现，提供多个可在 Google Colab 中运行的 ipynb notebook（建议连接 GPU/TPU），也可经 conda 环境、pip 安装在本地运行，并用 example.py 测试安装。适用于做学习与决策任务认知建模的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DisRNN 架构以少量独立、稀疏更新的潜变量获得可解释模型
- 支持合成数据生成、实验室数据打包、DisRNN 与标准 RNN 训练与拟合检查
- Multisubject DisRNN 用单一网络拟多个体的认知策略异同
- 提供 Colab notebooks 与本地 conda/pip 安装流程

## 适用场景

- 对人类或动物的学习决策行为数据拟合可解释的认知模型
- 生成合成数据集并比较 DisRNN 与 GRU 等 RNN 的拟合
- 研究个体间认知策略差异的多被试建模

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Disentangled RNN (DisRNN) is a recurrent neural network architecture designed
> L14: The code here allows generating synthetic datasets, packaging laboratory

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/disentangled_rnns 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-25 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f1c0f1e8e197` · [字段定义](../../DATASET.md)*
