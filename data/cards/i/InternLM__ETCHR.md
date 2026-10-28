# InternLM/ETCHR

⭐ 23 · Python · NOASSERTION · 推送 2026-05-25 · [GitHub](https://github.com/InternLM/ETCHR) · [官网](https://arxiv.org/abs/2605.23897) · 组织维护 · 中文 README

**面向 MLLM 的视觉推理辅助图像编辑模型，即插即用提升理解准确率**

ETCHR 是一个问答条件化、推理感知的图像编辑模型（基于 FLUX.2-klein-base-9B），作为解耦的视觉推理辅助模块服务于多模态大语言模型：通过 Edit-Verify-Reason 机制编辑图像以澄清细粒度焦点与空间变换，由理解模型校验编辑结果，失败时回退原图。插件式接入 Qwen3-VL-8B、Kimi K2.5 等下游模型，无需对其微调。仓库提供训练（SFT/RL 两阶段）与评测代码、9B 模型权重及三个数据集/基准，基于 FLUX Non-Commercial License 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解耦即插即用：无需对下游理解模型做任务微调即可接入
- Edit-Verify-Reason 机制：理解模型过滤低质量编辑，失败回退原图
- 提供 9B 模型权重、SFT-400K/GRPO-10K 数据集与 DL3DV-2K 基准
- 两阶段训练流水线与评测代码开源

## 适用场景

- 提升 MLLM 在细粒度感知、图表理解、拼图复原、3D 空间理解等任务的表现
- 在不微调理解模型的前提下为多种 MLLM 增加视觉澄清能力
- 复现模型训练（SFT+RL）或在 DL3DV-2K 基准上评测

## 场景标签

`多模态` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L29: We are thrilled to introduce ETCHR (Editing To Clarify and Harness Reasoning), a novel question-conditioned, reason
> L36: - 🔥 **Decoupled & Plug-and-Play:** ETCHR functions as a separate module, allowing it to assist diverse downstream M

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/ETCHR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `83f6371d9939` · [字段定义](../../DATASET.md)*
