# YFrisch/Generative_Models_Lecture

⭐ 3 · Jupyter Notebook · MIT · 推送 2026-11-03 · [GitHub](https://github.com/YFrisch/Generative_Models_Lecture) · 个人维护

**五类生成模型家族的 notebook 教程（从零实现到 MNIST）**

以 Jupyter notebook 形式组织的生成模型教学材料：VAE、归一化流、自回归模型、GAN、扩散模型五个家族先在二维 Ring of Gaussians 上从零实现并对比，再扩展到 MNIST（共 13 个编号 notebook），最后深入扩散采样器、classifier-free guidance 与无重训练的综合活动。面向掌握基础机器学习、概率与微积分的高年级本科生、研究生、工程师和研究者，强调可检查的 PyTorch 从零实现而非框架抽象。附各 notebook 运行时长、硬件建议与预训练 checkpoint 指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个编号 notebook：五种生成模型家族在 RoG 与 MNIST 上从零 PyTorch 实现
- DDPM/DDIM/DPM-Solver++ 采样器对比与 classifier-free guidance 演示
- 内置教学 checkpoint，重计算 notebook 无需重训即可加载演示
- 附各 notebook 运行时长与硬件要求对照表

## 适用场景

- 系统学习五类生成模型的目标函数与实现细节
- 在二维实验上直观对比不同家族的模式覆盖行为
- 用预训练 checkpoint 演示 MNIST 级生成模型而免于重训

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository is a notebook-based introduction to five major generative-model families: variational autoencoders (
> L11: The material is intended for advanced undergraduate or graduate students, engineers, and researchers who know basic

## 星数曲线

```mermaid
xychart-beta
    title "YFrisch/Generative_Models_Lecture 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `9f392c8080b9` · [字段定义](../../DATASET.md)*
