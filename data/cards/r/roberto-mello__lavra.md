# roberto-mello/lavra

⭐ 52 · Shell · MIT · 推送 2026-10-22 · [GitHub](https://github.com/roberto-mello/lavra) · [官网](https://lavra.dev) · 个人维护

**AI 编码 agent 插件：全流程开发工作流与自动记忆**

面向 AI 编码 agent 的插件，编排从头脑风暴到发布的开发全流程：/lavra-design 规划、/lavra-work 实现、/lavra-ship 发布，另有 QA 与回顾等共 19 个命令和 30 个专用 agent。核心机制是六类知识在工作过程中强制捕获并存储于 .lavra/memory/knowledge.jsonl（git 跟踪），会话开始时按当前 beads 与 git 分支自动召回。支持 Claude Code、OpenCode、Gemini CLI、Cortex Code。运行需 beads CLI、jq、sqlite3。面向非技术用户、独立开发者与团队。

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

- 13 条流水线/支撑命令覆盖设计-实现-发布全流程
- 六类知识（LEARNED/DECISION/FACT 等）强制内联捕获，会话开始自动召回
- 知识库以 knowledge.jsonl 存储、git 跟踪，团队共享复利
- 支持 Claude Code / OpenCode / Gemini CLI / Cortex Code 四种 agent

## 适用场景

- 让编码 agent 记住过往决策与坑，避免每次重讲上下文
- 一条命令完成从需求头脑风暴到创建 PR、跑测试的完整流程
- 团队沉淀开发知识，成员共享彼此的踩坑经验

## 场景标签

`编码 Agent` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: A plugin for coding agents that orchestrates the full development lifecycle -- from brainstorming to shipping -- whi
> L30: - **Automatic memory.** Knowledge is captured inline during work and recalled automatically at the start of every s
> L97: **30 specialized agents** across review, research, design, workflow, and docs. Each runs at the right model tier to

## 星数曲线

```mermaid
xychart-beta
    title "roberto-mello/lavra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-24 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `95b91221fedd` · [字段定义](../../DATASET.md)*
