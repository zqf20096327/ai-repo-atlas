# hexagon-codes/hexagon

⭐ 14 · Go · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/hexagon-codes/hexagon) · [官网](https://hexclaw.net) · 组织维护 · 中文 README

**面向 Go 开发者的 AI Agent 框架：编排、RAG、多 Agent 与持久化执行**

以 Go 库形式提供的 AI Agent 构建框架，包含 Graph/Chain/Workflow/Planner 任务编排、ReAct/PlanExecute/Reflection 运行时、RAG 引擎与智能文档工作流、多 Agent 团队与 AgentTool 组合、per-tool exactly-once 快照与中断恢复。通过配套 ai-core 库接入 OpenAI/DeepSeek/Anthropic/Gemini/通义/豆包/Ollama 等 Provider，支持 MCP、Google A2A 协议、OpenTelemetry 追踪与 Dev UI 调试界面。为库形态，无可直接运行入口，deploy/ 仅提供开发基础设施与 K8s 接入模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Graph/Chain/Workflow/Planner 任务编排与统一 Durable Runtime（快照与 Resume）
- RAG 引擎、ADW 智能文档工作流与结构化提取/验证
- 实现 Google A2A 协议与 MCP（含自动重连、分页工具发现）
- 7 种 LLM Provider 接入与智能模型路由、OpenTelemetry 可观测性

## 适用场景

- 用 Go 构建带工具调用的 ReAct Agent 与多 Agent 协作系统
- 搭建带持久化执行与中断恢复的长任务工作流
- 构建 RAG 或 schema 驱动的文档数据提取流程

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L15: 项目围绕 **易用性、并发执行、扩展性、任务编排、可观测性、安全性** 六个维度，为 Go 开发者提供构建 AI Agent 的框架组件。
> L51: - `llm/` - LLM Provider 接口 + 实现 (OpenAI, DeepSeek, Anthropic, Gemini, 通义, 豆包, Ollama)

## 星数曲线

```mermaid
xychart-beta
    title "hexagon-codes/hexagon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2b014f5fda01` · [字段定义](../../DATASET.md)*
