# kafein-technology/KAI-Flow

⭐ 56 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/kafein-technology/KAI-Flow) · [官网](https://kaiflow.io) · 组织维护

**节点式可视化 AI 工作流编排平台，用于搭建 LLM/Agent/RAG 应用**

拖拽式可视化画布平台，用于设计、测试与部署 AI 助手工作流：节点类型覆盖 LLM、Agent、工具（网页搜索、代码执行）、记忆、向量库、文档加载与定时触发。后端基于 FastAPI，集成 LangChain/LangGraph/LangSmith，向量存储使用 PostgreSQL+pgvector，带 JWT 认证（支持 Keycloak）、APScheduler 定时调度，并可将 Agent 导出为可嵌入网页的聊天组件。提供 Docker Compose 一键部署与 Python venv/Conda 本地开发两条路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- XYFlow 12 驱动的拖拽式可视化工作流构建器
- 集成 LangChain/LangGraph/LangSmith 构建与调试 Agent 流程
- PostgreSQL+pgvector 向量存储与语义检索
- Agent 可导出为 npm 嵌入式聊天组件，支持 cron 定时调度

## 适用场景

- 用可视化画布搭建问答、文档处理、自动化任务等 AI 助手
- 在自有网站嵌入平台构建的聊天 Agent
- 定时调度并运行 LLM/RAG 工作流

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L22:  KAI Flow: a visual platform for building AI-powered assistants
> L172: * **Visual Workflow Builder**: Drag-and-drop interface powered by XYFlow 12 for creating AI agents and chains.
> L174: * **AI/ML Framework**: Integrated LangChain, LangGraph, and LangSmith for building and debugging complex agent flo

## 星数曲线

```mermaid
xychart-beta
    title "kafein-technology/KAI-Flow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-30 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `372af2b2728d` · [字段定义](../../DATASET.md)*
