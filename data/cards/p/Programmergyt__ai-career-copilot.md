# Programmergyt/ai-career-copilot

⭐ 27 · Python · 推送 2026-05-03 · [GitHub](https://github.com/Programmergyt/ai-career-copilot) · [官网](http://8.153.79.69:3001) · 个人维护 · 中文 README

**面向求职者的多 Agent 求职辅助系统：JD 分析、简历生成、模拟面试**

基于 FastAPI + LangGraph + Vue 3 的 Web 应用，面向求职者：给定目标岗位 JD 与个人材料，由多个 Agent（规划、JD 分析、档案抽取、差距分析、内容生成、渲染、面试准备）协作完成简历结构化生成、HTML 渲染预览、能力差距分析与面试问答生成，支持多轮对话式修改。LLM 默认使用 DeepSeek，嵌入与重排使用 DashScope；Redis 存会话状态、MySQL 持久化。提供在线 Demo；本地部署需 Python 3.11+/Node 18+/MySQL 8+/Redis 6+ 及模型 API key，Docker Compose 需自备 MySQL/Redis 实例，仓库当前未包含 LICENSE 文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 多 Agent 编排：JD 分析、档案抽取、差距分析、内容生成、渲染、面试准备
- 结构化简历生成与 HTML 预览/导出，聊天式渲染指令
- 基于目标岗位与简历上下文的面试问答生成
- Redis 会话状态 + MySQL 持久化，Debug 面板展示中间产物

## 适用场景

- 上传目标 JD 后自动定制简历并多轮修改
- 对比 JD 与自身材料查看能力差距
- 针对目标岗位生成面试题做准备

## 场景标签

`多智能体` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L12: An AI-powered multi-agent web app for job description analysis, candidate profile extraction, resume generation, HT
> L19: - Agent-based orchestration with LangGraph for planner, JD analysis, profile extraction, gap analysis, content gene
> L84: |LLM integration|LangChain, DeepSeek|

## 星数曲线

```mermaid
xychart-beta
    title "Programmergyt/ai-career-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `58aab374f705` · [字段定义](../../DATASET.md)*
