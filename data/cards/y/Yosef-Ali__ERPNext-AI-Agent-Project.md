# Yosef-Ali/ERPNext-AI-Agent-Project

⭐ 21 · Python · 推送 2026-05-05 · [GitHub](https://github.com/Yosef-Ali/ERPNext-AI-Agent-Project) · 个人维护

**面向 ERPNext 的多智能体 AI 助手：语义检索与文档处理**

为 ERPNext 开发者和用户提供智能助手：通过自然语言语义检索 ERP 单据（发票、订单、客户），自动生成 Frappe DocType JSON、控制器与工作流，构建客户/订单/项目知识图谱，并以多智能体流水线处理需求分析到实现，支持 PDF/DOCX/Excel 摄入与自动索引。技术栈含 LangChain、OpenAI/Anthropic、ChromaDB/FAISS、Neo4j，并使用 Gymnasium/Stable-Baselines3 做强化学习训练。需 Python 3.10+，Neo4j、Redis 为依赖，推荐 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言语义检索 ERPNext 单据
- 从业务描述自动生成 Frappe DocType JSON、控制器与工作流
- 多智能体流水线（需求分析→架构→Schema→实现）
- PDF/DOCX/Excel 文档摄入与自动索引

## 适用场景

- 用自然语言查找 ERPNext 中的发票、订单和客户单据
- 描述业务需求自动生成 DocType 与工作流
- 对 ERP 文档做语义索引与知识图谱关联查询

## 场景标签

`多智能体` `语义搜索` `知识图谱` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L7: - **Semantic Search** — Find any ERPNext document (invoices, orders, customers) using natural language
> L10: - **Multi-Agent Pipeline** — Specialized agents handle requirements analysis → architecture → schema → implementati

## 星数曲线

```mermaid
xychart-beta
    title "Yosef-Ali/ERPNext-AI-Agent-Project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ceec3d9bea12` · [字段定义](../../DATASET.md)*
