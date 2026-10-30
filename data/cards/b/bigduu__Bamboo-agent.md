# bigduu/Bamboo-agent

⭐ 21 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/bigduu/Bamboo-agent) · [官网](https://bodhi-ai.vercel.app) · 个人维护 · 中文 README

**本地优先的 Rust agent 运行时：终端/浏览器/SDK 里跑 AI 代理**

Bamboo 是 Zenith 体系中的本地 agent harness/runtime：给定工作区与配置的模型后可读文件、调用工具、维护会话，并通过 HTTP/SSE/WebSocket 将同一运行时暴露给浏览器界面、桌面 shell 或 Rust 应用。支持 MCP 服务器、技能、子代理、工作流、定时任务与上下文组装，记忆持久化由 Jiandu 承担。本地运行但依赖外部模型提供商，密钥加密存储；源码构建需 Rust 1.95+ 并依赖锁定的 Lotus Next 前端产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 agent 引擎以 CLI、HTTP/SSE/WebSocket 服务与 Rust SDK 三种方式使用
- 支持 MCP 服务器、技能、子代理、定时提示词等扩展机制
- 会话与配置默认存储于 ~/.bamboo，提供商密钥加密存储
- 提供 Docker Compose 部署（loopback 端口、非 root 用户、命名数据卷）

## 适用场景

- 在终端对代码仓库执行提示词并续接会话
- 在自己的应用中通过 HTTP/WebSocket 或内嵌 SDK 接入 agent 能力
- 本地托管带浏览器界面的 agent 服务并接入既有 MCP 工具

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L9: Bamboo is the local agent harness at the core of Zenith. Give it a workspace and a configured model: it can read fil
> L19: |Keep useful project context|Session notes and Jiandu-backed durable memory can carry selected facts across turns a
> L135: For SDK embedding, `bamboo_sdk::agent::Agent` provides `run`, `run_stream`, and

## 星数曲线

```mermaid
xychart-beta
    title "bigduu/Bamboo-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `09f22d4c7d12` · [字段定义](../../DATASET.md)*
