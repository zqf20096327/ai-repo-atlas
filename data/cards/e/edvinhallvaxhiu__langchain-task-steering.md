# edvinhallvaxhiu/langchain-task-steering

⭐ 21 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/edvinhallvaxhiu/langchain-task-steering) · [官网](https://pypi.org/project/langchain-task-steering/) · 个人维护

**LangChain agent 的隐式状态机任务管道中间件**

面向 LangChain v1 agent 的 AgentMiddleware：将有序任务管道（PENDING→IN_PROGRESS→COMPLETE）隐式建模为状态机，模型通过调用 update_task_status 工具自行推进转换；中间件强制任务顺序、按任务限定可用工具、将当前任务指令注入系统提示词，并通过可插拔校验器把关完成判定。另提供 WorkflowSteeringMiddleware 支持 agent 自主激活混合自由对话与结构化工作流。以 Python（pip）与 TypeScript（npm）双语言包形式提供；不支持分支、并行与循环编排（README 指引此类需求用显式 LangGraph）。

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

- 有序任务管道的状态机中间件，模型经 update_task_status 自驱转换
- 按任务限定工具范围与动态提示词注入
- 可插拔的完成校验器与 TaskMiddleware 组合机制
- Python 与 TypeScript 双语言包

## 适用场景

- 让 agent 按顺序执行多个各有专属工具的任务
- 混合自由对话与结构化工作流的场景，由 agent 自主激活流程
- 从配置或数据库动态生成任务管道

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Implicit state-machine middleware for LangChain agents. Define ordered task pipelines with per-task tool scoping, dy
> L11: The model drives its own transitions by calling `update_task_status`. The middleware enforces ordering, scopes tool

## 星数曲线

```mermaid
xychart-beta
    title "edvinhallvaxhiu/langchain-task-steering 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1eddb9892cba` · [字段定义](../../DATASET.md)*
