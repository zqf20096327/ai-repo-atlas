# lee-fuhr/claude-session-index

⭐ 31 · Python · MIT · 推送 2026-03-21 · [GitHub](https://github.com/lee-fuhr/claude-session-index) · 个人维护

**为 Claude Code 会话建立全文索引与搜索分析的工具**

读取 ~/.claude/projects/ 下的 JSONL 会话文件，解析后存入 SQLite（FTS5 全文索引），提供内容、项目、工具、代理、日期等多维检索、会话上下文抽取、使用量分析与跨会话综合（通过会话内 Haiku 子代理，不产生额外 API 费用）。使用方式为 Claude Code 技能（SKILL.md）+ `sessions` CLI，支持 Claude Code hooks 实时主题采集和 macOS LaunchAgent 后台增量索引。核心功能仅依赖 Python 3.10+ 标准库，无需服务器与 API key。

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

- SQLite + FTS5 对全部 Claude Code 会话做毫秒级全文检索
- 跨会话综合：提取多次尝试的成功/失败结论（Haiku 子代理，无额外 API 成本）
- 使用量分析：按客户/项目的时长、工具调用趋势、主题模式
- 核心功能仅用 Python 标准库，无服务器、无数据库配置、无 API key

## 适用场景

- 找回上次调试某问题时的做法与结论
- 跨会话汇总某个任务尝试过哪些方案、哪些有效
- 统计每周会话时长、工具使用与主题分布
- 通过 claude --resume 链接直接跳回历史会话

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L70: 1. **Indexes** all your Claude Code sessions into SQLite with FTS5 full-text search
> L191: - Claude Code (the sessions to index)

## 星数曲线

```mermaid
xychart-beta
    title "lee-fuhr/claude-session-index 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d2f182c1fa1f` · [字段定义](../../DATASET.md)*
