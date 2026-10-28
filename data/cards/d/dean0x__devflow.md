# dean0x/devflow

⭐ 21 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/dean0x/devflow) · [官网](https://dean0x.github.io/x/devflow/) · 个人维护

**Claude Code 的元工具框架：编入 agent 团队与工程流程**

面向使用 Claude Code 的开发者的 npm 安装型框架：向主会话注入 charter 使其成为 orchestrator，向 20 个专职 agent（Opus/Sonnet/Haiku 分工）分派工作，最多 20 个并行 Review agent 覆盖安全/架构/性能等维度。提供跨重启与 /clear 的工作记忆、架构决策与坑点自动归档（.devflow/curation/）、按 feature 的 KNOWLEDGE.md、13 条常驻规则、42 个技能与 6 个合规框架引用（GDPR/HIPAA 等），支持 GitHub/Jira/Linear 三种 tracker，另有针对整系统交付的 graph workflows（wave 式构建）。通过 npx devflow-kit init 交互式安装，需 Node.js 22+。数据默认本地，仅知识库与约定经 git 共享。

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

- 20 个专职 agent 编队 + 最多 20 个并行 Review agent（带严重度/置信度评分）
- 会话记忆跨重启、/clear 与上下文压缩持久
- 6 个合规框架内置（GDPR/HIPAA/PCI DSS/SOC 2/ISO 27001/SOX）
- 42 个技能可被用户文件 shadow 覆盖

## 适用场景

- 把 Claude Code 单 agent 会话扩展为带分派与评审流程的 agent 团队
- 在仓库内沉淀架构决策、命名约定与 feature 知识库供团队复用
- 按合规框架要求对涉及受监管代码的 diff 自动触发审查
- 用 graph workflows 按依赖波次交付整个系统规格

## 场景标签

`代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: **A meta-harness for Claude Code.** Claude Code gives you one brilliant engineer. Devflow installs the engineering o
> L34: **A staffed agent roster.** 20 specialized agents with explicit model assignments — Opus for analysis, Sonnet for e

## 星数曲线

```mermaid
xychart-beta
    title "dean0x/devflow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `26332593ba49` · [字段定义](../../DATASET.md)*
