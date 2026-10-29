# EastStarAI/sanad-agent

⭐ 48 · Dart · MIT · 推送 2026-10-24 · [GitHub](https://github.com/EastStarAI/sanad-agent) · [官网](https://sanad.eaststarai.com) · 组织维护 · 中文 README

**本地优先的跨平台 AI agent，客户端统一管理多台电脑与服务器**

由 EastStar AI 开发的本地优先 AI agent：原生 Dart agent 运行在 macOS/Windows/Linux 上，通过 Flutter 桌面/移动/Web 客户端统一管理本机与远程配对设备的工作区与对话。支持 Ollama、LM Studio、llama.cpp 离线运行，可配置多 provider 多账户、运行中转向（steer）、并行隔离工作区、SOUL.md/MEMORY.md 记忆文件与 MCP 技能扩展，另含终端 REPL 与一次性任务 CLI。用户经安装包或 curl 脚本安装，开发者按 AGENTS.md 契约从源码构建；Windows 构建当前未签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生 Dart agent + Flutter 客户端管理多台电脑与无头服务器
- 配合 Ollama/LM Studio/llama.cpp 可离线运行对话与工具
- 运行中转向、排队任务、断连后可恢复的并行对话
- SOUL.md/USER.md/MEMORY.md 文件化记忆与 MCP/技能扩展

## 适用场景

- 在本机离线跑 AI agent 处理文件与工具操作
- 从手机或 Web 客户端管理多台远程电脑和服务器上的 agent
- 按工作区隔离上下文、权限与 provider 配置

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: Sanad Agent runs a native Dart agent close to your files and tools. Use it
> L242: Flutter Client
> L255: - `agent/` — native Dart CLI and background service that owns

## 星数曲线

```mermaid
xychart-beta
    title "EastStarAI/sanad-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-18 47 → 2026-10-29 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8875973bc03a` · [字段定义](../../DATASET.md)*
