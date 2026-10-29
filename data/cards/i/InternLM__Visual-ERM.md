# InternLM/Visual-ERM

⭐ 68 · Python · 推送 2026-03-23 · [GitHub](https://github.com/InternLM/Visual-ERM) · [官网](https://huggingface.co/internlm/Visual-ERM) · 组织维护 · 中文 README

**多模态奖励模型：在渲染视觉空间评估 vision-to-code 输出**

面向 chart-to-code、table-to-markdown、SVG-to-code 等 vision-to-code 任务的多模态生成式奖励模型：将模型预测渲染为图像后与真值图像对比，输出含类别、严重度、位置、描述的结构化差异标注，可转换为奖励信号用于 GRPO 强化学习（基于 veRL 框架、vLLM 部署奖励服务），也可作为视觉 critic 用于推理时的反思与修订。基于 Qwen3-VL-8B-Instruct 微调，在 Hugging Face 提供 checkpoint，另发布含 1,335 条实例的 VC-RewardBench 基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在渲染视觉空间而非文本规则或嵌入相似度上评估预测
- 输出含 category/severity/location/description 的结构化差异标注
- 单一奖励模型跨图表、表格、SVG 多任务通用
- 可作为 RL 奖励模型与推理时视觉 critic（反思-修订）两种方式使用

## 适用场景

- 为 vision-to-code 的强化学习训练提供视觉奖励信号
- 推理阶段作为视觉 critic 迭代修正模型输出
- 在 VC-RewardBench 上评测细粒度图像差异判别能力

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L8: 🌈 Official repository for **Visual-ERM**, a multimodal generative reward model for **vision-to-code** tasks.
> L46:  Visual-ERM can be used: (1) as a **reward model** for GRPO-based RL, and (2) as a **visual critic** for iterative 
> L83: We use veRL as the RL training framework. Before starting RL training, launch a reward model (Visual-ERM) service v

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/Visual-ERM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-29 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6100a6ca83af` · [字段定义](../../DATASET.md)*
