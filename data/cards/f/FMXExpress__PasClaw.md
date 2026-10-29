# FMXExpress/PasClaw

⭐ 64 · Pascal · MIT · 推送 2026-10-26 · [GitHub](https://github.com/FMXExpress/PasClaw) · [官网](https://pasclaw.dev/) · 个人维护 · 中文 README

**Object Pascal 编写的超轻量个人 AI agent 框架**

以 Delphi/FPC Object Pascal 实现的命令行个人 AI agent，功能包括工具调用、MCP 集成（客户端与服务器两种角色）、HTTP 网关、OpenAI 兼容 API、内嵌 Web UI、定时任务、技能系统与频道集成。提供约 26 个 LLM 提供商目录（含 OpenAI 协议兼容端点）、回退链与离线难度路由。编译为单个 4-5 MB 二进制（运行依赖仅 libsqlite3 与 OpenSSL），也提供 Docker 镜像。面向希望嵌入或本地运行 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件 4-5 MB 原生二进制，运行时依赖仅 libsqlite3 与 OpenSSL
- 约 26 个 LLM 提供商目录，支持 OpenAI 协议兼容端点
- MCP 双角色：客户端（Stdio/HTTP）与 MCP 服务器，暴露记忆/知识库检索给其他客户端
- 内置工具集：沙箱文件系统、shell 执行、BM25+本地向量混合记忆检索、子 agent 分发

## 适用场景

- 本地运行带工具调用的命令行 AI 助手
- 通过 OpenAI 兼容网关为其他客户端（如 Codex CLI）提供模型接入
- 在 Object Pascal 项目中嵌入 agent 能力
- 通过内嵌 Web UI 在浏览器中完成配置与对话

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L3: PasClaw is an ultra-lightweight personal AI agent written in Delphi Object Pascal. It is a Delphi/FPC port inspired 
> L32: **LLM providers** — ~26-entry catalog covering Anthropic Messages, OpenAI Chat Completions, Google Gemini `generate

## 星数曲线

```mermaid
xychart-beta
    title "FMXExpress/PasClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-18 63 → 2026-10-29 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `46cc1c915623` · [字段定义](../../DATASET.md)*
