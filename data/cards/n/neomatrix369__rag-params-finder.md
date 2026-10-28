# neomatrix369/rag-params-finder

⭐ 19 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/neomatrix369/rag-params-finder) · 个人维护

**RAG 参数扫描评测工具：在构建应用前找到最优检索配置**

Python/FastAPI 后端加 React 仪表盘的 RAG 参数扫描实验工具：给定数据与问题，对嵌入模型（13 个 Voyage 模型、本地 sentence-transformers、SIE、DoubleWord Qwen3-Embedding-8B）× 5 种分块方法 × 3 种检索方法（Dense/Sparse/Hybrid）做笛卡尔积实验，存储检索得分并展示各配置表现。支持 MongoDB Atlas、Postgres/pgvector、Elasticsearch、Redis 四种向量库；运行状态存 SQLite。仅做嵌入与检索评测，不调用 LLM；一条 YAML 配置加 CLI 命令即可运行，MIT 许可，当前版本 v0.12.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 嵌入模型 × 分块方法 × 检索方法的笛卡尔积扫描
- 支持 MongoDB Atlas、Postgres/pgvector、Elasticsearch、Redis 四种向量库
- 本地模型路径无需 API key，可完全离线运行
- 实验管理：暂停/恢复长扫描、取消、级联清理、生命周期跟踪

## 适用场景

- 在开发 RAG 应用前用真实数据对比不同配置的检索得分
- 对比不同向量数据库与嵌入模型组合的效果
- 跨会话持久化实验结果并复盘历次扫描

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L38: **RAG parameter sweep experimentation tool** — systematically evaluate embedding models, chunking strategies, and r
> L45: Give it your data and your questions. It runs every combination — embedding

## 星数曲线

```mermaid
xychart-beta
    title "neomatrix369/rag-params-finder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a7ef1a61dddf` · [字段定义](../../DATASET.md)*
