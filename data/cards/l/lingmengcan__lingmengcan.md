# lingmengcan/lingmengcan

⭐ 53 · Vue · MIT · 推送 2026-03-31 · [GitHub](https://github.com/lingmengcan/lingmengcan) · 个人维护 · 中文 README

**端到端 AI 应用开发平台：知识库、对话、工作流与图像生成**

基于大语言模型的应用开发平台，由 Vue 3 前端与 NestJS 微服务后端组成，提供多轮对话、知识库 RAG（文档上传、向量化、检索增强）、拖拽式工作流编排（LLM/条件/HTTP/循环/并行等节点）、插件市场与 Stable Diffusion 文生图集成。支持 OpenAI、Ollama、DeepSeek 等模型接入，使用 MySQL 与 ChromaDB，可完全本地部署；需自行安装 Node.js 18+、Python 3.10+、MySQL 8.0+ 并导入 SQL schema，README 截图声明为旧版待更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识库 RAG：多格式文档解析、ChromaDB 向量化与带引用问答
- 可视化工作流引擎：7 类节点、实时调试、JSON 导入导出
- 多模型接入：OpenAI、Ollama、DeepSeek，含负载均衡与监控
- 插件市场：动态加载、JSON Schema 配置自定义工作流节点

## 适用场景

- 企业内私有部署一套含知识库问答与 AI 绘图的应用平台
- 用可视化工作流编排 LLM、HTTP、数据库等多类型节点
- 通过 RBAC 权限体系为团队提供多用户 AI 服务

## 场景标签

`工作流自动化` `RAG` `图像生成` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L10: Lingmengcan is an end-to-end AI application development platform powered by large language models. It provides comp
> L18: - **🔄 Workflow Engine**: Drag-and-drop visual designer with rich node types and real-time debugging

## 星数曲线

```mermaid
xychart-beta
    title "lingmengcan/lingmengcan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-29 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `56ebc5abff5c` · [字段定义](../../DATASET.md)*
