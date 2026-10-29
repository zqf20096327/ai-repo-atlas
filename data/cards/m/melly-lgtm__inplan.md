# melly-lgtm/inplan

⭐ 24 · TypeScript · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/melly-lgtm/inplan) · [官网](https://inplan.ai) · 个人维护

**人机共同编写计划文档的 Markdown 编辑器（CLI+桌面端），面向编码 Agent**

面向 AI 辅助开发的规划工作区：用户与编码 Agent 在同一份 Markdown 计划文档上协作——Agent 起草需求并提出行内提问，用户在编辑器中就地回答或选择选项，Agent 修订后以 diff 形式供用户像审 PR 一样应用，形成版本化的需求与决策记录。安装 CLI 时自动检测并向 Claude Code、Codex、Pi 等 Agent 注入技能，Agent 通过 inplan open/wait/signal 驱动流程。计划为纯 Markdown 加尾部 HTML 注释存储评论，可在任意 Markdown 查看器渲染并在 Git 中 diff。主要在 macOS、turn 模式、Claude Code 下开发测试，其他 OS/模式/Agent 已接线但测试较少。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 人与 Agent 共享一份 Markdown 计划文档，行内评论问答、diff 审阅应用
- npm 安装时自动检测并注入 Agent 技能（Claude Code/Codex/Pi）
- 计划为纯 Markdown + 尾部 HTML 注释，任何查看器可渲染、Git 可 diff
- CLI 提供 open/wait/signal 命令驱动 Agent 与编辑器的交互循环

## 适用场景

- 在编码 Agent 动手写代码前与其共同打磨需求规格
- 把需求、决策与理由沉淀为版本化文档，减少实现漂移
- 以类似代码评审的流程审阅并应用 Agent 的计划修改

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: A Markdown workspace where you and your AI coding agent turn a vague ask into a real
> L159: inplan plugs into your coding agent through a bundled **skill** plus relay hooks: on
> L161: (`inplan install-skill` does this manually). The agent then drives the loop through the

## 星数曲线

```mermaid
xychart-beta
    title "melly-lgtm/inplan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `50a8ee715bb6` · [字段定义](../../DATASET.md)*
