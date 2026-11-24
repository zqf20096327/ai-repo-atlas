# cloro-dev/web-search-api-benchmark

⭐ 3 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/cloro-dev/web-search-api-benchmark) · [官网](https://cloro.dev/blog/web-search-api-benchmark/) · 组织维护

**面向 AI agents 的 Web 搜索 API 基准评测：10 家 API 的准确率/成本/延迟**

一个开放的 Web 搜索 API 基准，在 SimpleQA Verified（1,000 题）、FreshQA（358 题）和 FRAMES（824 题多跳问答）共 2,182 个问题上，对 cloro、SerpApi、Tavily、Exa、Parallel、Brave、Perplexity、Firecrawl、You.com、Keenable 十个搜索 API 统一测量准确率、每千次搜索成本与 p50 延迟。机制上每个问题每家 API 只做一次搜索，统一使用同一 reader（gemini-3.8-flash）与同一 grader，含 95% Wilson 区间与配对显著性检验；报告中标注了 Perplexity/Keenable 的数据集泄漏过滤与 You.com 的查询长度限制。代码、设置与全部判分答案随仓库开放。注意维护者 cloro 本身是受测 API 之一。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 2,182 个问题、10 个 Web 搜索 API 的统一基准
- 统一 reader 与 grader（Gemini 模型），每 API 每题一次搜索
- 输出准确率（含 95% 区间与配对检验）、每千次搜索成本与 p50 延迟
- 代码、运行设置与逐题判分答案开放在仓库中

## 适用场景

- 为 AI agent 或 RAG 管线选型 Web 搜索 API
- 对比各搜索 API 在短事实/时效性/多跳问题上的表现
- 查询各搜索 API 的免费额度与千次搜索价格

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L48: An open benchmark of ten web search APIs for AI agents and RAG pipelines:
> L54: `gemini-3.8-flash`, and the same grader, `gemini-pro-latest`, in November 2026. The code,
> L55: the settings and every graded answer are in this repo.

## 星数曲线

```mermaid
xychart-beta
    title "cloro-dev/web-search-api-benchmark 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2d299e24f25d` · [字段定义](../../DATASET.md)*
