# KimYx0207/claude-memory-3layer

⭐ 33 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/KimYx0207/claude-memory-3layer) · 个人维护 · 中文 README

**给 Claude Code 用户补齐跨会话记忆的管理层工具**

面向 Claude Code 用户的记忆管理钩子套件：三层结构（JSON 知识图谱 + Markdown 日记 + 默会知识），通过 SessionStart/PostToolUse/PreCompact 钩子自动抽取与加载事实；每条事实带 active/superseded 生命周期状态，记忆存于项目内 .claude/memory/ 可经 git 共享，单主题加载约 1500 token 可配置。定位为官方 auto-memory 的补充而非替代。纯 Python stdlib 零依赖，一行脚本安装。注意：仓库已并入 Kim Service，不再独立发布版本。

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

- 三层记忆：JSON 知识图谱 + 日记 MD + 默会知识 MD
- 事实级 active/superseded 生命周期与 /memory-review 清理命令
- 记忆存于 .claude/memory/，git 可追踪、团队可共享
- 纯 Python stdlib 零依赖，单主题约 1500 token 预算可配置

## 适用场景

- 让 Claude Code 在多会话间保留项目知识与决策
- 团队通过 git 共享和维护项目知识库
- 控制记忆加载的 token 开销并清理过期条目

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L76: - :electric_plug: **Hook-Powered** — SessionStart / PostToolUse / PreCompact lifecycle hooks
> L184:     "SessionStart": [

## 星数曲线

```mermaid
xychart-beta
    title "KimYx0207/claude-memory-3layer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3c571ed4f3ae` · [字段定义](../../DATASET.md)*
