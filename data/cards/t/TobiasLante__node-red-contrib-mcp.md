# TobiasLante/node-red-contrib-mcp

⭐ 14 · JavaScript · Apache-2.0 · 推送 2026-02-23 · [GitHub](https://github.com/TobiasLante/node-red-contrib-mcp) · 个人维护

**Node-RED 的 MCP 节点包：可视化搭建连接 MCP 工具的 AI Agent**

npm 安装的 Node-RED 扩展节点包，提供 mcp server/mcp tool/mcp resource/llm call/ai agent 等节点，通过 Streamable HTTP 或 SSE 传输连接任意 MCP 服务器，LLM 侧支持任意 OpenAI 兼容 API（OpenAI、Ollama、vLLM、Azure 等）。ai agent 节点运行工具发现→LLM 推理→工具执行的完整循环，输出答案与调用日志。面向制造、IIoT、楼宇自动化等场景的自动化开发者，要求 Node-RED ≥3.0.0 与 Node.js ≥18，Apache-2.0 许可，可完全本地运行。

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

- 连接任意支持 Streamable HTTP/SSE 的 MCP 服务器
- ai agent 节点实现完整 agentic 循环（工具发现→推理→执行→循环）
- 支持任意 OpenAI 兼容 API（Ollama/vLLM/Azure/LiteLLM 等）
- 无云依赖、可完全本地运行，Apache-2.0 许可

## 适用场景

- 在 Node-RED 中可视化搭建调用 MCP 工具的 AI Agent
- 构建 MQTT→AI Agent→MQTT 的工业物联网数据处理流水线
- 制造场景的 OEE 分析、预测性维护与质量根因分析
- 快速原型验证 agentic AI 流程并可视化调试

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L16: MCP (Model Context Protocol) is the open standard by Anthropic for connecting AI to external tools and data. **This
> L24: - **AI Agent node** — full agentic loop (tool discovery → LLM reasoning → tool execution → repeat)
> L59: |**ai agent**|**Autonomous agent** — LLM + MCP tools in a reasoning loop until it has an answer|

## 星数曲线

```mermaid
xychart-beta
    title "TobiasLante/node-red-contrib-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ce0ca57ae0fd` · [字段定义](../../DATASET.md)*
