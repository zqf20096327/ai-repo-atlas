# VoDaiLocz/kilo-kit-mcp

⭐ 28 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/VoDaiLocz/kilo-kit-mcp) · [官网](https://glama.ai/mcp/servers/VoDaiLocz/kilo-kit-mcp/) · 个人维护

**MCP 服务器与监督引擎：为 AI 编码 agent 加治理护栏**

面向 AI 编码助手（GitHub Copilot、Cursor、Windsurf、Claude Code、Gemini CLI）的 Model Context Protocol (MCP) 服务器，通过 stdio/JSON-RPC 接入各 MCP 兼容客户端。核心机制包括 C4 五门生命周期（探测、推理、审批、守卫执行、验证反思）、未读文件修改的协议级拒绝（Grounding Lock）、连续相同动作 3 次触发熔断、SQLite FTS5 BM25 跨会话记忆，以及 20/80 智能截断。提供 24 个 MCP 工具与 180 个技能目录，通过 npx 或 npm 全局安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C4 五门生命周期与 4 层任务分级执行路径
- 协议级拒绝未读文件修改、3 次重复动作熔断等监督护栏
- SQLite FTS5 BM25 跨会话持久记忆（亚毫秒检索）
- 24 个 MCP 工具与 180 个内置技能，含技能自动合成

## 适用场景

- 为 Cursor/Copilot/Claude Code 等 MCP 客户端加编码护栏，防止盲改与无限循环
- 让编码 agent 跨会话记住已验证的修复与架构决策
- 在完成前强制执行测试与 Playwright 验证

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: Kilo-Kit is an enterprise-grade Model Context Protocol (MCP) server and supervisor engine that transforms raw LLM c
> L73: [ Host AI Agent: Cursor / Copilot / Windsurf / Claude / Gemini ]

## 星数曲线

```mermaid
xychart-beta
    title "VoDaiLocz/kilo-kit-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `43ef10b0e174` · [字段定义](../../DATASET.md)*
