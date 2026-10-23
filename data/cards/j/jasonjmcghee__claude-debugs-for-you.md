# jasonjmcghee/claude-debugs-for-you

⭐ 514 · TypeScript · MIT · 推送 2025-12-20 · [GitHub](https://github.com/jasonjmcghee/claude-debugs-for-you) · [官网](https://marketplace.visualstudio.com/items?itemName=JasonMcGhee.claude-debugs-for-you) · 个人维护

**让 Claude 等 LLM 通过 MCP 在 VS Code 中交互式调试代码**

由 MCP Server 与 VS Code 扩展两部分组成，使 Claude（或任何具备工具调用能力的 LLM/MCP 客户端）能够以交互方式调试代码：设置断点（含条件断点）、评估表达式、逐步定位问题。语言无关，前提是 VS Code 调试控制台支持且有有效的 launch.json。提供 stdio 与 SSE 两种接入方式，作者仅在 Claude Desktop 与 Continue 中演示，也适用于 Cursor 等内置客户端；多窗口间可交接、可关闭自启动。通过 VS Code Marketplace 或 .vsix 安装，开发构建用 npm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP Server + VS Code 扩展，支持断点与表达式评估的交互式调试
- 语言无关，依赖 VS Code 调试器与 launch.json 配置
- 支持 stdio（Claude Desktop）与 SSE（Cursor 等）两种接入方式
- 支持条件断点，多 VS Code 窗口间可交接运行

## 适用场景

- 让 Claude Desktop / Continue 代我逐步调试并定位代码 bug
- 在 Cursor 等 MCP 客户端中接入调试工具
- 通过提示词驱动 AI 用断点和表达式评估而非猜测地排查问题

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: This is an MCP Server and VS Code extension which enables claude to interactively debug and evaluate expressions.
> L13: It's language-agnostic, assuming debugger console support and valid launch.json for debugging in VSCode.

## 星数曲线

```mermaid
xychart-beta
    title "jasonjmcghee/claude-debugs-for-you 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 513 --> 516
    line [515, 514]
```

2026-10-18 515 → 2026-10-23 514（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `997d100c8ce7` · [字段定义](../../DATASET.md)*
