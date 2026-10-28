# rupeshs/verity

⭐ 52 · Python · 推送 2026-03-01 · [GitHub](https://github.com/rupeshs/verity) · 个人维护

**本地运行的 Perplexity 式 AI 搜索问答引擎**

面向 AI PC 的本地 AI 搜索与问答引擎：用自托管 SearXNG 做元搜索，结合检索与本地 LLM 推理生成有出处的回答，不依赖云端 LLM 服务。支持 OpenVINO（CPU/iGPU/NPU）、Ollama（CPU/CUDA/Metal）、llama.cpp server 及任意 OpenAI 兼容服务作为运行时，默认使用 Jan-nano 4B 模型。提供 CLI、WebUI、流式 API server 与 MCP server，Windows 有自动化安装脚本，另有 Docker 方式（不含 OpenVINO）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SearXNG 自托管搜索 + 本地 LLM 生成有据回答
- 支持 OpenVINO（含 Intel NPU）/Ollama/llama.cpp/OpenAI 兼容服务四种运行时
- 提供 CLI、WebUI、SSE 流式 API 与 MCP server
- 无需付费 API，可完全自托管

## 适用场景

- 在本地跑一个 Perplexity 式的搜索问答工具
- 在 Intel AI PC 上利用 NPU 做本地推理问答
- 通过 MCP 把本地搜索问答接入 LM Studio 等 agent 客户端

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: **Verity** is a Perplexity-style AI search and answer engine that runs fully locally on AI PCs.
> L14: - OpenVINO,Ollama models,llama.cpp server or any OpenAI compatible LLM servers supported
> L22: - **Ollama** - CPU / CUDA / Apple Metal

## 星数曲线

```mermaid
xychart-beta
    title "rupeshs/verity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `19d51b5f4a40` · [字段定义](../../DATASET.md)*
