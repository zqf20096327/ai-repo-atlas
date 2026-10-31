# cogfoundry-labs/loomloom

⭐ 16 · Go · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/cogfoundry-labs/loomloom) · 组织维护

**将 AI 工作流编译打包为可复用软件的编译器与运行时**

面向开发者的 AI work 编译器与执行运行时：把提示词、技能与多步 agent 工作流定义为 AI work，经 SkillCompiler 分析优化为中间表示（AI work IR），再编译为执行 DAG 并打包为可部署的 SkillApp，通过 CLI 或兼容执行平台运行，支持依赖感知的并行执行、模型路由、缓存与失败恢复等运行时能力。提供开源 CLI 与编译器参考实现，执行平台可向 CogFoundry 获取商业许可。项目自述处于 beta，设计细节可能随反馈调整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI work 编译为中间表示（IR）与执行 DAG
- SkillApp 打包编译后的 AI 系统，可经 API/MCP/CLI 调用
- 依赖感知的并行执行、模型与工具路由、缓存与重试等运行时能力
- CLI 可与 Claude Code、Codex、Cline 等 agent 及 MCP 兼容环境协作

## 适用场景

- 把提示词、技能与工作流版本化为可分发的软件制品
- 构建需要依赖感知并行执行的多步 agent 工作流
- 将编译后的 AI 系统部署到兼容执行平台并通过 API/MCP 调用

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L72: loomloom provides a compiler and runtime layer for this new software primitive:
> L74: - Compile and package `AI work` into executable AI systems
> L75: - Execute AI systems across compatible runtimes

## 星数曲线

```mermaid
xychart-beta
    title "cogfoundry-labs/loomloom 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `55cfed258341` · [字段定义](../../DATASET.md)*
