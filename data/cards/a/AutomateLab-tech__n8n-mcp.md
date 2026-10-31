# AutomateLab-tech/n8n-mcp

⭐ 15 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/AutomateLab-tech/n8n-mcp) · [官网](https://automatelab.tech/products/mcp/n8n-mcp/) · 组织维护

**面向 AI agent 的 n8n 工作流调试 MCP 服务器**

为 Claude、Cursor 等 MCP 客户端提供 12 个操作 n8n 的工具：7 个无状态工具（自然语言生成工作流 JSON、20+ 规则 lint、失败执行逐节点诊断、语义 diff、节点回放等），5 个 REST 工具需配置 N8N_API_URL/API_KEY 以驱动在线 n8n 实例（列出/获取/创建/激活工作流、拉取执行记录）。附运行时策略环境变量（只读模式、禁用工具、工作流白名单）、配套 Agent Skill 与两个示例工作流。以 npm CLI、Docker、DXT 包及 Render/Railway/Fly 配置形式提供，需 Node 20+。

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

- execution_explain 对失败执行做逐节点诊断（0 items、未解析表达式、具体提示）
- workflow_lint 含 20+ 规则（废弃节点类型、AI Agent 缺语言模型、IF v1 schema 等）
- 5 个 REST 工具可驱动在线 n8n 实例
- 运行时策略环境变量：只读模式、禁用工具、工作流 ID/标签白名单

## 适用场景

- 让 Claude/Cursor 里的 agent 生成可直接导入 n8n 的工作流 JSON
- 诊断 n8n 失败执行中节点间静默丢数据的问题
- 在 CI 中用 GitHub Action 对工作流做 lint 与诊断

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: An MCP server for n8n that gives Claude, Cursor, and other AI agents tools for generating workflows, linting, diagno
> L30: Tool names follow dot-notation and form a navigable tree: `node.*`, `workflow.*`, `execution.*`. Every tool declare
> L32: **Stateless** (work without a live n8n instance):

## 星数曲线

```mermaid
xychart-beta
    title "AutomateLab-tech/n8n-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e6fd090c9e9d` · [字段定义](../../DATASET.md)*
