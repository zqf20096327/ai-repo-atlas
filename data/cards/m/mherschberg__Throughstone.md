# mherschberg/Throughstone

⭐ 15 · Shell · BSD-3-Clause · 推送 2026-10-27 · [GitHub](https://github.com/mherschberg/Throughstone) · [官网](https://throughstone.org) · 个人维护

**架构优先的软件项目脚手架：让 AI 编程助手按纪律流程从想法到成品**

一套供 AI 编程助手（Claude Code、Codex 等）协作使用的项目脚手架与方法论：用户带想法来，kickoff 访谈采集需求，首个 STEP 只产出架构文档与 ADR 决策记录（不写应用代码），工作拆分为 Phases→STEPs→substeps，每个单元可在独立上下文中由 agent 执行。含 init.sh 初始化向导（替换占位符、生成仓库）、多开发者/多 agent 协作约定、按经验级别定制的本地用户档案。面向经验开发者、初级开发者及无编码经验的构建者；作者注明协作层较新、单人项目验证为主。以 git clone 模板仓库方式使用，需 bash、git、perl。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 首个 STEP 只产出架构文档与 ADR，不写应用代码
- 工作拆分为 Phases→STEPs→substeps，供 agent 在独立上下文执行
- init.sh 初始化向导支持非交互式参数与 mono/multi-repo 布局
- kickoff 访谈用自然语言采集想法并生成项目简报

## 适用场景

- 用 AI 编程助手从零开始建一个需要长期维护的软件项目
- 给初级开发者或非技术创始人提供可重复的 AI 编码流程
- 在团队中多人/多 agent 协作时用分支-per-STEP 与 ADR 管理决策

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: A starting structure for building a software project *architecture-first*, with an AI
> L6: coding agent (Claude Code, Codex, etc.) as your collaborator. You bring an idea — roughly a
> L186: 3. **Start your AI agent in the project folder, and send it one command.** Launch your

## 星数曲线

```mermaid
xychart-beta
    title "mherschberg/Throughstone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `52223093dd3f` · [字段定义](../../DATASET.md)*
