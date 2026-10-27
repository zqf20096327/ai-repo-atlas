# MANDO-Project/ge-sc

⭐ 35 · Solidity · MIT · 推送 2026-04-13 · [GitHub](https://github.com/MANDO-Project/ge-sc) · 组织维护

**基于异构图神经网络的智能合约漏洞检测（合约级+行级）**

MANDO 论文（DSAA 2022）的官方实现：将 Solidity 智能合约源码表示为异构控制流图（HCFGs）与调用图（HCGs），基于 DGL 的 HAN/GAT 模型进行图分类（合约级检测）与节点分类（行级/函数级检测），支持 access_control、重入等 7 类漏洞，节点特征可用 GAE/LINE/node2vec。提供实验数据集与训练/检测脚本，实验环境为 Ubuntu 20.04 + CUDA 11.1 + RTX 3080。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 合约级（图分类）与行级/函数级（节点分类）双层漏洞检测
- 支持 7 类漏洞：access_control、reentrancy、arithmetic 等
- 基于 DGL 实现 HAN/GAT，节点特征支持 GAE/LINE/node2vec
- 提供实验数据集与 TensorBoard 训练监控

## 适用场景

- 检测以太坊智能合约源码中的已知类型漏洞
- 复现 MANDO 论文的图分类/节点分类实验
- 在合约级与行级粒度上定位漏洞位置

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: This repository is an implementation of MANDO: Multi-Level Heterogeneous Graph Embeddings for Fine-Grained Detectio
> L11: The source code is based on the implementation of HAN and GAT model using Deep Graph Library.

## 星数曲线

```mermaid
xychart-beta
    title "MANDO-Project/ge-sc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-27 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8ee26f4d73fd` · [字段定义](../../DATASET.md)*
