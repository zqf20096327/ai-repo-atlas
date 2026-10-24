# CloudLLM-ai/mentisdb

⭐ 87 · Rust · MIT · 推送 2026-10-22 · [GitHub](https://github.com/CloudLLM-ai/mentisdb) · [官网](https://mentisdb.com) · 组织维护

**给 AI agent 的持久记忆引擎与版本化技能注册库**

面向 AI agent 的持久化语义记忆引擎：以追加写入、哈希链式（hash-chained）的记忆日志存储带类型的 thoughts，通过可替换的存储适配层落盘；另含 Git 式的不可变技能版本库，每次上传产生新版本（以 unified diff 存储），支持 Ed25519 签名验证来源与审计历史。多个 agent 可同时读写同一 chain key，通过 MCP/REST 与 Claude Code、Codex、GitHub Copilot CLI、Qwen Code、Cursor 等 MCP 客户端共享同一记忆。以 cargo 安装或预编译二进制/Docker 镜像提供，含 TUI 与 headless 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 追加写入、哈希链式记忆日志，跨上下文重置与模型切换保留记忆
- Git 式技能注册库：版本不可变、可签名、历史可审计
- 多 agent 并发读写同一 chain key，按 agent 身份/类型/标签/时间窗口查询
- 通过 MCP/REST 接入 Claude Code、Codex、Copilot CLI 等客户端共享同一 daemon

## 适用场景

- 让 coding agent 在上下文窗口写满后压缩并恢复工作状态
- 多 agent 团队共享同一份持久记忆与经验教训
- 对 agent 技能文件做带签名的版本管理与溯源

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: MentisDB is a **durable semantic memory engine and versioned skill registry** for AI agents — a persistent, hash-cha
> L7: It stores semantically typed thoughts in an append-only, hash-chained memory log through a swappable storage adapter
> L138: |Ports|`9471` MCP (HTTP), `9472` REST (HTTP), `9475` dashboard (HTTPS). HTTPS MCP/REST (`9473`/`9474`) are off in 

## 星数曲线

```mermaid
xychart-beta
    title "CloudLLM-ai/mentisdb 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 85 --> 88
    line [86, 87, 87]
```

2026-10-18 86 → 2026-10-24 87（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `9005821f7e22` · [字段定义](../../DATASET.md)*
