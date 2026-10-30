# VikrantSingh01/adaptive-cards-mcp

⭐ 33 · TypeScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/VikrantSingh01/adaptive-cards-mcp) · [官网](https://www.npmjs.com/package/adaptive-cards-mcp) · 个人维护

**帮 AI 助手生成/校验 Adaptive Cards 的 MCP 服务器**

TypeScript 实现的 MCP 服务器，为 Claude Code、GitHub Copilot、Cursor、Windsurf、Copilot Studio、ChatGPT 等 AI 客户端提供 9 个工具：从自然语言或数据生成合法 Adaptive Card JSON、校验 schema 与无障碍性并给出宿主兼容矩阵（Teams/Outlook/Webex 等 7 宿主版本上限）、优化、模板化与版本升降级，另含 3 个引导式 prompt 工作流与 5 类资源。通过 npx 免安装运行，支持 stdio/SSE 传输；也可 npm 安装作为库用于自有代码。MCP 场景下无需 API key，独立/库用法可配置 Anthropic/OpenAI/Azure/Ollama。

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

- 9 个 MCP 工具：生成、校验（schema+无障碍+宿主兼容）、数据转卡片、优化、模板化、版本转换等
- 7 宿主兼容矩阵（Teams 1.6 / Outlook 1.4 / Webex 1.3 等）
- npx 免安装运行，支持 stdio/SSE 传输与 HTTP API key 认证
- 21 个布局模式与 36 个示例卡片资源，924 项测试

## 适用场景

- 在 Claude Code/Copilot/Cursor 中用自然语言生成 Teams 审批、CI/CD 通知等卡片
- 校验既有卡片在不同宿主和版本下的兼容性与无障碍问题
- 把 API/CSV 数据转换为表格或 FactSet 卡片

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: An MCP server that helps AI assistants generate valid, accessible Adaptive Cards for Teams, Outlook, Copilot, and o
> L354: > **Note:** When used via MCP (Claude Code, Copilot, Cursor), the host LLM provides the intelligence — no API key 

## 星数曲线

```mermaid
xychart-beta
    title "VikrantSingh01/adaptive-cards-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `032f3add7ce8` · [字段定义](../../DATASET.md)*
