# DazzleML/Claude-Session-Backup

⭐ 16 · Python · GPL-3.0 · 推送 2026-09-09 · [GitHub](https://github.com/DazzleML/Claude-Session-Backup) · 个人维护

**Claude Code 会话的 git 备份与恢复 CLI（csb）**

Python CLI 工具 csb，备份 ~/.claude/projects/ 下的 Claude Code 会话 JSONL 及 ~/.claude/ 全部内容到 git 仓库，建 SQLite/FTS5 元数据索引；提供时间线视图、文件夹分析、删除检测、会话恢复（字节+元数据精确还原，含 transcript、子代理、工具结果）、IM 风格聊天记录阅读层（distill）、fork 谱系树与重启前会话恢复。自动化靠 Claude Code 插件（PreCompact/SessionEnd 钩子）与 OS 定时任务。需 Python 3.10+ 与 git，跨 Windows/Linux/macOS/BSD，自述为 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- git 为事实来源、SQLite 为可重建索引的备份架构
- 删除会话的完整足迹恢复（transcript/子代理/工具结果/时间戳）
- FTS5 全文会话搜索与 distill 可读聊天日志层
- Claude Code 插件钩子 + OS 调度器双层自动备份

## 适用场景

- 防止 Claude Code 升级或 /compact 导致会话历史丢失
- 按名称/内容/时间线检索与阅读历史会话
- 从 git 历史恢复被删除的会话并继续使用
- 查看会话 fork 谱系与重启前的工作现场

## 场景标签

 · 领域:开发者工具/AI 会话数据管理

## 证据(README 行号)

> L12: **Git-backed Claude Code session backup with timeline view, folder analysis, deletion detection, and session restor
> L18: **csb** preserves every session in your existing `~/.claude` git repository, builds a searchable metadata index, de
> L170: **Key principle**: Git is the source of truth. The SQLite database is a rebuildable index for fast queries. If the

## 星数曲线

```mermaid
xychart-beta
    title "DazzleML/Claude-Session-Backup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `78a7bd767b5c` · [字段定义](../../DATASET.md)*
