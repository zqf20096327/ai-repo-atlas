# BlinkZer0/LM-Studio-IDE-Plugin

⭐ 21 · TypeScript · MIT · 推送 2025-11-04 · [GitHub](https://github.com/BlinkZer0/LM-Studio-IDE-Plugin) · 个人维护

**把 LM Studio 等本地 LLM 接入 VS Code/Windsurf 的编码助手插件**

VS Code/Cursor/Windsurf 扩展，连接 LM Studio 及任意 OpenAI 兼容本地 LLM 服务器（如 Ollama），提供行内补全、聊天面板（@file/@selection/@workspace 指令）、命令面板动作（解释代码、生成测试、重构、执行 shell 命令等），并可桥接 Agent-Cascade MCP 服务器执行文件操作与命令，工具可用 allowlist 控制。需要 Node.js 20+ 构建，通过 VSIX 安装或从源码构建；本地 LLM 服务器为必要前置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于本地 LLM 的行内补全与聊天面板（@file/@selection/@workspace 指令）
- 命令面板动作：解释、生成测试、重构、应用 diff、执行 shell 命令
- Agent-Cascade MCP 工具桥接，支持工具 allowlist 安全配置
- 兼容任意 OpenAI 兼容服务器（LM Studio、Ollama 等）

## 适用场景

- 在 VS Code 中用本地模型获得行内补全和聊天问答
- 不依赖云端 API 在编辑器内生成测试、解释和重构代码
- 通过 MCP 工具让编辑器执行文件操作与终端命令

## 场景标签

`代码生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: A powerful VS Code extension that integrates LM Studio and other Local LLM servers with Agent-Cascade MCP tools, pro
> L47: 2. **Local LLM Server** - Any OpenAI-compatible server (LM Studio, Ollama, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "BlinkZer0/LM-Studio-IDE-Plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e4c75a818360` · [字段定义](../../DATASET.md)*
