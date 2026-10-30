# kayba-ai/agentic-context-engine

⭐ 2,607 · Python · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/kayba-ai/agentic-context-engine) · [官网](https://www.kayba.ai) · 组织维护

**让 AI agent 从经验中学习的持久学习循环引擎**

ACE 是 Kayba 托管服务背后的开源引擎，为 AI agent 增加“执行—反思—更新”的持久学习循环：Reflector 分析执行轨迹提取经验教训，SkillManager 维护策略集合 Skillbook，下次任务时注入 agent。Recursive Reflector 在沙箱中编写并执行 Python 代码来搜索模式与定位错误。基于 PydanticAI 与 LiteLLM 路由到 100+ LLM 提供商，提供 LiteLLM、Core、Trace Analyser、browser-use、LangChain、Claude Code 等多种 Runner，另有 CLI 与 MCP server。无需微调、训练数据或向量数据库。

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

- Skillbook 持久策略集合 + Agent/Reflector/SkillManager 三角色学习循环
- Recursive Reflector 在沙箱中编写执行 Python 代码做程序化反思
- 经 LiteLLM 集成路由 100+ LLM 提供商
- 可从既有 agent 轨迹直接提取策略，无需重跑任务

## 适用场景

- 让生产环境 agent 不再重复同样的失败
- 浏览器自动化等任务随运行次数累积经验降低成本
- 从历史 agent 日志中挖掘可复用策略

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: **AI agents don't learn from experience.** They repeat the same mistakes every session, forget what worked, and ign
> L78: All roles are backed by PydanticAI agents with structured output validation. PydanticAI routes to 100+ LLM provider

## 星数曲线

```mermaid
xychart-beta
    title "kayba-ai/agentic-context-engine 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29", "2026-10-30"]
    y-axis "stars" 2599 --> 2608
    line [2600, 2604, 2605, 2607]
```

2026-10-18 2,600 → 2026-10-30 2,607（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b8be19a6507a` · [字段定义](../../DATASET.md)*
