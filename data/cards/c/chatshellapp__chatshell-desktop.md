# chatshellapp/chatshell-desktop

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/chatshellapp/chatshell-desktop) · [官网](https://chatshell.app) · 组织维护 · 中文 README

**桌面 AI agent：内置 9 种工具，开箱即用的自主任务执行客户端**

基于 Tauri 2 + Rust 构建的桌面 AI agent 客户端，内置 Web 搜索、Web 抓取、Bash、文件读写编辑、Grep、Glob 等 9 种工具，AI 可自主组合多步完成研究、代码修改与系统自动化任务。支持 40+ 云端模型提供商及 Ollama/LM Studio 等本地模型，API 密钥用 AES-256-GCM 加密存于系统钥匙串，数据存本地 SQLite、无遥测。提供 Skills 技能系统与 MCP 服务器接入，可创建本地自定义助手。三平台安装包 22MB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种内置工具零配置，AI 自主链式调用完成多步任务
- 支持 40+ 云端提供商与 Ollama/LM Studio 等本地模型
- Skills 渐进式注入技能系统，未调用技能不消耗 token
- MCP 集成：STDIO/HTTP 双传输、OAuth 2.1/PKCE 认证

## 适用场景

- 让 AI 自主搜索网页并汇总成报告
- 在本地项目中批量查找、替换代码并生成文档
- 通过 MCP 接入数据库与外部工具扩展 agent 能力

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A lightweight desktop AI agent with 9 built-in tools. Built with Tauri 2 + Rust, not Electron.
> L35: The agent chains Grep, Read, and Write tools together to complete multi-step tasks on its own.
> L82: Most AI clients are just chat wrappers — you type, the AI replies, end of story. ChatShell ships with **9 built-in 


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `cd15e452a2e3` · [字段定义](../../DATASET.md)*
