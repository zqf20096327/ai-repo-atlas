# julioczn/graphite

⭐ 7 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/julioczn/graphite) · [官网](https://julioczn.github.io/graphite/) · 个人维护

**面向开发者与 DBA 的多数据库桌面客户端，带 AI 助手与 MCP 服务**

基于 Electron 的键盘友好型桌面 SQL 客户端，支持 SQLite、PostgreSQL、MySQL、Oracle、MongoDB、Redis、DynamoDB 等 24 种数据库，提供 SQL 编辑器、表浏览器、行内编辑、ER 图、备份恢复与导出。AI 部分：内置聊天助手经 Anthropic API 或任意 OpenAI 兼容端点（含 Ollama、LM Studio 本地模型）读取 schema、执行只读查询并给出 SQL；同时暴露仅监听 127.0.0.1 的 MCP 服务器供 Claude Code、Cursor 等外部 agent 使用。写入操作须经审批对话框确认，读取由数据库自身的只读模式强制执行。提供 macOS/Windows/Linux 安装包与 AppImage，无遥测，密码经系统钥匙串加密。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 24 种 SQL、NoSQL 与云端仓库数据库的统一连接与编辑
- 内置 AI 助手与 MCP 服务器共享同一组 schema/查询工具
- 写操作审批对话框，读操作由数据库端只读模式强制
- 导入 DBeaver、TablePlus、Navicat 等十余种工具的已存连接

## 适用场景

- 用一个桌面应用统一管理多种数据库连接与查询
- 让 AI 助手或外部 agent 以只读优先方式协助写 SQL
- 团队通过 GitHub 私有仓库同步工作区与保存的查询

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5:  A fast, keyboard-friendly desktop client for 24 databases : SQL, NoSQL and cloud warehouses
> L83: ## AI: bring your own model or agent
> L104: - **Anything else** opens an **approval dialog** in Graphite showing who asked, the connection and every statement


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `c2a7e45fa16c` · [字段定义](../../DATASET.md)*
