# Daily-Nerd/daimon

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Daily-Nerd/daimon) · [官网](https://daily-nerd.github.io/daimon/) · 组织维护

**AI 编码代理的会话记忆工具：会话末写检查点，会话初生成简报**

面向 Claude Code、Codex、Kimi Code、Windsurf、Gemini CLI 等 AI 编码代理宿主的记忆工具。会话结束时写入认知检查点，下次会话开始时自动注入一份可快速浏览的续接简报，使代理从先验状态恢复。每条记忆标注信任类别（逐字引用/推断），逐字项锁定原文不改写；提供全文检索 recall、溯源检查 why、代码锚点 anchor、否定知识台账 refute、可选的团队记忆（git 远端镜像）与离线签名收据。无嵌入、无图数据库、无必需守护进程，按项目存 JSON 加 SQLite FTS5 索引。以 pip/uv 安装的 CLI 与 Claude Code 插件形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 会话末写检查点、会话初注入续接简报
- 逐字/推断双信任类别，逐字项不可被改写或截断
- recall 全文检索、why 溯源检查、anchor 代码锚点、refute 否定知识台账
- 无嵌入/图数据库/必需守护进程，按项目 JSON + SQLite FTS5，离线优先

## 适用场景

- 跨会话恢复 AI 编码代理的工作上下文
- 检索与审计代理历史决策及其出处
- 小团队通过 git 远端共享代理记忆（可选项）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: Your agent forgets everything between sessions. Daimon writes a small cognitive checkpoint when a session ends and 
> L85: - **Trust-classed, quote-pinned memory:** every briefing item is marked verbatim (exact quote, immutable everywhere

## 星数曲线

```mermaid
xychart-beta
    title "Daily-Nerd/daimon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9c8c4f70d971` · [字段定义](../../DATASET.md)*
