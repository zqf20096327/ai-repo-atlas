# MiniMax-AI/MiniMax-M2.1

⭐ 543 · NOASSERTION · 推送 2026-01-28 · [GitHub](https://github.com/MiniMax-AI/MiniMax-M2.1) · [官网](https://www.minimax.io) · 组织维护 · 中文 README

**面向开发与 agent 场景的开源大语言模型权重（M2.1）**

MiniMax 公司发布的开源大语言模型 MiniMax-M2.1 的官方仓库，发布模型权重并面向编码、工具调用、指令遵循与长程规划等 agent 能力优化。README 提供三条使用途径：MiniMax 开放平台 API、基于该模型的产品 MiniMax Agent、以及 Hugging Face 上的开源权重本地部署。本地部署推荐 SGLang、vLLM、Transformers，另列 MLX-LM 与 KTransformers；给出推荐推理参数与默认系统提示。内容大量为基准测试结果（SWE-bench、VIBE、Toolathlon 等）与评测方法说明。许可为 Modified-MIT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型权重开源，支持本地部署
- 面向编码、工具调用、长程规划的 agent 能力优化
- 推荐 SGLang/vLLM/Transformers 三种推理框架并附部署指南
- 给出推荐推理参数与工具调用指南

## 适用场景

- 通过 API 或本地部署将模型用于编码 agent 应用
- 在多种推理框架上自行部署 MiniMax-M2.1
- 对比基准结果评估模型在软件工程任务上的表现

## 场景标签

 · 领域:大语言模型/开发与 agent

## 证据(README 行号)

> L42: Today, we are handing **MiniMax-M2.1** over to the open-source community. This release is more than just a paramete
> L52: - The MiniMax-M2.1 model weights are now open-source, allowing for local deployment and use: https://huggingface.co

## 星数曲线

```mermaid
xychart-beta
    title "MiniMax-AI/MiniMax-M2.1 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 542 --> 544
    line [543, 543]
```

2026-10-18 543 → 2026-10-26 543（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `72fbaef34796` · [字段定义](../../DATASET.md)*
