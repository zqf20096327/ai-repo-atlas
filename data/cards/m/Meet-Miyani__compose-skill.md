# Meet-Miyani/compose-skill

⭐ 306 · Shell · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Meet-Miyani/compose-skill) · [官网](https://compose.avinya.dev) · 个人维护

**给 AI 编码 agent 的 Jetpack Compose 代码风格技能包（7 个技能）**

面向 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等 AI 编码 agent 的技能包：提供 7 个技能，为 Jetpack Compose 与 Compose Multiplatform 开发规定统一的代码风格——MVI、Koin、Navigation 3、Ktor、Room 等。核心机制是约 1.3k token 的入口决策树，按任务类型与影响区域按需加载参考文件（全套约 127k token）；另含 11 个 shell 守护脚本用于 CI 漂移检查。通过 npx skills、gh skill 及 Claude Code/Codex 插件市场四种渠道安装。README 报告了 90+36 次 agentic 运行的盲评测试结果，并披露了测试局限（每单元单次生成、6 个任务）。

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

- 7 个技能覆盖架构、特性、UI、数据、项目、平台六个领域
- 约 1.3k token 入口决策树按需加载参考文件
- 11 个 shell 守护脚本加 90 个 fixture 测试用于 CI 漂移检查
- 四种安装渠道：npx skills / gh skill / Claude Code 插件 / Codex 插件

## 适用场景

- 让我的 AI 编码 agent 按 MVI + Koin + Navigation 3 风格写 Compose 代码
- 团队在仓库内共享统一的 Compose 代码规范给 agent 使用
- 在 CI 中用守护脚本检查 agent 生成代码的风格漂移

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A Compose skill for AI coding agents: seven agent skills that make Claude Code, Codex, Cursor, Copilot and Gemini
> L16: **Works with** Claude Code · Codex · Cursor · OpenCode · Copilot · Gemini CLI · Antigravity
> L84: Install all seven skills. `compose` is the entry point, and it hands each task to the other six. Step-by-step pages

## 星数曲线

```mermaid
xychart-beta
    title "Meet-Miyani/compose-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 303 --> 307
    line [304, 306, 306]
```

2026-10-18 304 → 2026-10-30 306（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ad711ae243d7` · [字段定义](../../DATASET.md)*
