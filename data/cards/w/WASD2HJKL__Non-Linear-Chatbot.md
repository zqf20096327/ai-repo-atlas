# WASD2HJKL/Non-Linear-Chatbot

⭐ 10 · JavaScript · MIT · 推送 2026-02-17 · [GitHub](https://github.com/WASD2HJKL/Non-Linear-Chatbot) · [官网](https://nonlinearchatbot.netlify.app) · 个人维护 · 中文 README

**树状分支式 AI 聊天应用：从任意节点探索多条对话路径**

基于 Wasp + React + ReactFlow 构建的可视化对话应用：每条消息对是树中的一个节点，用户可在任意位置分叉出新分支、保留上下文地探索不同回复路径，并以交互式节点图实时查看、拖拽整理对话树。AI 侧采用统一客户端工厂接入任意 OpenAI 兼容端点，服务端流式输出与 NDJSON 队列解析，API key 在服务端管理；支持导出可离线打开的交互式 HTML。需 Node.js 22+ 与 PostgreSQL；本地模型（Ollama）仅用于开发环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意节点分叉的对话树，ReactFlow 实时可视化与拖拽整理
- 统一客户端工厂接入任意 OpenAI 兼容 API 端点
- 服务端流式输出与队列式 NDJSON 解析
- 对话树导出为可离线使用的交互式 HTML

## 适用场景

- 对同一问题探索多条回答路径后再做决定
- 以节点图方式梳理复杂主题的讨论脉络
- 导出对话树为独立 HTML 分享给他人离线查看

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: A revolutionary conversational AI application that breaks free from traditional linear chat interfaces. Create branc
> L32: - Multi-provider AI support with OpenAI-compatible API interfaces
> L34: - Support for OpenAI, Gemini, OpenRouter, and other cloud providers

## 星数曲线

```mermaid
xychart-beta
    title "WASD2HJKL/Non-Linear-Chatbot 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `167e6f717253` · [字段定义](../../DATASET.md)*
