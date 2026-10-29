# existential-birds/beagle

⭐ 85 · Shell · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/existential-birds/beagle) · [官网](https://existentialbirds.com) · 组织维护

**面向编码 agent 的技能市场：代码审查/文档/测试/架构技能集**

Agent Skills 市场，为支持 Agent Skills 的编码 agent（Claude Code、Codex 等）提供框架感知技能：代码审查、文档质量与 AI 写作检测、测试计划生成与执行、架构分析（ADR/头脑风暴/LLM-as-judge）及 git 工作流（commit-push、create-pr、发布说明）。技能覆盖 Python、Go、Rust、Elixir、React/Remix、iOS/Swift 等，按 10 个插件组织。通过 npx skills CLI 或 Claude Code 插件市场安装；可选依赖 agent-browser 用于 run-test-plan 技能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个插件覆盖 Python/Go/Rust/Elixir/React/iOS 等技术栈
- 技能含代码审查、测试计划生成、ADR、LLM-as-judge
- git 工作流技能：create-pr、gen-release-notes、PR 反馈处理
- AI 写作检测与文档改进技能（Diataxis）

## 适用场景

- 给 Claude Code / Codex 等 agent 增加代码审查与测试技能
- 让 agent 执行 git 提交、PR 创建与反馈响应工作流
- 生成 ADR 与测试计划等工程文档

## 场景标签

`代码审查` `编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: Beagle is an Agent Skills marketplace: framework-aware code review, documentation, testing, architectural analysis, 
> L11: Install for any agent: `npx skills add existential-birds/beagle`. Then your agent loads the right skill automatical
> L18: - A coding agent that supports Agent Skills

## 星数曲线

```mermaid
xychart-beta
    title "existential-birds/beagle 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-29 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `84e3d553841d` · [字段定义](../../DATASET.md)*
