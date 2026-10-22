# leonyangdev/lc-studylab

⭐ 404 · Python · MIT · 推送 2025-12-09 · [GitHub](https://github.com/leonyangdev/lc-studylab) · 个人维护 · 中文 README

**基于 LangChain v1.0 的智能体学习与实践全栈示例平台**

以学习和研究为导向的 LangChain v1.0.3 全栈示例项目，按五个渐进式阶段组织：基础 Agent 与工具调用（含流式输出、FastAPI 接口、CLI）、RAG 知识库（多格式加载、FAISS 向量索引、多种检索策略）、LangGraph 有状态工作流（SQLite 检查点、人机交互、SSE）、DeepAgents 多智能体协作研究与 Guardrails 安全机制（注入检测、脱敏、三级安全等级）。后端 Python/FastAPI，前端 Next.js，支持 Docker Compose 一键部署或本地开发部署，需配置 API key 环境变量，模型支持 OpenAI、DeepSeek、Anthropic、Ollama 等。

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

- 五阶段渐进式覆盖 LangChain v1.0.3：Agent/RAG/LangGraph/DeepAgents/Guardrails
- RAG 模块含多格式文档加载、FAISS 索引与相似度/MMR/阈值检索策略
- Guardrails 含 Prompt Injection 检测、敏感信息脱敏与三级安全等级
- Docker Compose 一键部署前后端，另提供 CLI 与 FastAPI 接口

## 适用场景

- 系统学习 LangChain v1 各核心组件的用法与设计模式
- 作为构建生产级 AI 智能体系统的参考实现或实践模板
- 本地搭建可交互的 RAG 知识库与多智能体研究演示

## 场景标签

`教程课程` `Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L12: LC-StudyLab 是一个以学习和研究为导向的 LangChain v1.0.3 全栈示例项目，系统性地集成了 LangChain 生态的核心能力。项目采用模块化设计，分为五个渐进式阶段，每个阶段对应 LangChain 文档
> L16: - 学习平台：系统学习 LangChain v1.0.3 的完整能力地图
> L17: - 实践模板：可直接用于构建生产级 AI 智能体系统

## 星数曲线

```mermaid
xychart-beta
    title "leonyangdev/lc-studylab 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 401 --> 405
    line [402, 403, 404]
```

2026-10-18 402 → 2026-10-22 404（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `599956f1e033` · [字段定义](../../DATASET.md)*
