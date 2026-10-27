# brucechou1983/chainlit_langgraph

⭐ 97 · Python · MIT · 推送 2025-12-19 · [GitHub](https://github.com/brucechou1983/chainlit_langgraph) · 个人维护

**Chainlit+LangGraph 集成模板：快速搭建多模型对话 AI 应用**

将 Chainlit 对话界面与 LangGraph 状态图框架结合的项目模板，供开发者快速构建并部署对话式 AI agent。自动检测并支持多种 LLM（Ollama、Claude、GPT、Grok、Groq、Gemini），通过继承 BaseState/BaseWorkflow 编写自定义工作流，内置简单聊天、多模态聊天、简历优化、Lean Canvas 等示例工作流。以 Docker Compose 启动，附带 PostgreSQL 与 MinIO 服务；也可在 Python 3.10 虚拟环境中运行。MCP、研究助手、NVIDIA NIM 等列于待开发功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测多种 LLM（Ollama/Claude/GPT/Grok/Groq/Gemini）
- 继承 BaseState/BaseWorkflow 自定义 LangGraph 状态图工作流
- Docker Compose 一键启动（Chainlit 应用+PostgreSQL+MinIO）
- 内置简单聊天、多模态、简历优化、Lean Canvas 示例工作流

## 适用场景

- 基于开源模型（Ollama）本地搭建对话 AI agent
- 快速原型验证多 LLM 切换的聊天应用
- 通过自定义工作流扩展自己的对话 agent 逻辑

## 场景标签

`Agent 框架` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L8: Rapidly build and deploy production-ready conversational AI agents using Chainlit and LangGraph. This powerful integ
> L20: - **Building Blocks**: Utilize a variety of building blocks to create your own conversational AI agents.
> L86: 3. Define Your Workflow

## 星数曲线

```mermaid
xychart-beta
    title "brucechou1983/chainlit_langgraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-27 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fdb148a961eb` · [字段定义](../../DATASET.md)*
