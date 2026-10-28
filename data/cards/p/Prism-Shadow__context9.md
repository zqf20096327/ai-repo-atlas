# Prism-Shadow/context9

⭐ 31 · TypeScript · Apache-2.0 · 推送 2026-01-30 · [GitHub](https://github.com/Prism-Shadow/context9) · 组织维护 · 中文 README

**本地优先的 MCP 服务器：为 AI agent 实时供给最新代码文档**

Context9 是一个可自部署的 MCP（Model Context Protocol）服务器，从配置的 GitHub 仓库（含私有仓库，需 Token）同步、发现并索引文档，通过 MCP 接口向 Cursor、Claude Code 等编程 agent 实时提供最新文档以降低 LLM 幻觉。提供 Web UI 管理仓库配置与 API key 权限（按 key 限定可访问仓库），仓库根目录需提供 spec.md 作为索引入口，文档内直接使用仓库相对链接即可。部署方式包括 Docker 镜像、Dockerfile 自建及源码运行（Python>=3.10，GUI 需 Node.js>=18），支持配置同步间隔。默认登录账号密码为 ctx9-admin/88888888，首次登录需修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器向 agent 实时供给仓库文档
- 支持私有仓库（GitHub Token）与公开仓库混合配置
- Web UI 管理仓库、API key 及按 key 的仓库访问权限
- Docker 镜像与源码两种部署路径，GUI 与 API 同端口服务

## 适用场景

- 让 Cursor / Claude Code 在编码时自动获取最新项目文档
- 在企业私有服务器上安全接入内部私有仓库文档
- 为团队统一维护 agent 可访问的文档知识源

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L27: **Context9 (Context Mine)** is an MCP (Model Context Protocol) server. With local deployment, Context9 securely fee
> L95: After deploying the Context9 service, you can seamlessly integrate both private and public real-time code documenta

## 星数曲线

```mermaid
xychart-beta
    title "Prism-Shadow/context9 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7d223d6f71b7` · [字段定义](../../DATASET.md)*
