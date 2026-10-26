# shell-nlp/gpt_server

⭐ 253 · Python · Apache-2.0 · 推送 2026-05-09 · [GitHub](https://github.com/shell-nlp/gpt_server) · [官网](https://blog.csdn.net/q506610466/article/details/151360406) · 个人维护 · 中文 README

**多模态模型统一 OpenAI 接口服务框架：LLM/Embedding/Reranker/ASR/TTS/文生图**

基于 FastChat 提供 OpenAI 规范接口的模型服务框架，将 Chat、Embedding、Reranker、文本审核、ASR（FunASR）、TTS（SparkTTS）、文生图与图片编辑（diffusers）等多种模型经同一端口调用并自动调度；推理后端支持 HF、vLLM、LMDeploy、SGLang，Embedding/Reranker 支持 infinity 后端动态组批，并兼容 OpenAI Responses API。注意：README 声明自 2026 年 5 月 9 日起不再维护，建议迁移到 vllm/sglang 官方镜像或 vllm-omni 等替代方案。安装提供 uv/conda 环境配置与 Docker 镜像方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多模型共用同一 OpenAI 规范端口并自动调度
- HF/vLLM/LMDeploy/SGLang 多推理后端，Embedding/Reranker 走 infinity 动态组批
- ASR 基于 FunASR、TTS 基于 SparkTTS（支持声音克隆与流式输出）、文生图/图片编辑基于 diffusers
- 兼容 OpenAI Responses API 与 cohere 规范 /v1/rerank

## 适用场景

- 用统一 OpenAI 接口在生产环境部署多类模型
- 让已有 OpenAI 兼容项目（如 Dify）直接调用 Reranker 等模型
- 对推理服务做 Throughput/TTFT/TPOT 性能测试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: 本项目依托fastchat的基础能力来提供**openai server**的能力.
> L13: 1. 支持**Chat**、**Embedding**、**ReRanker**、**text-moderation（文本审核，分类）**、**ASR**、**TTS（支持声音克隆）**、**SD(Stable Diffusion
> L14: 2. 支持**HF**、**vLLM**、**LMDeploy**和**SGLang** 多种加速推理后端引擎。

## 星数曲线

```mermaid
xychart-beta
    title "shell-nlp/gpt_server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 252 --> 254
    line [253, 253]
```

2026-10-18 253 → 2026-10-26 253（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `45bdfaaed7ae` · [字段定义](../../DATASET.md)*
