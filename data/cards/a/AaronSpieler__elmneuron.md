# AaronSpieler/elmneuron

⭐ 17 · Jupyter Notebook · MIT · 推送 2026-10-29 · [GitHub](https://github.com/AaronSpieler/elmneuron) · 个人维护

**ELM 神经元模型的 PyTorch 最小实现，复现论文核心结果**

提供（Branch）Expressive Leaky Memory neuron 的 PyTorch 最小实现，用于复现论文在 NeuronIO、SHD/SHD-Adding 数据集上的核心结果；附带多尺寸预训练模型（AUC 0.94-0.9946）与训练/评估 notebook。作者指出本仓库非最优版本（最优版为 JAX 的 elmnetwork），PyTorch 版慢约 2 倍，并明确列出已知问题：浅拷贝导致保存的 best model 实为最终 epoch 模型（含预训练模型）、NeuronIO 训练需先下载约 115GB 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供多尺寸预训练 Branch-ELM 模型（d_m=1~100）
- 含 NeuronIO、SHD/SHD-Adding 训练与评估 notebook
- v2 实现改进时间尺度处理，推荐用于新项目
- README 列出已知实现问题及论文勘误

## 适用场景

- 复现 ELM 神经元论文的核心实验结果
- 在 NeuronIO/SHD 数据集上训练评估现象学神经元模型
- 将 ELM 神经元用于新的长时程序列建模项目

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: This repository features a minimal implementation of the (Branch) Expressive Leaky Memory neuron in PyTorch.
> L6: Notebooks to train and evaluate on NeuronIO are provided, as well as pre-trained models of various sizes.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `63a43efb4876` · [字段定义](../../DATASET.md)*
