# danishashko/make-mcp

⭐ 10 · TypeScript · MIT · 推送 2026-02-14 · [GitHub](https://github.com/danishashko/make-mcp) · [官网](https://www.npmjs.com/package/make-mcp-server) · 个人维护

**让 AI 助手检索、校验并部署 Make.com 自动化场景的 MCP 服务器**

非官方、社区维护的 MCP 服务器，向 Claude Desktop、GitHub Copilot、Cursor 等 MCP 客户端提供 Make.com 模块文档检索（内置 200+ 模块的 SQLite FTS5 数据库）、场景蓝图校验、账户/区域兼容性检查，以及通过 Make.com API 一键部署场景。提供自动修复 LLM 生成蓝图的自愈机制与 BasicRouter 多路由支持。部署需配置 MAKE_API_KEY 与 MAKE_TEAM_ID；不配置凭据时仍可用文档、搜索与校验工具。通过 npx、Docker 或源码运行。

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

- 内置 200+ Make.com 模块文档的全文检索（SQLite FTS5）
- 部署前蓝图校验与账户/区域模块兼容性检查
- 自动修复 LLM 生成蓝图的 auto-healing（补 metadata、剥离不支持的属性）
- 支持 builtin:BasicRouter 多路由与递归校验

## 适用场景

- 在对话中让 AI 助手生成并校验 Make.com 自动化场景
- 部署前检查模块在当前账户/区域是否可用
- 按自然语言描述走引导式流程搭建场景

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8: A Model Context Protocol (MCP) server that gives AI assistants like **Claude**, **GitHub Copilot**, and **Cursor** f
> L16: - **🚀 Deploy to Make.com** — Push validated blueprints directly to Make.com via API


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `b5b9ef5d5626` · [字段定义](../../DATASET.md)*
