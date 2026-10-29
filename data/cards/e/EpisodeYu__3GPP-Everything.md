# EpisodeYu/3GPP-Everything

⭐ 18 · Python · AGPL-3.0 · 推送 2026-08-13 · [GitHub](https://github.com/EpisodeYu/3GPP-Everything) · [官网](https://3gpp-everything.org/) · 个人维护 · 中文 README

**面向 3GPP 5G 规范的 RAG 问答 Agent：自然语言提问，带段落级原文引用**

对 GSMA 发布的 Rel-18/19 全部 5G 系列 TS（1270 篇 / 394,859 段落块）做检索增强问答的 Agent 系统，供协议工程师与标准研究人员使用。检索采用 Qdrant dense + BM25 sparse + RRF 融合 + Voyage rerank，编排用 LangGraph；回答内嵌 [N] 索引引用并由后端回填 spec/section 元数据，跳转章节阅读器。严格 grounding：仅基于检索内容生成，self-RAG 独立模型三维自评。提供 Docker Compose standalone 一条命令部署，生成 LLM 经 LiteLLM 可配置切换，附带与华为 Telco-RAG 的对比评测。限制：不开放自助注册，需模型上游 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hybrid 检索（Qdrant dense 1024 维 + BM25 + RRF）→ Voyage rerank → LLM 生成
- 段落级 [N] 引用，后端回填 spec/section 元数据并可点击跳转原文
- self-RAG 独立模型 grounding/coverage/confidence 三维自评（最多 retry 2 次）
- Docker Compose standalone 把 Qdrant/LiteLLM/PostgreSQL/Redis 全部打进一条命令起整栈

## 适用场景

- 用自然语言查询 3GPP 5G 规范并核对其原文出处
- 跨多份 TS 文档做多实体、多文档对比推理
- 团队自托管一套带鉴权、配额与反馈溯源的规范问答系统

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L12: 一个对 3GPP 标准文档做深度 RAG 的 Agent 系统，覆盖 GSMA 发布的 **Rel-18 + Rel-19 全部 5G 系列 TS（1270 篇 / 394,859 段落块）**。核心是：用自然语言问 3GPP，拿
> L26: |**检索增强问答**|Hybrid 检索（Qdrant dense 1024 维 + BM25 sparse + RRF 融合）→ Voyage rerank → LLM 生成；small2big 召回（命中小块、回展父 sec
> L28: |**严格 grounding**|仅基于检索内容生成；查无证据明示"未在 3GPP 文档中找到"；self-RAG 用独立模型做 grounding/coverage/confidence 三维自评（最多 retry 2 次强制

## 星数曲线

```mermaid
xychart-beta
    title "EpisodeYu/3GPP-Everything 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ca0431021791` · [字段定义](../../DATASET.md)*
