# mahmoudsamy7729/agentic-rag

⭐ 18 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/mahmoudsamy7729/agentic-rag) · 个人维护

**面向生产的认证式 Agentic RAG 全栈应用模板（FastAPI）**

基于 FastAPI 的生产导向 RAG 起始工程：带 JWT 认证、文档所有权与按文档作用域检索，支持文本与 PDF 摄取、Chroma 向量存储、可插拔嵌入（OpenAI/Hugging Face）与可选 Cohere 重排、Postgres+pgvector 语义缓存、带工具调用的 Agent 循环，以及含 Hit@k/MRR/LLM 裁判指标的评测流水线与内置 Jinja UI。面向开发者，通过 Docker Compose 或 uv 本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 带工具调用的 Agent 循环与按文档作用域检索
- 检索指标（Hit@k/Recall@k/MRR）+ LLM 裁判答案指标的评测流水线，支持运行历史与失败重跑
- Postgres+pgvector 语义缓存与页面级引用
- JWT 认证、文档所有权与软删除

## 适用场景

- 作为生产级 RAG 应用的起始工程快速搭建问答服务
- 对自己的 RAG 系统跑检索与答案质量评测并对比历史运行
- 需要认证与文档隔离的内部知识问答部署

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Production-oriented FastAPI starter for authenticated, document-scoped, evaluation-driven RAG systems.
> L45: - Agent loop with tool calling
> L103: - `POST /agent/ask`

## 星数曲线

```mermaid
xychart-beta
    title "mahmoudsamy7729/agentic-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f45ef5ae01c7` · [字段定义](../../DATASET.md)*
