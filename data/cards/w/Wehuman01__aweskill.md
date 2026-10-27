# Wehuman01/aweskill

⭐ 36 · TypeScript · MPL-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/Wehuman01/aweskill) · 个人维护 · 中文 README

**给多 AI 编码工具统一管理技能包的本地 CLI**

面向同时使用 Codex、Claude Code、Cursor、Gemini CLI、Qwen Code、Windsurf 等多个 AI agent 的开发者与团队：以 ~/.aweskill/skills/ 作为技能单一来源，通过 symlink/junction/copy 将技能投影到各 agent 的技能目录，支持查找、安装、更新、打包、去重、备份与修复（doctor 工作流默认 dry-run）。内置三个管理技能，可由 agent 通过自然语言调用 CLI 完成日常操作。以 npm 全局安装，需 Node.js 20 或更高版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中央存储 + symlink/junction/copy 投影到各 agent 技能目录
- 跨 skills.sh、sciskillhub.org、GitHub 源与本地路径的搜索安装更新循环
- doctor 修复工作流：断裂投影、重复条目、畸形 frontmatter（默认 dry-run）
- 内置 aweskill/aweskill-doctor/aweskill-creator 三个 agent 可调用管理技能

## 适用场景

- 我在多个 AI 编码工具间同步同一套技能，不想逐个复制 SKILL.md
- 把项目或团队常用技能打包成 bundle 一次性启用/移除
- 让 agent 用自然语言帮我创建、安装和修复技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A CLI-first skill package manager that AI agents can operate themselves.
> L33: Instead of copying the same `SKILL.md` folders into every tool by hand, `aweskill` keeps one central source of trut
> L269: - **Agent-callable management, repair, and authoring skills** so AI agents can run `aweskill`, `aweskill-doctor`, 

## 星数曲线

```mermaid
xychart-beta
    title "Wehuman01/aweskill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `df20727f3b95` · [字段定义](../../DATASET.md)*
