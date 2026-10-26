# fokhruli/STGCN-rehab

⭐ 45 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/fokhruli/STGCN-rehab) · [官网](https://fokhruli.github.io/STGCN-rehab/) · 个人维护

**面向论文的康复动作评分模型：STGCN 训练与评估代码**

IEEE TNSRE 2022 论文官方实现，提供基于时空图卷积网络（STGCN）及 LSTM 扩展的训练与评估代码，用于对 KIMORE 和 UI-PRMD 两个骨架数据集上的物理康复动作进行评分。流程为：数据预处理、生成骨架图、训练 STGCN 模型、运行 demo 推理输出预测评分。用户需自行下载并解压数据集，通过编辑 train.py 修改优化器与学习率等参数。依赖 Python3 与 TensorFlow 2.0。

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

- STGCN 与 STGCN+LSTM 扩展的端到端康复动作评分模型
- 支持 KIMORE 与 UI-PRMD 两个骨架数据集
- 提供训练脚本 train.py 与推理示例 demo.py

## 适用场景

- 复现论文中的康复动作评分实验
- 在 KIMORE/UI-PRMD 数据集上训练 STGCN 评分模型
- 对康复动作骨架样本执行推理并输出预测评分

## 场景标签

 · 领域:医疗康复/人体动作分析

## 证据(README 行号)

> L3: This code is the official implementation of the following works (train + eval):
> L33: * `train.py` : to perform training on Physical rehabilitation exercise

## 星数曲线

```mermaid
xychart-beta
    title "fokhruli/STGCN-rehab 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-26 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3dccfee12ebf` · [字段定义](../../DATASET.md)*
