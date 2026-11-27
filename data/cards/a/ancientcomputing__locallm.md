# ancientcomputing/locallm

⭐ 10 · Swift · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/ancientcomputing/locallm) · [官网](https://thisbrain.ai/locallm) · 组织维护

**给 Mac 应用加本地 AI 聊天与工具调用的 Swift SDK**

面向开发者的 Swift SDK，为 Mac 应用集成可调用工具的聊天助手：模型可选 Apple 端侧模型、MLX 运行的开源权重模型（Qwen/Gemma/Llama）、Apple Private Cloud Compute 或托管模型，切换模型仅需改一行。核心机制是每次工具调用经过授权器（authorizer）安全门：改数据的工具须先获批准，配合沙箱与审计流。以多个二进制框架加 SwiftUI 组件源码分发，SDK 源码闭包但免费提供，需 Apple Silicon Mac、Xcode 27 与 macOS 27（端侧模型 macOS 26 即可）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Apple 端侧模型、MLX 开源权重模型与托管模型统一 API，一行切换
- 每次工具调用经 authorizer 授权，改数据工具默认拒绝未授权调用
- 内置 MCP 客户端，支持 resources/prompts 与多服务器按需联系
- prompt 缓存默认开启，本地模型工具循环不重读全对话

## 适用场景

- 给 Mac 应用加一个能调用工具的本地聊天助手
- 在数据不出机器的前提下用 Qwen3 等 MLX 模型
- 让聊天中的工具调用走统一审批与审计流程
- 用 Claude Code/Codex 等 agent 按 skill 快速搭建 SDK 应用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Add a chat assistant that can use tools to your own Mac app, with the model running on the Mac: Apple's
> L69: |`LocalLMLabSDKCore`|The model layer (routes, sessions, Apple's on-device model), tools, an MCP client, the securit
> L87: - **Every tool call passes an authorizer.** The authorizer is the code that decides whether a call may run. A sessi


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `ad1fac139865` · [字段定义](../../DATASET.md)*
