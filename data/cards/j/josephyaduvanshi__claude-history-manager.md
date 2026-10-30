# josephyaduvanshi/claude-history-manager

⭐ 49 · Swift · NOASSERTION · 推送 2026-04-26 · [GitHub](https://github.com/josephyaduvanshi/claude-history-manager) · [官网](https://github.com/josephyaduvanshi/claude-history-manager) · 个人维护

**macOS 原生应用：浏览检索 Claude Code/Codex/Gemini CLI 会话历史**

Chronicle 是 SwiftUI 编写的 macOS 原生桌面应用，直接读取 Claude Code、Codex CLI、Gemini CLI 三种 CLI 编码助手在本地目录中的会话记录，解析为标题、token 用量、模型、工具调用等元数据后写入本地 SQLite（GRDB + FTS5）索引。提供全文检索与斜杠过滤器、九类彩色工作区分组、智能文件夹、置顶/标签/归档、Markdown 转写视图、token 与费用统计面板，并可一键在任意终端恢复会话。各 provider 数据相互隔离，转写文件不离开本机。另有 Linux/macOS 伴随 CLI（无 SQLite 索引，按需读 JSONL）。要求 macOS 15.0+，应用为 ad-hoc 签名未经公证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取三种 CLI 助手的本地会话存储并索引到 SQLite FTS5
- 置顶/标签/归档/软删除与一键在终端恢复会话
- 智能文件夹与 /full:、/tag:、/model: 等组合过滤器
- Linux/macOS 伴随 CLI，四命令按需读 JSONL

## 适用场景

- 在数千条 Claude Code/Codex/Gemini 会话中快速找到解决某问题的那次会话
- 按项目统计 token 用量与估算费用
- 在远程 Linux 开发机上用 CLI 检索会话转写

## 场景标签

 · 领域:开发者工具/AI 会话管理

## 证据(README 行号)

> L7:  A native macOS browser for your CLI coding-assistant session history — Claude Code, Codex CLI, and Gemini CLI.
> L37: Three CLI coding assistants, three different transcript formats, all sitting in different corners of your home dire
> L154: Chronicle is a SwiftUI app on top of two boring layers. Parsers read each provider's transcript format. Claude and

## 星数曲线

```mermaid
xychart-beta
    title "josephyaduvanshi/claude-history-manager 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-30 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2c1c41a6dfb9` · [字段定义](../../DATASET.md)*
