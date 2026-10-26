# MuzeAnisichael/agent-skill-factory

⭐ 37 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/MuzeAnisichael/agent-skill-factory) · 个人维护 · 中文 README

**本地工具链：把任务材料生成、校验并发布为可复用 Agent Skill**

面向开发者的 Agent Skill 生命周期 CLI 工具链：从任务简报、文档、代码约定与 Agent 轨迹 ingest 生成可审查的 SkillPlan，再生成 Skill 包并做 lint、eval、有界修复，最终注册、导出与安装。LLM 访问可选：本地 Ollama、OpenAI 兼容 API 或确定性离线流程；运行时仅依赖 PyYAML。当前版本 0.8.0，自述仍处 alpha；未实现图形界面、第一方 Agent 适配器与沙箱，示例含在仓库而非 wheel 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ingest→plan→generate→lint→eval→repair→registry→export 完整本地生命周期
- LLM 可选：本地 Ollama / OpenAI 兼容 API / 确定性离线工作流
- 运行时仅依赖 PyYAML，计划与生成分离以支持审查
- 支持导出到 codex 与 claude-code 目标目录

## 适用场景

- 把团队文档和代码约定整理成可测试的 Agent Skill
- 对生成的 Skill 做 lint、eval 与有界修复再发布
- 用本地 Ollama 模型离线规划与生成 Skill

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: Agent Skill Factory is an open-source local toolchain for generating, validating, evaluating, registering, and expo
> L59: - local Ollama and OpenAI-compatible model providers

## 星数曲线

```mermaid
xychart-beta
    title "MuzeAnisichael/agent-skill-factory 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-23 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d9a0d307ff83` · [字段定义](../../DATASET.md)*
