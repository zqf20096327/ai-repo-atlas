# cosbidev/NAIM

⭐ 15 · Python · MIT · 推送 2026-03-14 · [GitHub](https://github.com/cosbidev/NAIM) · 组织维护

**论文官方实现：面向含缺失值表格数据的 Transformer 分类模型**

NAIM（Not Another Imputation Method）的 PyTorch 官方实现，面向表格数据分类任务中存在缺失值的场景：通过按特征类型定制的查找表为缺失值分配非可训练向量，其自注意力机制会忽略注意力矩阵中缺失值的贡献，从而无需任何插补策略；同时提供受图像增广启发的数据增广方式，每个 epoch 随机掩码样本。实验基于 Facebook Hydra 配置文件驱动，支持复现论文实验（5 个 UCI 数据集、0%-75% 缺失率组合）或在自有数据上训练测试，输出交叉验证、预处理参数、模型与预测结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 查找表为缺失值分配非可训练向量，无需插补策略
- 自注意力机制忽略缺失值贡献
- 随机掩码式数据增广（每 epoch）
- Hydra 多层配置文件驱动实验，支持复现论文全部实验

## 适用场景

- 在含缺失值的表格数据上直接做分类训练与测试
- 复现论文中不同缺失率下的实验结果
- 以配置文件方式在自有数据集上声明与运行实验

## 场景标签

 · 领域:机器学习/表格数据

## 证据(README 行号)

> L13: This document describes the implementation of *``Not Another Imputation Method´´* (NAIM) in Pytorch.
> L14: NAIM is an architecture specifically designed for the analysis of tabular data, with a focus on addressing missing 

## 星数曲线

```mermaid
xychart-beta
    title "cosbidev/NAIM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `89e9714f533d` · [字段定义](../../DATASET.md)*
