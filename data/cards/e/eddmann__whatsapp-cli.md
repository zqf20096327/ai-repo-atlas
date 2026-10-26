# eddmann/whatsapp-cli

⭐ 27 · Go · MIT · 推送 2026-05-26 · [GitHub](https://github.com/eddmann/whatsapp-cli) · [官网](https://eddmann.com/whatsapp-cli/) · 个人维护

**终端 WhatsApp 客户端 CLI，可作 AI agent 技能使用**

Go 编写、基于 whatsmeow 的 WhatsApp 命令行工具：以 QR 码登录后支持会话/消息/联系人/群组/媒体的读取、搜索、发送、转发、导出与持续同步；数据存储于本地 SQLite（FTS5）与媒体目录。输出支持 JSON/JSONL/CSV/TSV/human 格式，可通过 jq、管道与 Unix 工具组合脚本化。另以 Agent Skill 形式适配 Claude Code、Cursor 等 AI 代理，安装后由代理自动调用。提供安装脚本、Homebrew 与源码编译三种安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖聊天、消息、搜索、发送、群组、导出等 WhatsApp 全量数据操作
- JSON/JSONL/CSV/TSV/human 多格式输出，可组合 jq/管道/Unix 工具
- 以 Agent Skill 形式适配 Claude Code、Cursor 等 AI 代理
- 本地 SQLite（FTS5）存储会话与消息，支持持续同步守护模式

## 适用场景

- 在终端查询、搜索和收发 WhatsApp 消息
- 用管道和 jq 脚本化处理 WhatsApp 数据
- 让 Claude Code / Cursor 等代理通过技能直接操作我的 WhatsApp

## 场景标签

 · 领域:通讯/命令行工具

## 证据(README 行号)

> L13: - AI agent ready — install the skill for Claude, Cursor, and other assistants
> L176: This CLI is available as an Agent Skill — it works with Claude Code, Cursor, and other compatible AI agents. See `
> L202: This project is an exploration of Claude Code Skills and the emerging Agent Skills standard for AI-tool interopera

## 星数曲线

```mermaid
xychart-beta
    title "eddmann/whatsapp-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1ce2d148369d` · [字段定义](../../DATASET.md)*
