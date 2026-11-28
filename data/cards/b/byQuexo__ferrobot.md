# byQuexo/ferrobot

⭐ 3 · Rust · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/byQuexo/ferrobot) · [官网](https://github.com/byQuexo/ferrobot/wiki) · 个人维护

**自托管多 Agent 团队平台：每个 Agent 有独立沙箱电脑、邮箱与记忆**

以 Rust 守护进程为内核、Tauri 桌面应用为客户端的多 Agent 平台。每个 Agent 获得一个 Docker 容器形式的独立沙箱电脑，配备邮箱、记忆、定时任务与语音；Agent 间可通过 @提及、任务委派和群聊协作，创建新队友需用户审批。模型密钥存于系统钥匙串，由守护进程代理注入，不进入沙箱。支持 Claude（Agent SDK）、OpenAI 兼容 API、Ollama、OpenRouter、Bedrock、Vertex 等提供商，支持 MCP 连接器、cron 例程、OTLP 追踪导出。当前版本 v0.1.12，README 自述尚处早期，部分提供商仅经 fake 服务测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每 Agent 一个 Docker 沙箱，含快照、休眠与加密归档
- 密钥经守护进程代理注入，永不出现在沙箱内
- Agent 间邮箱、任务委派、群聊语音房间
- 支持远程/本地 MCP 连接器与 cron 定时例程

## 适用场景

- 自托管组建一支可协作的 AI Agent 团队处理日常任务
- 用本地 Ollama 模型在无 API key 环境验证多 Agent 流程
- 让 Agent 在各自沙箱里写代码、生成 HTML 并在聊天中实时预览
- 通过 OTLP 把 Agent 的模型与工具调用轨迹导出到可观测平台

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L19: ferrobot is a small Rust daemon on your machine and a thin desktop app on top.
> L22: never enter a sandbox: agents reach their model through the daemon's proxy,
> L79: - **Providers and drivers.** Claude (Agent SDK), any OpenAI-compatible API


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `0a01f197b401` · [字段定义](../../DATASET.md)*
