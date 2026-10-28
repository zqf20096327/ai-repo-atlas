# tum-pbs/tadpole

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/tum-pbs/tadpole) · [官网](https://tum-pbs.github.io/tadpole/) · 组织维护

**三维偏微分方程的自动编码器科学基础模型**

慕尼黑工业大学团队发布的科学基础模型，以自编码器方式在三维 PDE 数据上预训练，采用 GPU 求解器在线生成合成训练数据以规避 3D 数据的存储与 IO 瓶颈。支持自编码重建、动力学预测与生成建模等多种下游任务；动力学学习采用低秩适配、潜空间变换与重引入跳连的参数高效微调策略。预训练权重托管在 Hugging Face，通过 pip 从 GitHub 安装；在线学习框架与微调教程尚未补充。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以自编码器范式在三维 PDE 数据上预训练基础模型
- GPU 求解器在线生成数据，规避 3D 数据存储与 IO 瓶颈
- 支持自编码、动力学预测、生成建模等多下游任务
- 预训练权重托管于 Hugging Face

## 适用场景

- 加载预训练权重对三维 PDE 解做重建与预测
- 在物理仿真任务上做参数高效微调
- 科研复现论文中的在线学习预训练方法

## 场景标签

`科研工具` `模型训练` `微调` · 领域:学习与行业

## 证据(README 行号)

> L18: Tadpole is a foundation model for three-dimensional partial differential equations (PDEs).
> L26: (2) Tadpole is pretrained with ***online learning***, utilizing a GPU-based solver to generate diverse data distrib
> L28: (3) Tadpole is able to process ***multiple downstream tasks***, including autoencoding, dynamics prediction, and ge

## 星数曲线

```mermaid
xychart-beta
    title "tum-pbs/tadpole 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-26 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9279312db84d` · [字段定义](../../DATASET.md)*
