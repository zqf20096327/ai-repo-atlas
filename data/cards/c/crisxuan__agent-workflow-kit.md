# crisxuan/agent-workflow-kit

⭐ 31 · NOASSERTION · 推送 2026-05-23 · [GitHub](https://github.com/crisxuan/agent-workflow-kit) · 个人维护 · 中文 README

**为 AI 辅助开发项目提供评估优先的工作流规则与 AGENTS.md 模板**

面向维护者的工具中立指南与 agent 工作流包：通过仓库检查与 0-16 分风险评分表判断项目是否需要 AI 工作流及强度，按 Level 0-3 四级选择最小安全工作流，并生成可复制的 AGENTS.md 规则块（安装/测试/lint/构建/验收命令与外部操作审批规则）。skills/ 目录提供 Codex 兼容格式的英文与中文 Skill 包，内容为纯 Markdown 与 YAML，Claude、Cursor、Gemini 等 harness 均可读取适配。指南与 Skill 指令采用 CC BY 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 0-16 分仓库风险评分与 Level 0-3 四级工作流选择
- 提供可复制的英文/中文 AGENTS.md 模板块
- Codex 兼容 Skill 包（SKILL.md + openai.yaml + 参考模板），纯 Markdown/YAML 可被其他 agent 读取
- 英文/中文双语指南与模板

## 适用场景

- 评估我的仓库是否需要 AI 开发规则以及规则该多重
- 为团队的 coding agent 建立一致的验收与外部操作审批规则
- 快速获得一份标准工作流级别的 AGENTS.md 起步模板

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: Agent Workflow Kit is a tool-neutral guide and agent workflow package for deciding whether a repository needs AI-as
> L88: The `skills/` directory contains agent-facing versions of the guide. They are packaged as Codex-compatible Skills, 

## 星数曲线

```mermaid
xychart-beta
    title "crisxuan/agent-workflow-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ba4092aecbce` · [字段定义](../../DATASET.md)*
