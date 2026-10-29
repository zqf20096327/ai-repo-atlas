# 01-ai/langcrew

⭐ 117 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/01-ai/langcrew) · [官网](https://langcrew.ai) · 组织维护 · 中文 README

**基于 LangGraph 的高级多智能体开发框架，面向产品化交付**

01-ai（Open AgentKit）开源的多智能体开发框架（OAK Framework），在 LangGraph 之上提供高层抽象：多智能体编排、HITL 人工审批系统、多层记忆（LangGraph 原生 + langmem）、统一工具注册表与安全护栏、LangSmith/LangTrace 可观测性集成。附带 Agent-UI 协议与 React 组件库做全栈可视化，内置工具库（浏览器自动化、沙箱代码解释器等）与招聘、营销、旅行等行业模板。本地开发采用 git clone + pnpm，亦提供 Docker Compose 一键启动，需 OpenAI/Anthropic/DashScope API key。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 LangGraph 之上提供 crew/agent/task 高层抽象与预置编排实现
- HITL 审批系统、多层记忆、统一工具注册表与 LangSmith/LangTrace 集成
- Agent-UI 协议与 React 组件库实现执行过程可视化
- 含浏览器自动化、云手机控制、沙箱代码解释器等工具与行业模板

## 适用场景

- 快速搭建需要人工审批环节的多智能体业务系统
- 可视化调试与交付多智能体应用的前后端全栈方案
- 基于行业模板（招聘筛选、营销策划、旅行规划）快速原型化

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: LangCrew is a high-level multi-agent development framework built on LangGraph, combining CrewAI's intuitive concepts
> L47: The heart of LangCrew - a high-level abstraction over LangGraph that provides multi-agent orchestration, memory man

## 星数曲线

```mermaid
xychart-beta
    title "01-ai/langcrew 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-29 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f4296444d2c5` · [字段定义](../../DATASET.md)*
