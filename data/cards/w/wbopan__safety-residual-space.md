# wbopan/safety-residual-space

⭐ 23 · Python · 推送 2026-06-12 · [GitHub](https://github.com/wbopan/safety-residual-space) · [官网](https://arxiv.org/abs/2502.09674) · 个人维护

**ICML 2025 论文代码：LLM 对齐中正交安全方向的多维分析**

ICML 2025 论文 The Hidden Dimensions of LLM Alignment 的源码、数据集与实验结果仓库。提供 8 种越狱攻击的实现（含触发词移除攻击）、DPO/SSFT 安全微调训练代码（基于 accelerate 对 Llama 3.1 8B 全参微调，约需 600GB 显存，资源受限可改用 3B 单卡）、安全残差空间秩分析与干预实验脚本，以及论文用的预生成数据集和中间结果 artifacts（图表、指标 CSV/JSON）。数据生成可选配置 Openrouter API 访问多个模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 种越狱攻击基线实现（GCG、GPTFuzz、PAIR 等）
- Llama 3.1 8B 的 SSFT/DPO 安全微调训练代码
- 安全残差空间的秩、探针分类与干预分析实验
- 提供论文预生成数据集与中间结果 artifacts

## 适用场景

- 复现论文中安全残差空间的多维分析实验
- 研究生成不同越狱样本数据集并评估 Strong Reject 分数
- 对安全对齐模型做层间相关性与组件干预分析

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: Source code, datasets, and experimental results for the **ICML 2025** paper
> L6: *The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions*
> L93: To derive the safety residual space, we perform SSFT and DPO training on Llama 3.1 8B. The training code is in `src

## 星数曲线

```mermaid
xychart-beta
    title "wbopan/safety-residual-space 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3621ea3ce004` · [字段定义](../../DATASET.md)*
