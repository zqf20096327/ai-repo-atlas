# DollhouseMCP/mcp-server

⭐ 46 · TypeScript · AGPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/DollhouseMCP/mcp-server) · [官网](https://www.npmjs.com/package/@dollhousemcp/mcp-server) · 组织维护

**面向 MCP 客户端的 AI 人格/技能模块管理与权限控制服务器**

以 MCP 服务器形式运行的 AI 定制工具：通过本地 portfolio 文件夹管理 6 类元素（人格、技能、模板、代理、记忆、组合），支持用自然语言创建、编辑、激活元素，并可从社区集合安装他人作品。核心机制包括：将操作归并为 5 个语义端点（CRUDE）的 MCP-AQL 查询语言以减少 token 消耗；服务端 Gatekeeper 权限系统，由激活元素的策略控制操作许可，deny 优先且客户端无法覆盖。兼容 Claude Code、Claude Desktop、Cursor、Codex 等多种 MCP 客户端，高级功能在 Claude Code 上测试较多，其他平台未全部验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 6 类模块化元素（人格/技能/模板/代理/记忆/组合）本地 portfolio 管理
- MCP-AQL 将全部操作归并为 5 个语义端点，自述 token 消耗约降 85%
- 服务端 Gatekeeper 权限系统，元素策略优先于客户端授权
- Dollhouse Skills 与 Anthropic agent skills 格式的双向无损转换器

## 适用场景

- 给 Claude Code/Cursor 等 MCP 客户端安装并切换 AI 人格与技能
- 用本地 portfolio 管理自建或社区共享的 AI 定制元素
- 通过元素策略限制 AI 会话的操作权限（如只读沙箱）

## 场景标签

`提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L45: DollhouseMCP installs on any MCP-compatible AI client — Claude Code, Claude Desktop, Cursor, Gemini, Codex, and loc
> L122: **MCP-AQL** (Model Context Protocol – **A**dvanced **A**gent **A**PI **A**dapter **Q**uery **L**anguage) organizes

## 星数曲线

```mermaid
xychart-beta
    title "DollhouseMCP/mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-25 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e7e59e8b23b1` · [字段定义](../../DATASET.md)*
