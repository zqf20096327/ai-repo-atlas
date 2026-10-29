# opencmit/alphora

⭐ 348 · Python · Apache-2.0 · 推送 2026-07-07 · [GitHub](https://github.com/opencmit/alphora) · [官网](https://bigdata.10086.cn/) · 组织维护 · 中文 README

**构建可组合 AI Agent 的全栈 Python 框架**

面向生产环境的 AI agent 开发框架：提供 ReAct 与 Plan-Execute 推理循环、@tool 装饰器自动生成函数调用 schema、多会话记忆管线、本地/Docker/远程 Docker 代码沙箱、兼容 agentskills.io 的技能生态、MCP 集成、类型化 SSE 流式输出，以及一行式 publish_agent_api 将 agent 发布为 OpenAI 兼容 REST API，并附带 AgentChat Web 前端。模型层对接任意 OpenAI 兼容 API（含 GPT、Claude、Qwen、DeepSeek、本地模型），支持多模态输入与多后端负载均衡。以 pip 包分发，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct/Plan-Execute 循环与 Agent 派生（derive 继承 LLM、记忆、配置）
- 本地/Docker/远程 Docker 代码沙箱与安全策略
- 一行 publish_agent_api 发布 OpenAI 兼容 REST API + 内置 Web UI
- 兼容 agentskills.io 技能生态与 MCP 集成

## 适用场景

- 构建带工具调用与记忆的生产级 AI agent 应用
- 将 agent 以 OpenAI 兼容 API 形式部署并接入前端
- 在隔离沙箱中运行 agent 生成的代码做数据分析

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L20: Alphora is a full-stack framework for building production AI agents. It provides everything you need — agent orches
> L54: - **Multi-Model Support** — Works with any OpenAI-compatible API (GPT, Claude, Qwen, DeepSeek, local models). Multi

## 星数曲线

```mermaid
xychart-beta
    title "opencmit/alphora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 347 --> 349
    line [348, 348]
```

2026-10-18 348 → 2026-10-29 348（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `e59999e555d0` · [字段定义](../../DATASET.md)*
