# brokspace/brok

⭐ 11 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/brokspace/brok) · [官网](https://github.com/brokspace/brok) · 组织维护

**开发者本地工作区的代码搜索与 agent 工具集**

面向开发者的本地优先工具：以 tree-sitter 分块做语义+关键词混合代码搜索，跨 git 子模块索引，可离线且不依赖 LLM。通过 MCP 向 Claude Code、Cursor、VS Code/Copilot、Codex 提供 brok_search 与记忆工具；一条命令接入 Ollama 或 LM Studio 本地模型；会话记忆经 git 共享；支持事件驱动的 shard 集成与 SKILL.md 技能分发。提供 macOS/Linux/Windows 安装脚本与预编译二进制，Cargo 安装需 C 编译器与 protoc。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义+BM25 混合代码搜索，支持离线且无需 LLM
- 经 MCP 为主流编码 agent 提供搜索与记忆工具
- 一条命令接入 Ollama 或 LM Studio 本地模型
- 事件驱动 shard 运行时与 SKILL.md 技能共享机制

## 适用场景

- 在 monorepo 中按语义快速定位函数与类
- 让编码 agent 具备工作区搜索与跨会话记忆能力
- 本地模型下基于代码库的问答与代码审查
- 用 shard 编写响应工作区事件的自定义集成

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L22: - **Your coding agent, Brokspace-aware.** `brok setup agents` gives Claude
> L24:  (MCP) and a set of proven engineering **skills**.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e95d69ad1fc3` · [字段定义](../../DATASET.md)*
