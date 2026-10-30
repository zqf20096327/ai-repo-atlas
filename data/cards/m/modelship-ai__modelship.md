# modelship-ai/modelship

⭐ 54 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/modelship-ai/modelship) · [官网](https://docs.model-ship.ai/) · 组织维护

**自托管 OpenAI 兼容推理网关：多模型共享 GPU，一个 /v1**

基于 Ray Serve 的自托管推理服务，提供 OpenAI 兼容的 /v1 接口（chat/completions、responses、embeddings、语音、图像生成），面向需要在自己硬件上运行多模型的开发者。支持 vLLM、llama.cpp、Diffusers、sherpa-onnx、whisper.cpp 等后端共存，每模型独立部署与资源预算，可按 GPU 分数分配；提供服务端会话状态、MCP 工具执行、零停机热更新与 Prometheus/OpenTelemetry 可观测性。通过 Docker（CPU/CUDA）、pip/uv 原生安装或 Helm 部署，要求 Python 3.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型多 GPU 共存：chat、嵌入、STT、TTS、图像生成走同一 OpenAI 兼容 /v1
- 推理后端可插拔：vLLM、llama.cpp、Diffusers、sherpa-onnx、whisper.cpp
- 服务端 MCP 工具执行与 reasoning 解析为 first-class 输出
- 零停机增量热更新模型集，每模型独立生命周期与 GPU 分数分配

## 适用场景

- 让现有 OpenAI 客户端的 agent 切换到自托管 /v1/responses 后端
- 在有限 GPU 上同时部署 LLM、TTS 与图像生成并按比例分配资源
- 搭建带会话状态与 MCP 工具调用的多模型推理集群

## 场景标签

`推理引擎` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: Modelship serves the whole agentic surface — reasoning, tool calling, server-side conversation state, and MCP serve
> L104: - **A stack that fits the hardware you have.** Allocate GPU fractions per model (70% for the LLM, 5% for TTS), or 
> L140: Each model runs as an isolated Ray Serve deployment with its own lifecycle, health checks, and resource budget. Se

## 星数曲线

```mermaid
xychart-beta
    title "modelship-ai/modelship 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-30 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e6ccb3e42295` · [字段定义](../../DATASET.md)*
