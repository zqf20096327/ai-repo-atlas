# MiiFlow/miiflow-agent

⭐ 19 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/MiiFlow/miiflow-agent) · [官网](https://www.miiflow.ai) · 组织维护

**模型无关的 Python agent 框架：统一 API 接 9 家 LLM**

以 Python 库形式提供的模型无关 agent harness，定位与 Claude Agent SDK 同类但不绑定单一模型家族：统一 API 支持 OpenAI、Anthropic、Gemini、Bedrock、OpenRouter、Groq、Mistral、Ollama、xAI 九家提供商，一行切换。单一 ReAct 循环内实现计划与多 agent 分发，提供并行工具执行、子 agent 深度/预算限制、人机审批与多选题澄清、JSON 可序列化 Checkpoint 暂停恢复、上下文压缩引擎、MCP 客户端与服务端原生接入、类型化事件流与 OpenInference 追踪。不内置文件系统/shell/web 工具，能力由用户提供的工具决定。需 Python 3.10–3.12。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 覆盖 9 家 LLM 提供商，一行切换模型
- 单一 ReAct 循环内置子 agent 分发（深度/环/预算限制）
- Checkpoint 暂停恢复与工具审批、澄清、计划模式的人机协同机制
- 上下文引擎自动压缩长对话，超阈值时工具 schema 收进 tool_search 元工具

## 适用场景

- 构建可切换多家 LLM 提供商的产品 agent
- 需要人机协同（工具审批、计划确认）的 agent 流程
- 为多用户服务的产品 agent 做可观测性与审计

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: **miiflow-agent is that harness, as a Python library.** It plays the same role as the Claude Agent SDK, but it is n
> L39: |**Models**|**Claude**|**OpenAI, Anthropic, Gemini, Bedrock, OpenRouter, Groq, Mistral, Ollama, xAI**|

## 星数曲线

```mermaid
xychart-beta
    title "MiiFlow/miiflow-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `57fca99473c0` · [字段定义](../../DATASET.md)*
