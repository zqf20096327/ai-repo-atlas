# mvplab-ai/agentdream

⭐ 19 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/mvplab-ai/agentdream) · [官网](https://agentdream.dev) · 组织维护

**给 AI agent 做睡眠期记忆整理的 CLI/库：合并去重、纠错、出报告**

agentdream 读取 agent 已有的记忆存储（markdown 文件夹、JSON/JSONL、SQLite、stancelog）与会话转录，经 load→redact→consolidate→verify→insights 流水线生成一份暂存的新存储与报告：合并重复、替换过时值、以转录 file:line 引用为证修正错误笔记、归纳跨会话模式。输入存储只读，默认 dry-run，可整体/部分接受或丢弃，接受前自动备份。零依赖，LLM 后端失败时回退到确定性规则，另可作为 MCP server 与 Claude Code 集成。

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

- 确定性规则与 LLM 后端双路径，模型不可用时自动回退启发式
- 每处修改带转录 file:line 引证，操作以内容哈希为稳定 id，可选择性接受
- 只读输入+暂存输出+备份，dry-run 默认，可恢复
- 以 CLI、Python 库和 MCP server 三种形态提供

## 适用场景

- 清理 Claude Code 项目里积累重复、过时的 CLAUDE.md/记忆目录
- 对 JSON/SQLite 形式的 agent 记忆库做批量纠错并逐条审阅
- 离线环境下用规则引擎整理记忆存储
- 通过 MCP 让 Claude 按需对记忆执行 dream 并查看报告

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L149: agentdream is a **maintenance pass** over a memory store you already have. It is not a new memory
> L155: |**agentdream**|Sleep-time consolidation CLI / library / MCP server|Your machine (stdlib-only; optional local or A
> L9: **Sleep-time memory consolidation ("dreaming") for any agent and any model — local-first, reviewable, zero dependenc


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `0b7a7ad2aa6c` · [字段定义](../../DATASET.md)*
