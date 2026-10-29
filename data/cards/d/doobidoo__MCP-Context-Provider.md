# doobidoo/MCP-Context-Provider

⭐ 31 · TypeScript · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/doobidoo/MCP-Context-Provider) · 个人维护

**给 Claude 提供持久化上下文的 MCP 服务器：跨会话保留工具规则与习得规则**

TypeScript 实现的静态 MCP 服务器，向 Claude Desktop 与 Claude Code 提供两类持久化数据：Contexts（手工编写的静态工具规则 JSON）与 Instincts（从会话中提炼、带置信度评分、需人工批准的习得规则 YAML）。含四个子系统：加载合并的 Engine、stdio/HTTP 双传输的 MCP 服务器（10 个工具）、管理 instinct 生命周期的 CLI mcp-cp、以及可选同步到 mcp-memory-service 的 Memory Bridge。通过 git clone + npm 构建安装，或从 Claude Code 插件市场安装；状态自述为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Contexts（静态规则）与 Instincts（习得评分规则）双概念体系
- stdio + HTTP 双传输，10 个 MCP 工具
- /instill 技能从会话中提炼习得规则，需人工批准生效
- 自动触发 hook 监测用户纠正与工具失败并提示提炼

## 适用场景

- Claude Desktop/Code 每次新会话不再重复交代工具偏好与规则
- 从历史会话沉淀可复用的工作模式并逐步累积置信度
- 团队为特定工具（如 git）注入统一的静态使用规则

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: A TypeScript MCP server that gives Claude persistent **Contexts** (static tool rules) and **Instincts** (learned, co
> L23: - **MCP Server** (`src/server/index.ts`) — stdio + HTTP transport, 10 MCP tools

## 星数曲线

```mermaid
xychart-beta
    title "doobidoo/MCP-Context-Provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8ec90488e749` · [字段定义](../../DATASET.md)*
