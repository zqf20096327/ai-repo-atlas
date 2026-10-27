# tale-project/tale

⭐ 36 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/tale-project/tale) · [官网](https://tale.dev) · 组织维护

**面向团队与 AI agent 的自托管项目工作区与任务协作平台**

Tale 是一个开源（MIT）的项目工作区：团队在任务板上创建任务并分配给成员或 AI agent，agent 在持久沙箱中运行，产出报告与文件供团队审阅。可为每个 agent 选择运行时（Claude Code、Codex、Cursor、Gemini CLI、Hermes、OpenClaw、OpenCode、Pi、Qwen Code）、模型与工具，并可配置管理型 agent 分派任务。内置模型网关、知识检索、自动化工作流、连接器与治理策略。通过 CLI 脚本配合 Docker/Compose 自托管，或使用托管云服务；Enterprise 版在相同产品功能上增加运营与支持服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任务板分配工作给团队成员或 AI agent，含审阅与交付物管理
- 支持 9 种 agent 运行时（Claude Code、Codex、Cursor、Gemini CLI 等）
- agent 运行于持久沙箱工作区，并发受配置容量限制
- 内置模型网关、自动化工作流、Arena 模型对比与治理策略

## 适用场景

- 团队把任务分配给人和 AI agent 协同完成并审阅结果
- 用管理型 agent 分派就绪任务并协调后续工作
- 在自有基础设施上自托管带治理与审计的 AI 工作区

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L13: Tale gives teammates and AI agents a shared project workspace. Add tasks to the board, assign people or agents, fol
> L15: Choose each agent’s runtime, model, skills, and tools. Equip a manager agent to delegate ready tasks and coordinate
> L58: **Which agent runtimes can I use?** Tale includes Claude Code, Codex, Cursor, Gemini CLI, Hermes, OpenClaw, OpenCod

## 星数曲线

```mermaid
xychart-beta
    title "tale-project/tale 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-27 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b6419e22194d` · [字段定义](../../DATASET.md)*
