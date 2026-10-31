# tachella/unsure

⭐ 14 · Python · BSD-3-Clause · 推送 2025-11-21 · [GitHub](https://github.com/tachella/unsure) · [官网](https://tachella.github.io/) · 个人维护

**ICLR'25 论文 UNSURE 代码：无需噪声水平的自监督重建损失**

Tachella、Davies 与 Jacques 的 ICLR 2025 论文 UNSURE 的官方代码库。提出一种自监督学习损失，用于在仅有噪声测量、且噪声水平未知的数据集上训练重建网络，通过 min-max 形式结合网络散度项估计风险，支持高斯、泊松-高斯、空间相关噪声等多种变体。实现基于 deepinv 库，UNSURE 损失已并入 deepinv 并提供 jupyter notebook 演示。使用流程：克隆仓库、安装 deepinv、运行 generate_datasets.py 生成数据后运行 main.py。面向成像逆问题研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 噪声水平未知的自监督损失（SURE 的扩展）
- 支持高斯、泊松-高斯、空间相关等多种噪声类型变体
- 基于 deepinv 库实现，损失已合入该库并有 notebook 演示

## 适用场景

- 复现论文中的自监督重建实验
- 在噪声水平未知的成像逆问题中训练重建网络
- 通过 deepinv 集成在自有重建管线中使用该损失

## 场景标签

 · 领域:计算成像/逆问题

## 证据(README 行号)

> L13: UNSURE is a self-supervised learning loss that can be used for learning a reconstruction network $f$
> L6: We use the deepinv library for most of the code.

## 星数曲线

```mermaid
xychart-beta
    title "tachella/unsure 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5af9e37a95c9` · [字段定义](../../DATASET.md)*
