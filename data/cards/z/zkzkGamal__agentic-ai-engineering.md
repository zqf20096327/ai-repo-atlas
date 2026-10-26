# zkzkGamal/agentic-ai-engineering

⭐ 36 · Jupyter Notebook · MIT · 推送 2026-06-01 · [GitHub](https://github.com/zkzkGamal/agentic-ai-engineering) · [官网](https://zkaria-gamal.vercel.app/post/35) · 个人维护

**面向开发者的 Agentic AI 系统分章工程实践教程仓库**

以 5 个章节组织的工程学习路径：从 LLM 提供商接入（OpenAI/Gemini/Ollama）、LangChain LCEL 编排，到检索与记忆基础设施（ChromaDB/FAISS/Sentence Transformers）、LangGraph 状态图 agent 模式（ReAct、路由、多 agent、HITL），最终指向第 5 章的多节点 LangGraph 助手加 FastMCP 工具服务器的参考实现，含 pytest 测试与 GitHub Actions CI。面向构建需要状态、工具、路由与模型提供商灵活性的开发者，通过 git clone 源码与 pip 按章安装依赖运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 章递进结构：提供商抽象→LCEL 编排→RAG/记忆→agent 图模式→生产式运行时
- 第 5 章参考实现：多节点 LangGraph 助手 + FastMCP 独立工具服务器
- 支持 OpenAI、Gemini、Ollama 三类 LLM 提供商接口
- 第 5 章含 pytest 测试套件与 GitHub Actions CI 验证

## 适用场景

- 按章节系统学习 agent 系统的工程构建方法
- 参考多节点 LangGraph + MCP 的生产式架构实现
- 了解 RAG、多 agent 协作与人机协同的代码模式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L8: **Agentic AI Engineering** is a production-grade engineering resource for building modern agentic AI systems with La
> L10: The repository leads toward the architecture implemented in **Chapter 5**: a multi-node LangGraph assistant connect
> L12: This is not a beginner chatbot walkthrough. It is a structured engineering path for developers building systems tha

## 星数曲线

```mermaid
xychart-beta
    title "zkzkGamal/agentic-ai-engineering 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-26"]
    y-axis "stars" 33 --> 37
    line [34, 35, 36, 36]
```

2026-10-18 34 → 2026-10-26 36（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4639dd04c843` · [字段定义](../../DATASET.md)*
