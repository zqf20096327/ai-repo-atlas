# tmasjc/deka-oss

⭐ 54 · Python · MIT · 推送 2026-07-14 · [GitHub](https://github.com/tmasjc/deka-oss) · [官网](https://tinyurl.com/s33sstx4) · 个人维护 · 中文 README

**人机协同工作台：把专家直觉转化为可复用的语料标注**

面向领域专家的人机协同标注工作台（Web 应用）：通过 Probe（交互调优混合检索）→ Harvest（嵌入邻域全量扫描）→ Refine（LLM 依据语言规则判样）→ Apply（训练低成本分类器全量标注）四个阶段，将专家对“找类似内容”的直觉判断升级为可复现、可规模化的标注数据集与持久化 logistic 回归分类器。依赖 uv/Python 3.11、Node.js 18，运行时需自备 Milvus 向量库、Embeddings 服务与 OpenRouter 兼容 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段流程：混合检索调优→邻域收割→LLM 规则精炼→分类器全量标注
- 产出自包含标注数据集（merged.csv）与零 LLM 成本的持久化分类器
- 混合（dense + learned-sparse）检索与 RRF 融合，含收敛指标（PQK/FIT/NOT_FIT）
- FastAPI 后端 + React/Vite 前端，cookie 会话鉴权

## 适用场景

- 把专家的隐性相关性判断转化为语料级的可复用标注
- 为无法用关键词表达的概念型查询构建带标签数据集
- 训练低成本分类器对同概念的未来数据持续打标

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L10: Deka — **Definition and Embedding Knowledge Alignment** —
> L21: |**3.&nbsp;Refine**|Distil that geometric cohort into an explicit, auditable language rubric, then judge a stratifi
> L22: |**4.&nbsp;Apply**|Train a low-cost classifier on the rubric-judged sample to label the full cohort at near-zero ma

## 星数曲线

```mermaid
xychart-beta
    title "tmasjc/deka-oss 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 53 --> 56
    line [55, 54, 54]
```

2026-10-18 55 → 2026-10-24 54（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ba766f3875c6` · [字段定义](../../DATASET.md)*
