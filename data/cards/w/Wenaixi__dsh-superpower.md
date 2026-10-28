# Wenaixi/dsh-superpower

⭐ 26 · JavaScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Wenaixi/dsh-superpower) · [官网](https://www.npmjs.com/package/@wenaixi/dsh-superpower) · 个人维护 · 中文 README

**DSH 插件：为 agent 运行时注入 15 个工程纪律技能，双语切换可开关**

obra/superpowers 的 DeepSeek Harness 移植插件，将 15 个工程方法论技能（头脑风暴、写计划、TDD、系统化调试、验证后完成、代码评审等）注入 ctx.skills。技能正文保留上游英文原文，每个 SKILL.md 声明英文与中文双语 description，插件面板提供每技能独立开关与三态语言切换（中文/English/跟随宿主），状态存于 profile 的 cordis.patch.yml。以 dsh.bundle 形式发布，通过 dsh plugin 命令或 npm 安装，需 dsh 运行时（>=0.2.0-rc.2）、Node 与 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个 obra/superpowers 工程方法论技能注入 ctx.skills
- 技能描述中英双语三态切换，技能名保持上游英文
- 每技能独立开关，关闭后模型目录与 skill 工具调用均不可见
- 以 dsh.bundle 发布，不写主目录、可干净卸载、HMR 重建

## 适用场景

- 为 DeepSeek Harness agent 补充设计先行、测试驱动的工程纪律流程
- 中文环境下让模型以中文感知技能描述
- 按需启停部分工程技能以控制 agent 行为

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: A DSH port of obra/superpowers. 15 skills are injected into `ctx.skills`. Skill bodies are the official English ori
> L17: Needs the dsh runtime (adapted to latest `v0.2.1-rc.2` / `>=0.2.0-rc.2` via `npm i -g @deepseek-ai/dsh`); Node and 

## 星数曲线

```mermaid
xychart-beta
    title "Wenaixi/dsh-superpower 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-28 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `641e64c0ebf4` · [字段定义](../../DATASET.md)*
