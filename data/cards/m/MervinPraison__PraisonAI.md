# MervinPraison/PraisonAI

⭐ 9,377 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/MervinPraison/PraisonAI) · [官网](https://praison.ai) · 组织维护

**可完全离线运行的 Python AI agent 框架**

开源 Python agent 框架，支持在本地计算机上运行 AI agent，配合本地模型可完全离线、无需 API key。功能覆盖单/多 agent 协作、工作流（路由/并行/循环）、记忆与 RAG、工具与 MCP、护栏与人工审批、追踪评估、微调与部署，提供 CLI、YAML 无代码配置、JavaScript SDK 与桌面应用。面向开发者构建 agent 应用，同时为高监管团队提供任务交接的早期访问企业产品。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 配合 Ollama/vLLM/LM Studio 可完全离线运行，无需 API key
- 五层 agent 架构：Prompt/Context/Harness/Loop/Graph，含 doom-loop 检测
- 支持 YAML 无代码配置、MCP、护栏、人工审批、AgentFlow 工作流
- 提供 CLI、桌面应用（macOS/Windows/Linux）与 JavaScript/TypeScript SDK

## 适用场景

- 在本地离线环境运行 agent 处理私有数据
- 构建多 agent 工作流自动化业务流程
- 部署支持 Telegram/Discord/Slack 的客服机器人
- 生成代码、内容或执行数据分析任务

## 场景标签

`Agent 框架` `多智能体` `RAG` `微调` · 领域:Agent 开发

## 证据(README 行号)

> L14: - **For everyone else:** a free, open-source Python agent framework. With a local model you need no API key and pay
> L102: - **Agents and multi-agent teams:** Agents · Handoffs · Workflows
> L107: - **Your choice of model:** Models · Model router

## 星数曲线

```mermaid
xychart-beta
    title "MervinPraison/PraisonAI 星数(近 24 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 9261 --> 9387
    line [9271, 9281, 9284, 9285, 9289, 9292, 9296, 9300, 9304, 9307, 9308, 9310, 9312, 9289, 9327, 9334, 9333, 9336, 9337, 9340, 9342, 9344, 9372, 9377]
```

2026-10-20 9,271 → 2026-11-22 9,377（+106）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `fbefa7fbe334` · [字段定义](../../DATASET.md)*
