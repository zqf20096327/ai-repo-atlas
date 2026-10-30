# cih1996/AgentKernel

⭐ 15 · Rust · 推送 2026-06-22 · [GitHub](https://github.com/cih1996/AgentKernel) · [官网](https://cih1996.github.io/AgentKernel/) · 个人维护 · 中文 README

**轻量级 Rust Agent 运行时内核：以 WebSocket 接入 AI**

Rust 编写的可嵌入 AI 运行时内核（Agent Runtime Kernel），以 WebSocket 为核心通信协议独立运行：负责连接模型、管理会话与上下文、推送推理进度事件，业务侧通过 WS 动态注册工具能力（含 MCP）并由回调执行。兼容 OpenAI、Claude、Ollama 等多模型提供商。不内置重型记忆系统或技能市场，定位为纯运行时，非 Chat UI 或完整业务 Agent。通过 git clone 与 cargo run 启动，默认监听 ws://localhost:9991/ws，另提供本地 Web 调试控制台。

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

- WebSocket 双向通信协议，与业务代码解耦的独立微服务
- 工具能力/技能/MCP 动态热插拔注册与回调执行
- 兼容 OpenAI、Claude、Ollama 等多模型提供商
- 事件流一等公民：推送 model.delta、tool.call.request 等状态

## 适用场景

- 为已有业务系统或 Web 应用添加 AI 运行时
- 构建多 Agent 编排平台或类似 ComfyUI 的 Agent 运行节点
- 跨语言项目（Python/Node.js/Go/Rust）通过 WS 复用同一 AI 内核

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A lightweight, embeddable, WebSocket-driven AI Runtime Kernel
> L36: AgentKernel is neither a Chat UI nor a Business Agent, but an **Agent Runtime Kernel**.

## 星数曲线

```mermaid
xychart-beta
    title "cih1996/AgentKernel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e405647cce7d` · [字段定义](../../DATASET.md)*
