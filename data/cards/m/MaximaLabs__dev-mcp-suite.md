# MaximaLabs/dev-mcp-suite

⭐ 96 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/MaximaLabs/dev-mcp-suite) · [官网](https://maximalabs.tech) · 个人维护

**给 AI 编程助手加持久记忆与会话交接的本地 MCP 服务器套件**

面向独立开发者与 vibe coder 的四个本地 MCP 服务器（另含可选 Armada 集群控制面）：project-memory 提供 Obsidian 兼容 Markdown 知识库与本地 384 维向量检索；devjournal 记录会话进度、保存交接并恢复上下文；checkpoint 提供独立于 git 的文件快照与回滚；context-pack 提供省 token 简报、依赖影响分析与安全审计。一条 init 命令自动写入各 MCP 客户端配置，数据全部本地存储，无遥测。

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

- 一条 npx init 命令自动配置 Codex CLI、Claude Code、Cursor 等客户端
- 本地零依赖 384 维向量检索，可完全离线运行（MCP_DETERMINISTIC_FALLBACK）
- journal_handoff/journal_resume 实现跨会话上下文交接与恢复
- git 之外的 checkpoint 快照与一键回滚，pack_audit 检查泄露密钥

## 适用场景

- AI 会话重置后不想反复解释项目架构
- 让 AI 重构代码前先建立可回滚的文件快照
- 离线或无 API key 环境下做本地语义检索

## 场景标签

`Agent 记忆` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L20: **Dev MCP Suite** is a suite of four local, zero-telemetry MCP (Model Context Protocol) servers built for solo deve
> L54: |🛰️ **`armada`** *(opsional)*|**Fleet Ops Control Plane**: Watch heartbeats and enqueue policy-gated jobs on many h


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `350f2eda57bc` · [字段定义](../../DATASET.md)*
