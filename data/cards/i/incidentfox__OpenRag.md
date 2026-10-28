# incidentfox/OpenRag

⭐ 43 · Python · MIT · 推送 2026-02-03 · [GitHub](https://github.com/incidentfox/OpenRag) · 个人维护

**多策略 RAG 检索系统：RAPTOR+图+HyDE+BM25+神经重排**

面向多跳问答检索场景的完整 RAG 实现：组合 RAPTOR 层级检索、知识图谱、HyDE、BM25 混合检索与 Cohere 神经重排，在 MultiHop-RAG 全量 2,556 查询上报告 72.89% Recall@10，并附消融实验与成本分析（每查询约 $0.0025）。以 Python 服务形式运行（本地 8000 端口 API，支持查询/批量摄取/树持久化），提供 fast/standard/thorough 三档检索模式。嵌入依赖 OpenAI API（必需），重排默认走 Cohere 云端 API，隐私敏感场景可切换本地 BGE cross-encoder 免外部调用。另含 MultiHop-RAG、CRAG、SQuAD 基准评测脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 组合 RAPTOR 层级检索、知识图谱、HyDE、BM25 与神经重排的多策略流水线
- MultiHop-RAG 全量基准 72.89% Recall@10，含组件级消融实验
- 本地 API 服务：查询/批量摄取/RAPTOR 树保存加载
- 可切换本地 CrossEncoderReranker（BAAI/bge-reranker-base），无需外部 API

## 适用场景

- 搭建面向多跳问答的高召回检索服务
- 在 MultiHop-RAG、CRAG、SQuAD 上复现或评测 RAG 策略
- 通过消融实验了解各检索组件的召回贡献

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: - 🔧 **Full RAG Implementation** (`ultimate_rag/`) - RAPTOR + Graph + HyDE + BM25 + Neural Reranking
> L101: curl -X POST http://localhost:8000/query \
> L35: python -m api.server

## 星数曲线

```mermaid
xychart-beta
    title "incidentfox/OpenRag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-28 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c4019b235eff` · [字段定义](../../DATASET.md)*
