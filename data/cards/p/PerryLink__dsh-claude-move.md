# PerryLink/dsh-claude-move

⭐ 29 · JavaScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/PerryLink/dsh-claude-move) · [官网](https://perrylink.github.io/plugins/dsh-claude-move/) · 个人维护 · 中文 README

**把 Claude Code 等四源会话迁移进 DeepSeek Harness 的 DSH 插件**

面向 DeepSeek Harness（DSH）的插件：自动扫描 ~/.claude 等数据目录，把 Claude Code、Codex、OpenCode、Hermes 的会话、记忆、技能、指令与斜杠命令导入为可恢复的 DSH 会话。提供 /move 向导（detect→preview→run）、Web 迁移面板、增量幂等导入、审批门控与冲突处理（默认 skip），并支持把 DSH 会话导出回 Claude JSONL。全程只读源数据；限定 dsh 0.1.x–0.2.x 兼容带，需 Node ^22.19||>=24。仓库描述标注自 2026-10-05 起维护冻结。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四源迁移向典 /move：检测→预览→审批执行→报告
- 会话/记忆/技能/斜杠命令的完整映射，导入后可直接续聊
- 幂等增量导入与冲突四选一处理（skip/overwrite/rename/merge）
- 双向导出：DSH 会话可写回可恢复的 Claude JSONL

## 适用场景

- 从 Claude Code 切换到 DSH 时保留全部历史会话与技能
- 在 DSH 中继续最近的 Claude 会话
- 把 Codex/OpenCode/Hermes 的数据合并进 DSH

## 场景标签

 · 领域:AI agent 工具链/迁移

## 证据(README 行号)

> L6: **Migrate Claude Code, Codex, OpenCode and Hermes into DeepSeek Harness — copy sessions, memories, skills, instructi
> L61: 6. **Four-source migration wizard** — `/move` plus `move_detect` / `move_preview` / `move_run` migrate Claude Code,

## 星数曲线

```mermaid
xychart-beta
    title "PerryLink/dsh-claude-move 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-28 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c17e916a35f5` · [字段定义](../../DATASET.md)*
