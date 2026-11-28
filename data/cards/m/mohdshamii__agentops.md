# mohdshamii/agentops

⭐ 10 · Python · 推送 2026-10-24 · [GitHub](https://github.com/mohdshamii/agentops) · 个人维护

**探索 Agent 架构的个人项目：多步推理、工具执行与向量记忆**

一个用于学习多步 AI Agent 架构的开源个人项目。核心机制是模型适配器层，将 Agent 逻辑与模型提供方解耦，可在运行时切换 LLaMA 3.2、Mistral 7B、Qwen 2.5、DeepSeek R1 等 open-weight 模型，并附带 OpenAI 兼容与本地回退适配器。功能覆盖 ReAct 推理循环（SSE 流式输出）、滑动窗口短期记忆、基于 MiniLM-L6-v2 的本地向量长期记忆、网页抓取/HTTP/SQL/Python 执行工具，前端 Next.js 14，后端 Flask/FastAPI，支持 Docker。README 明确声明为早期阶段学习项目，列出无鉴权、代码执行未加固、向量存储不可扩展等已知缺口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 适配器层解耦 Agent 逻辑与模型提供方，运行时可切换模型
- ReAct 推理循环，推理步骤经 SSE 流式输出到界面
- 短期滑动窗口记忆 + MiniLM-L6-v2 本地向量存储（余弦相似度检索）
- 工具集含网页抓取/搜索、HTTP 客户端、SQL 与 Python 执行，经 REST API 暴露

## 适用场景

- 学习和研究多步 Agent 的架构组成方式
- 自托管一个可切换 open-weight 模型的对话与工作流界面
- 需要本地向量记忆与工具调用能力的 Agent 实验

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: AgentOps is an open-source project I'm building to understand how multi-step AI agents are put together. The core id
> L7: > **Status: early-stage learning project, not a production system.** See Known Gaps before running it anywhere that 
> L23: |**Model adapters**|`ModelAdapterFactory` decouples agent logic from the provider. Hugging Face router, OpenAI-comp


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `7fab870ab900` · [字段定义](../../DATASET.md)*
