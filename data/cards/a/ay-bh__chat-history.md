# ay-bh/chat-history

⭐ 13 · Rust · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ay-bh/chat-history) · [官网](https://crates.io/crates/chat-history) · 个人维护

**供 AI agent 检索 Claude Code/Codex/Cursor 对话历史的 CLI**

Rust 编写的 CLI 工具，读取本机的 Claude Code、OpenAI Codex 与 Cursor 会话记录文件（jsonl/SQLite），提供会话列表、BM25 索引搜索、inspect/view/export/resume 等命令，并支持 JSON 与 compact 输出供 agent 解析。主要用法通过随附安装的 agent 技能（SKILL.md）调用，首次运行自动写入 ~/.claude/skills 与 ~/.agents/skills。沙箱环境下自动回退到可写临时目录缓存。经 cargo install 安装，评分逻辑移植自 claude-historian-mcp 等项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合 Claude Code / Codex / Cursor / Cursor IDE 四类本地会话数据源
- BM25 索引搜索，支持 --json / --compact 机器可读输出
- 首跑自动安装 SKILL.md agent 技能并支持自定义技能名
- 沙箱环境自动回退临时缓存目录，无需重启即生效

## 适用场景

- 让 Claude Code / Codex / Cursor agent 查询我之前讨论过的内容
- 按日期/来源/项目过滤并检索历史会话
- 导出或恢复（resume）指定会话
- 回顾近期项目工作摘要（inspect 输出时长、token、关键决策）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: CLI for **agents** to search, inspect, and export **Claude Code**, **OpenAI Codex**, and **Cursor** conversation his
> L5: Most usage is via an agent skill (`SKILL.md`) that tells Claude Code / Codex / Cursor when and how to call this tool

## 星数曲线

```mermaid
xychart-beta
    title "ay-bh/chat-history 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6f1332da6cc2` · [字段定义](../../DATASET.md)*
