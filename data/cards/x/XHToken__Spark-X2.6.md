# XHToken/Spark-X2.6

⭐ 833 · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/XHToken/Spark-X2.6) · [官网](https://xhtoken.ai/) · 组织维护 · 中文 README

**4B 参数开源 LLM 系列，面向端侧 agent 与编码任务**

Spark-X2.6-4B 是 SparkLLM Team 发布的 4B 参数通用语言模型，架构与 Spark-X2.5-4B 相同，通过改进的后训练提升编码、agent 工作流、长上下文与多语言能力。提供三档可配置思考预算（none/low/high）以平衡推理质量与延迟。模型在 Hugging Face、ModelScope、Ollama 等平台发布，README 给出 Transformers、SGLang、vLLM、MLX、llama.cpp、Ollama、LM Studio、Unsloth 等多种推理方式，支持 NVIDIA GPU 与 Ascend NPU，Apache 2.0 许可，推荐 Llama-Factory 微调。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4B 参数端侧模型，架构沿用 Spark-X2.5-4B，经改进后训练获得能力提升
- 三档思考预算（none/low/high）可动态平衡推理与延迟
- 覆盖 Transformers/SGLang/vLLM/MLX/llama.cpp/Ollama/LM Studio 等多种推理途径
- 支持 NVIDIA GPU 与华为昇腾 NPU 部署

## 适用场景

- 在本地或端侧设备上运行支持工具调用与多步规划的 agent
- 搭建本地 OpenAI 兼容推理服务（SGLang/vLLM/llama.cpp）
- 资源受限环境下的编码与长上下文任务

## 场景标签

 · 领域:AI 模型/自然语言处理

## 证据(README 行号)

> L15: A little over a month has passed since Spark-X2.5. In the rapidly evolving world of AI agents, that is enough time 
> L17: Spark-X2.6-4B retains exactly the same architecture as Spark-X2.5-4B, achieving its capability gains through improv


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `b5684203c473` · [字段定义](../../DATASET.md)*
