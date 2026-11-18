# Antrairs/inside-transformer

⭐ 12 · Jupyter Notebook · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/Antrairs/inside-transformer) · 个人维护 · 中文 README

**以最小可运行实现讲解 Transformer 架构的教程**

一个以 notebook 为主体的 Transformer 架构教学项目：按章节顺序从单头自注意力、多头注意力、RoPE 位置编码到 Transformer Encoder 与 GPT 风格 Decoder，逐步用最小化 PyTorch 代码重建并配合张量形状、训练循环、实验结果与注意力可视化。面向想理解注意力机制原理的学习者，要求 Python 3.13+ 与 PyTorch 2.10+，通过 Jupyter Notebook 运行；Decoder 章节尚在进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按论文到代码的学习路径重建自注意力、多头注意力、RoPE、Encoder 与 Decoder
- 每章配套可运行的 Jupyter Notebook，含张量形状、训练循环与实验结果
- 最小实现优先，核心逻辑不隐藏在大型框架之后
- 包含玩具任务、真实数据集训练与注意力可视化

## 适用场景

- 想从零理解自注意力与 RoPE 的实现细节
- 跟随章节顺序系统学习 Transformer 架构
- 在真实数据集上运行小型实验并查看注意力可视化

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2:  A notebook-first guide to the Transformer architecture, built from minimal, runnable PyTorch implementations.
> L15: - Runnable, chapter-sized notebooks: each topic pairs explanation with PyTorch code, tensor shapes, training loops,

## 星数曲线

```mermaid
xychart-beta
    title "Antrairs/inside-transformer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-11-08", "2026-11-18"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-10-18 11 → 2026-11-18 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `70d24e3563d0` · [字段定义](../../DATASET.md)*
