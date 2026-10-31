# SomeOddCodeGuy/WilmerAI

⭐ 830 · Python · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/SomeOddCodeGuy/WilmerAI) · 个人维护

**LLM 语义路由与工作流编排网关，接在应用与多个 LLM API 之间**

WilmerAI 是位于客户端应用与多个 LLM API 之间的语义路由与编排服务：基于节点式工作流引擎，路由决策可读取完整对话历史，按意图选择专用工作流；节点可调用不同 LLM 端点、外部工具、自定义脚本或其他工作流。对外暴露 OpenAI 与 Ollama 兼容 API 端点，后端连接 OpenAI、Ollama、KoboldCpp 等。含四部分对话记忆系统、工具调用透传、结构化输出、实验性 MCP 集成，开发以隐私优先为原则。README 声明项目仍在开发中、按原样提供。需 Python 3.11+（web fetcher 需更高版本）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 节点式工作流引擎，路由基于完整对话历史
- 对外暴露 OpenAI/Ollama 兼容 API 端点
- 多 LLM、多工具编排：每个节点可连接不同端点或执行工具
- 四部分状态化对话记忆（摘要、滚动摘要、向量库、状态文档）

## 适用场景

- 让现有前端工具不改代码接入多模型路由后端
- 把重复的迭代式 LLM 调用流程固化为可复用工作流
- 利用多台旧机器运行小模型组成分布式 LLM 工作流

## 场景标签

`模型网关` `工作流自动化` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L24: WilmerAI is an application designed for advanced semantic prompt routing and complex task orchestration. It
> L38: To the client application, this entire multi-step process appears as a standard API call, enabling advanced backend
> L121:  WilmerAI's "front door." It exposes OpenAI- and Ollama-compatible API endpoints, allowing you to connect your exi

## 星数曲线

```mermaid
xychart-beta
    title "SomeOddCodeGuy/WilmerAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 829 --> 831
    line [830, 830]
```

2026-10-18 830 → 2026-10-31 830（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `06936bbf435e` · [字段定义](../../DATASET.md)*
