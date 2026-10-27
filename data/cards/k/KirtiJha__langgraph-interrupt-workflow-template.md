# KirtiJha/langgraph-interrupt-workflow-template

⭐ 32 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/KirtiJha/langgraph-interrupt-workflow-template) · [官网](https://langgraph-interrupt-workflow-templa.vercel.app) · 个人维护

**GitHub 维护者代理：代理分诊 issue/PR，公开操作前请求人工批准**

面向 GitHub 维护者的 human-in-the-loop 代理应用：对指定仓库做 issue 分诊、PR 审查、陈旧线程清理、发布说明起草与新贡献者欢迎，每个公开操作附带风险评分与预览，经批准/编辑/拒绝后才执行。技术栈为 LangGraph v1 + LangChain v1、FastAPI 后端与 Next.js 前端；内置 per-call 中断、时间旅行、Postgres 持久线程、四档自治级别与评估。无模型 key 时可用规则式离线 pilot 运行；接入真实模型支持 Vercel AI Gateway、Anthropic/OpenAI/Google、OpenRouter 等任意 provider。同时作为 human-in-the-loop LangGraph 应用的生产级参考模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个公开操作前中断并附风险评分与预览，支持批准/编辑/拒绝/回复四类决策
- 四档自治级别（Observe/Careful/Balanced/Autopilot）与时间旅行分支
- 无模型 key 时以规则式离线 pilot 运行五个起始任务
- 凭据经请求头传入且不落盘；可选 guardrails、MCP 工具、限流等生产层

## 适用场景

- 维护者让代理批量分诊 issue 并逐条审批后再公开操作
- 作为 LangGraph human-in-the-loop 应用的参考实现学习中断与时间旅行
- 在公开仓库上无配置试用后端到端 HITL 流程

## 场景标签

`Agent 框架` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L13: Repo Steward is an agent for GitHub maintainers. Point it at a repository and
> L20: It is also a complete, production-shaped reference for **human-in-the-loop
> L21: agents on LangGraph v1 + LangChain v1**: per-call interrupts, a risk policy that

## 星数曲线

```mermaid
xychart-beta
    title "KirtiJha/langgraph-interrupt-workflow-template 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-27 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d9926280c70b` · [字段定义](../../DATASET.md)*
