# nextflow-io/agent-skills

⭐ 25 · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/nextflow-io/agent-skills) · [官网](https://nextflow.io) · 组织维护

**面向编码 agent 的 Nextflow 流程构建技能包**

Nextflow 官方组织提供的 Agent Skills 集合，包含 5 个技能：安装/升级 Nextflow、从 Nextflow Registry 组合模块创建流程、用 nextflow module 原生运行模块、在 Seqera Platform 启动流程、迁移流程代码到新语言特性。技能遵循 Agent Skills 规范，可被 Claude Code、Codex CLI、OpenCode、Cursor 等兼容 agent 使用。通过 Claude Code 插件市场或 GitHub CLI（v2.90.0+）安装；要求 Nextflow 26.04+（工作流模块需 26.10+），部分技能需配置 Seqera MCP 服务器。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个技能覆盖 Nextflow 安装、创建、运行、启动与代码迁移
- 遵循 Agent Skills 规范，兼容多种编码 agent
- 可从 Nextflow Registry 各命名空间（含 nf-core）组合模块
- 通过 Claude Code 插件市场或 gh skill 安装

## 适用场景

- 让编码 agent 帮我搭建和运行 Nextflow 生信流程
- 在 Claude Code / Cursor 中直接调用 Registry 模块
- 把旧流程代码迁移到新语言特性

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agent skills for building and running Nextflow pipelines with modules from the Nextflow Registry.
> L7: These skills follow the Agent Skills specification, so they can be used by any skills-compatible agent, including Cl

## 星数曲线

```mermaid
xychart-beta
    title "nextflow-io/agent-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a9b2ff10c6d4` · [字段定义](../../DATASET.md)*
