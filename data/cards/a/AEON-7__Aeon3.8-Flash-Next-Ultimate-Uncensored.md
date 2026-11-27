# AEON-7/Aeon3.8-Flash-Next-Ultimate-Uncensored

⭐ 3 · 推送 2026-11-26 · [GitHub](https://github.com/AEON-7/Aeon3.8-Flash-Next-Ultimate-Uncensored) · [官网](https://huggingface.co/AEON-7/Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS) · 个人维护

**为 DGX Spark 用户提供去审查版 Qwen 180B 模型的部署指南**

该仓库收录 NVIDIA DGX Spark 上运行 Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED（基于 Qwen3.8-Flash-Next 的 abliterated 版本，180B 参数，NVFP4 4-bit 量化后占 98 GiB）的复制即用部署指南。提供 1、2、4 台 Spark 共五种经过验证的配置，分别使用 Strata 或 AEON vLLM Ultimate 引擎，对外提供 OpenAI 兼容 API，支持图像读取与 131K–256K 上下文。仓库另含面向 AI agent 的 AGENTS.md，用于自动化部署。权重托管在 Hugging Face，遵循 Qwen Community License 1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种经测量的部署配置：单 Spark 60.6 tok/s，四 Spark 并发 748 tok/s
- 去除拒绝行为的 abliterated 模型，56 项测试 0 次拒绝
- AGENTS.md 供 AI agent 自动完成硬件识别、配置选择与部署
- OpenAI 兼容 API，支持图像输入与 131K–256K 上下文

## 适用场景

- 在 DGX Spark 本地部署无审查的大参数多模态模型
- 通过 OpenAI 兼容 API 接入本地应用
- 让 AI agent 按指南自动完成模型上线与测试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: **A 180-billion-parameter model with the refusals removed, running on one desktop DGX Spark at 60 tokens a second.**
> L9: This repo holds the copy-paste serve guides for Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS: an uncensored (abli


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `a09b9a6f402d` · [字段定义](../../DATASET.md)*
