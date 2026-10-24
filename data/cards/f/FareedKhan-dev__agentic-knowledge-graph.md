# FareedKhan-dev/agentic-knowledge-graph

⭐ 66 · Jupyter Notebook · NOASSERTION · 推送 2026-08-15 · [GitHub](https://github.com/FareedKhan-dev/agentic-knowledge-graph) · 个人维护

**基于结构化元数据的知识图谱 RAG：在 PubMedQA 上做可溯源问答研究**

覆盖完整 PubMed 2026 基线的引用与本体知识图谱研究项目：图结构（9.29 亿条边）完全由 NLM 已发布的引用关系与人工 MeSH 标引构建，零 LLM 抽取调用；检索用 bge-small-en-v1.5 精确搜索，生成端用本地运行的 Qwen2.5-14B-Instruct 以受限解码产出 yes/no/maybe 后验，在 600 题留出集上得 83.2%。面向研究人员与开发者，提供 196 格已执行 notebook 与可复现脚本，CPU 十秒级复现（GPU 部分预计算并缓存），无需 GPU、语料下载或 API key。README 以负结果同等篇幅记录四次自我推翻的结论。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 929,824,202 条边全部来自 NLM 结构化元数据，图构建零 LLM 调用（10.8 分钟）
- 受限解码读取 yes/no/maybe 三 token 后验，支持校准与弃答分析
- DEV 400 / TEST 600 留出评测协议：DEV 拟合、TEST 单次评分、配对 McNemar 与 bootstrap CI
- 仓库自带已执行 notebook 与 run_all.py，CPU 约 10 秒复现全部数字

## 适用场景

- 复现一个端到端知识图谱 RAG 基准的全部实验数字
- 研究引用/MeSH 元数据构建知识图谱与 LLM 抽取图的成本/溯源差异
- 考察受限解码、校准与评测协议设计在生物医学 QA 上的效果

## 场景标签

`模型评测` `知识图谱` `RAG` · 领域:评测与运维

## 证据(README 行号)

> L18: > The knowledge graph is built from **929,824,202 edges** with **zero LLM calls**,
> L166: The generator is `Qwen2.5-14B-Instruct`, run locally in bf16. Labels are obtained
> L15: > **83.2%** on 600 held-out PubMedQA questions (95% CI 80.2 to 86.2), against a

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/agentic-knowledge-graph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-24 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1ace2de77a69` · [字段定义](../../DATASET.md)*
