# OrionStarAI/EasyCode

⭐ 422 · TypeScript · Apache-2.0 · 推送 2026-06-17 · [GitHub](https://github.com/OrionStarAI/EasyCode) · [官网](https://easycode.bot) · 组织维护 · 中文 README

**给开发者的 CLI/VS Code AI 编程助手，支持多模型接入与任务派发**

面向开发者的智能编程助手，以 CLI（终端交互）与两个 VS Code 扩展形式提供。基于 MCP 协议构建项目级上下文，AI 可通过内置工具集执行文件操作、Shell 命令、网页抓取等操作，敏感操作需用户确认。支持 OpenAI 兼容格式与 Anthropic Claude API 自定义模型，可接本地模型（LM Studio、Ollama）。提供会话持久化、检查点回滚、Hooks/Skills 扩展机制，并可作为 ACP 编排方将任务派发给本机 Claude Code 或 Codex 执行，支持飞书网关模式与多会话管理。需 Node.js 20+，通过 npm 全局安装或源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 协议构建项目级上下文，支持第三方 MCP 服务器接入（标准/Streamable HTTP 两种模式）
- OpenAI 兼容与 Anthropic Claude 格式自定义模型，支持本地模型（LM Studio、Ollama）
- CLI + 两个 VS Code 扩展（轻量伴侣与完整图形化插件）
- 可作为 ACP 编排方将任务派发给本机 Claude Code / Codex，支持飞书网关与多会话管理

## 适用场景

- 在终端或 VS Code 中通过对话让 AI 生成、重构、修复代码
- 接入自选模型服务（含本地 Ollama/LM Studio）进行编码协作
- 通过飞书远程驱动本机编码 agent 并管理多会话任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L24: **Easy Code** 是一款革命性的 AI 驱动智能编程助手，通过深度整合人工智能技术，全面提升软件开发的效率、质量和创新能力。
> L63: - **智能代码生成** - 根据自然语言描述生成完整的函数、类、模块甚至整个应用
> L510: Easy Code 支持配置 OpenAI 兼容格式和 Anthropic Claude API 格式的自定义模型，让你可以使用任何兼容的 AI 服务。

## 星数曲线

```mermaid
xychart-beta
    title "OrionStarAI/EasyCode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 421 --> 423
    line [422, 422]
```

2026-10-18 422 → 2026-10-22 422（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `de63bebea8e0` · [字段定义](../../DATASET.md)*
