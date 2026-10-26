# rezaho/MARSYS

⭐ 25 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/rezaho/MARSYS) · [官网](https://marsys.ai) · 个人维护

**构建与协调多智能体 AI 系统的 Python 框架**

面向开发者的多智能体编排 Python 框架：支持以字符串、对象或预定义模式定义智能体拓扑，提供 AgentPool 并行执行与动态分支、断点续跑的状态持久化、审批与错误恢复的 human-in-the-loop 交互。模型接入覆盖 OpenAI、Anthropic、Google、OpenRouter、xAI 及本地模型，另有 ChatGPT/Claude 订阅的 OAuth 登录方式（其中 anthropic-oauth 为非官方路径，README 提示可能违反服务条款）。含 BrowserAgent 浏览器自动化，需额外安装 Playwright。以 pip 包与源码两种方式安装，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 字符串/对象/预定义模式三种拓扑定义方式
- AgentPool 真并发与动态分支生成
- 检查点式状态持久化，长任务可暂停恢复
- 内置 human-in-the-loop 审批与错误恢复流程

## 适用场景

- 搭建多个专业化 agent 协作完成的工作流
- 需要人工审批节点的自动化任务管道
- 长时运行任务的暂停与恢复场景

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: **A framework for orchestrating collaborative AI agents with sophisticated reasoning, planning, and autonomous capab
> L15: MARSYS (Multi-Agent Reasoning Systems) is a Python framework for building and coordinating multi-agent AI systems. 
> L24: - **Multi-Model Support**: OpenAI, Anthropic, Google, OpenRouter, xAI, and local models

## 星数曲线

```mermaid
xychart-beta
    title "rezaho/MARSYS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-26 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ecb6c6bda1f0` · [字段定义](../../DATASET.md)*
