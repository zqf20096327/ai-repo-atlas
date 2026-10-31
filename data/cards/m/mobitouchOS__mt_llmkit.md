# mobitouchOS/mt_llmkit

⭐ 15 · Dart · MIT · 推送 2026-09-08 · [GitHub](https://github.com/mobitouchOS/mt_llmkit) · [官网](https://mobitouch.net/) · 组织维护

**Flutter 移动端 LLM 工具包：本地 GGUF 推理、云端统一接口与本地 RAG**

面向 Flutter 开发者的 LLM 插件：通过 llamadart（封装 llama.cpp）在 Android/iOS 设备上运行量化 GGUF 模型，支持 GPU 层数卸载、流式输出、实时性能指标（tokens/s）与多模态视觉模型（需 mmproj 文件）。另提供统一 AIChatProvider 接口接入 OpenAI、Gemini、Claude、Mistral 四家云端服务商，以及全本地 RAG 管线（分块、本地嵌入、内存向量库、索引持久化）。限制：处于 0.0.1-beta.1 版本；云端能力需各自 API key；本地推理需自备 GGUF 模型文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端运行 GGUF 模型，支持 isolate/inProcess 两种后端与 GPU 层数卸载
- 统一接口接入 OpenAI/Gemini/Claude/Mistral，含类型化异常与自动重试
- 多模态视觉：LLaVA、Gemma 3、Qwen 2.5 VL、SmolVLM 等 mmproj 模型
- 全本地 RAG：分块、嵌入、向量检索、索引持久化均在单 worker isolate 内

## 适用场景

- 在 Android/iOS 应用中离线运行 LLM 并流式输出
- 用一套代码在多个云端 LLM 服务商之间切换
- 构建完全不出设备的文档问答（RAG）功能
- 在移动端接入多模态视觉模型做图片理解

## 场景标签

`RAG` `推理引擎` `多模态` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: A Flutter plugin for running Large Language Models (LLMs) locally on Android and iOS using llamadart (which wraps ll
> L320: `RagEngine` provides a fully on-device Retrieval-Augmented Generation pipeline. Documents are chunked, embedded wi

## 星数曲线

```mermaid
xychart-beta
    title "mobitouchOS/mt_llmkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `27a755272e15` · [字段定义](../../DATASET.md)*
