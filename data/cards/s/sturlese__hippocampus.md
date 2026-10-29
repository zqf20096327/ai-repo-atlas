# sturlese/hippocampus

⭐ 29 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/sturlese/hippocampus) · [官网](https://github.com/sturlese/hippocampus) · 个人维护

**用编码代理把零散笔记整理成 Obsidian 知识库的轻量个人大脑模板**

一个刻意轻量的个人知识管理系统仓库模板：用户把杂乱笔记投入 inbox/，由 Claude Code（原生）或 Codex（支持）按 CLAUDE.md 中的契约整理为带 YAML frontmatter 和 wikilinks 的结构化 Obsidian vault，并以 hot.md 会话缓存、index.md 主索引、log.md 日志实现跨会话记忆与三步检索。不使用向量库、embedding、MCP 服务器或 Obsidian 插件，仅依赖一个 stdlib Python 脚本、shell hook、markdown 与 git；数据保留在用户私有 git 仓库中。Obsidian 仅作为浏览界面，附确定性 linter 与矛盾标记机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- inbox→ingest→wiki 整理流水线，类型化页面与 wikilink 交叉链接
- hot.md 会话缓存 + index.md 主索引 + log.md 追加日志的三件套检索与记忆机制
- 零依赖：仅一个 stdlib Python 脚本、shell hook、markdown 与 git
- 确定性 linter 检查死链、孤儿页、别名冲突与索引漂移

## 适用场景

- 把日常随手记的杂乱笔记整理为可检索的结构化知识库
- 让编码代理在终端里整理、查询和保存我的笔记
- 跨会话延续工作上下文（'我们上次进行到哪了'）
- 在多台机器间用私有 git 仓库同步个人知识库

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Drop messy notes into an inbox. Your coding agent consolidates them into a structured, cross-linked Obsidian vault —
> L39: **Requirements:** Claude Code (native) or Codex (supported) · git · Python 3.10+ · Obsidian (optional, for browsing

## 星数曲线

```mermaid
xychart-beta
    title "sturlese/hippocampus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2658b6d1eacf` · [字段定义](../../DATASET.md)*
