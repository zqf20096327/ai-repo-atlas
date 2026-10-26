# doganarif/fastapi-ai-sdk

⭐ 62 · Python · MIT · 推送 2026-06-23 · [GitHub](https://github.com/doganarif/fastapi-ai-sdk) · 个人维护

**FastAPI 后端对接 Vercel AI SDK 的流式响应辅助库**

Python 辅助库，用于在 FastAPI 后端实现 Vercel AI SDK 协议，使 Next.js 前端可通过 useChat 获得类型安全的 SSE 流式 AI 响应。实现完整 AI SDK 事件类型（文本流、推理、工具调用、结构化数据、错误事件），提供 AIStreamBuilder 构建器与 @ai_endpoint、@streaming_endpoint、@tool_endpoint 装饰器。需 Python 3.9+ 与 FastAPI，通过 pip 安装。库本身不调用模型，由开发者自行组装流内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现完整 Vercel AI SDK 协议事件类型（含 reasoning、tool-call、data-*）
- AIStreamBuilder 构建器与三种装饰器（ai_endpoint/streaming_endpoint/tool_endpoint）
- 基于 Pydantic 的类型校验与 SSE 流式支持
- 提供 Next.js 前端 useChat 集成示例

## 适用场景

- 用 FastAPI 作为 Next.js AI 应用的流式后端
- 向 Vercel AI SDK 前端推送工具调用与推理过程事件
- 快速搭建符合 AI SDK 协议的聊天/生成接口

## 场景标签

 · 领域:LLM 应用开发/后端集成

## 证据(README 行号)

> L8: A Pythonic helper library for building FastAPI applications that integrate with the Vercel AI SDK. This library prov
> L12: - **Full Vercel AI SDK Compatibility** - Implements the complete AI SDK protocol specification

## 星数曲线

```mermaid
xychart-beta
    title "doganarif/fastapi-ai-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-26 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `323f2901e151` · [字段定义](../../DATASET.md)*
