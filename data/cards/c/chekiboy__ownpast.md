# chekiboy/ownpast

⭐ 4 · Python · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/chekiboy/ownpast) · 个人维护

**本地优先的 AI agent 记忆与身份运行时**

Whaat 是一个本地优先的 AI Identity Runtime：为基于 CLI 的 AI agent 提供跨会话的持久记忆、日志、身份隔离与会话生命周期管理。记忆以 markdown 文件存于本地 Git 仓库，每次变更生成 commit，可审查回滚；记忆分层（全局/仓库组/单仓库/个人）并带时效衰减评分。通过 Claude Code 插件与 MCP server 接入，提供浏览器应用、CLI、本机 JSON API 等接口。运行于 macOS，Linux 仅在容器中测试过；版本 0.5.0，README 自述为早期软件，API/CLI/文件格式在 1.0 前可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 记忆以 markdown 文件存于本地 Git 仓库，每次变更记录为可回滚的 commit
- 记忆分层与 Truthness/Validity 评分，每 30 天衰减 0.2，确认与成功使用可回馈
- 通过 Claude Code hooks 强制记忆读写经运行时记录，并提供结构化人工审批的 curation 流程
- whaat mcp 以 MCP 协议向任意 stdio MCP 客户端提供同一套记忆/日志/报告调用

## 适用场景

- 让编码 agent 在新会话中记住此前的纠错与项目陷阱
- 为多个 agent 身份各自维护独立的记忆库与 token 隔离
- 定期审查 agent 记忆质量并批准合并、移动、修正建议

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Whaat is an **AI Identity Runtime**: a local-first system that gives AI agents persistent memory and identity contin
> L21: |Category|AI Identity Runtime: persistent AI memory and identity continuity for AI agents|
> L26: |Interfaces|An app (in a browser or its own window), the `whaat` command line, a JSON API on 127.0.0.1, an MCP serv


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `7a43e761d282` · [字段定义](../../DATASET.md)*
