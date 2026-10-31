# meraki-digital/repo-template

⭐ 14 · Shell · MIT · 推送 2025-11-06 · [GitHub](https://github.com/meraki-digital/repo-template) · 组织维护

**面向 AI agent 的项目开发模板：SRS→PRD→任务的分步文档工作流**

用于新项目起步的仓库模板，核心是与 AI 编码 agent（如 Amp）配合的分步工作流：通过 "Do Step 1-6" 指令驱动 agent 进行发现式访谈生成 SRS、产出 PRD、拆解任务清单、生成 Tech Stack 文档、执行任务并输出面向客户的 Status Recap。产出文件保存在 tasks/mods/[n]/ 目录，由 AGENTS.md 提供命令与规范约束。另提供可选的 Obsidian 文档同步 git hook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 步指令式工作流（SRS→PRD→任务→技术栈→实施→汇报）
- 设计为与 AI 编码 agent（如 Amp）直接协作
- AGENTS.md 集中定义命令与仓库规范
- 可选 Obsidian vault 文档同步（pre-push hook）

## 适用场景

- 新项目用 AI agent 引导完成需求与任务文档
- 保持 AI 辅助开发过程的一致文档轨迹
- 把项目文档自动同步到 Obsidian 笔记库

## 场景标签

 · 领域:软件开发流程/模板

## 证据(README 行号)

> L24: - **Step-by-Step Development Process**: Follow numbered steps (1-4) to generate requirements, PRDs, tasks, and expl
> L25: - **Agent-Driven Workflow**: Integrates with AI agents for consistent command execution, style guidelines, and repo

## 星数曲线

```mermaid
xychart-beta
    title "meraki-digital/repo-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `4b61d91665a0` · [字段定义](../../DATASET.md)*
