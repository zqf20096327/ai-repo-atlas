# Saichandra2520/AgentForge

⭐ 22 · Python · MIT · 推送 2026-04-28 · [GitHub](https://github.com/Saichandra2520/AgentForge) · [官网](https://github.com/Saichandra2520/agentforge#readme) · 个人维护

**一条 CLI 命令生成生产级 Python AI agent 项目脚手架**

create-agent-app（AgentForge）是一个 Python CLI 脚手架工具：通过交互式流程选择模板与选项，生成基于 LangGraph 模式的 agent 项目，覆盖 ReAct 工具调用、RAG（含语义缓存与安全护栏可选）、多 agent Supervisor、会话式与人机协同五类模板。生成的项目含可运行 main.py、config.yaml/.env.example、可选 FastAPI API 路由、tests 与 Docker 工件，并自动初始化 git。支持 Groq、Gemini、Azure OpenAI、Ollama 四个 LLM 提供方，凭据经 .env 配置。以 PyPI 包形式分发，MIT 许可。

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

- 五种 agent 架构模板（ReAct/RAG/多agent Supervisor/会话式/HITL）
- 交互式选择模板、提供方、API 后端、流式、Docker、测试等选项
- RAG 模板可选语义缓存与安全护栏（security/ 模块）
- Jinja 模板渲染，生成结构可扩展、不锁定

## 适用场景

- 团队按统一结构快速起一个新的 agent 项目
- 从零搭建带工具调用的 ReAct 助手或 RAG 问答服务
- 为 agent 项目一键附带 FastAPI 后端、测试与 Docker 配置

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Scaffold production-ready Agentic AI projects in Python with one command.
> L5: `create-agent-app` generates opinionated, extensible project templates built around LangGraph patterns, modern provi
> L23: |`react_agent`|Tool-using assistants with iterative reasoning|ReAct loop with LangGraph + tool execution|

## 星数曲线

```mermaid
xychart-beta
    title "Saichandra2520/AgentForge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `993eb5ee0fbe` · [字段定义](../../DATASET.md)*
