# SoftBacon-Software/mycelium

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/SoftBacon-Software/mycelium) · [官网](https://mycelium.fyi/) · 组织维护

**本地自托管的多智能体记忆与协调层，HTTP 皆可接入**

单一 Node 进程加内嵌 SQLite 的本地服务器，让 AI agent、脚本、传感器、GPU 与人通过 HTTP 加入同一网络，共享任务、消息、审批、上下文存储与持久身份，无云端依赖。提供 MCP 服务器（79 个工具）、HTTP API、Node SDK 与无构建步骤的操作台；核心功能覆盖多级审批门、哈希链记忆审计、运行遥测与花费追踪、GPU 无人机队列与插件系统。安装支持一键脚本、Docker Compose 与源码运行，需 Node 20+。README 附成熟度声明：核心经测试，语音适配器等边缘部分无测试覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任何 HTTP 客户端可注册为 peer，硬件设备为一等公民
- 风险分级的人工审批门与全局 kill switch
- 哈希链式追加型记忆审计表，可校验篡改
- 79 个 mycelium_* 工具的 MCP 服务器与插件系统

## 适用场景

- 在自有硬件上协调多个本地/云端模型 agent 的任务与消息
- 为 Claude Code 等 MCP 客户端提供共享记忆与审批工作流
- 让传感器、摄像头、GPU worker 与 agent 在同一网络协作
- 对 agent 记忆读写做可验证的审计追踪

## 场景标签

`Agent 记忆` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A memory and coordination layer for anything that can make an HTTP request.** If it can `POST`, it can join — AI a
> L7: We build flagship things on it — a self-improving local multi-model code squad, the local forge we run our own proje
> L19: - **Agent network** — register any agent (Claude, GPT, Ollama, local models, scripts). Each gets a role contract, a

## 星数曲线

```mermaid
xychart-beta
    title "SoftBacon-Software/mycelium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `cd12fd096027` · [字段定义](../../DATASET.md)*
