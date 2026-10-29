# kh0pper/crow

⭐ 26 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/kh0pper/crow) · [官网](https://maestro.press/software/crow/) · 组织维护

**自托管的模块化 Agent 框架与 MCP 平台，连接自有 AI 客户端**

Crow 是可自托管的开源 agentic 框架兼 MCP 平台，基于 Model Context Protocol。一方面通过 Bot Builder 让用户构建运行自己的 Agent，部署到 Gmail、Discord、语音（含 Meta Ray-Ban 眼镜），带持久记忆、权限策略与操作员审批；另一方面作为原生 MCP 服务器接入 Claude Code、Claude Desktop、Cursor 等既有 AI 客户端。附带 P2P 加密共享、博客、S3 兼容存储、20+ 集成、模型目录（含 llama.cpp 运行时），以及 Crow OS 树莓派/Debian 自托管安装方式。本地或云端模型均可，数据留在自有基础设施。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bot Builder 构建 Agent 并部署到 email/Discord/语音渠道，带权限策略与操作员审批
- 作为原生 MCP 服务器接入 Claude Code、Claude Desktop、Cursor 等 AI 客户端
- 端到端加密 P2P 共享记忆、项目与消息，无中心服务器
- Crow OS 安装脚本支持树莓派/Debian/Ubuntu，可安装 Ollama、Nextcloud 等自托管应用

## 适用场景

- 在自有硬件上搭建带记忆和研究能力的个人 AI 服务器
- 让 Claude Code 或 Cursor 通过 MCP 直接使用自托管的记忆与工具
- 构建跨 Gmail/Discord/语音渠道运行的自动化 Agent
- 在树莓派上运行自托管家庭服务器并安装本地 AI 应用

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Crow is a modular, agentic framework and MCP platform that integrates with the services and AI tools you already use
> L11: As an **agentic framework**, build and run your own agents (the Bot Builder) over email, Discord, and voice — local
> L80: Crow connects to the AI clients you already use as a native MCP server — not a middleware layer, not a plugin harne

## 星数曲线

```mermaid
xychart-beta
    title "kh0pper/crow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `89c088382c7f` · [字段定义](../../DATASET.md)*
