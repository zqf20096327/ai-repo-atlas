# kishormorol/CiteLens

⭐ 22 · TypeScript · MIT · 推送 2026-09-18 · [GitHub](https://github.com/kishormorol/CiteLens) · [官网](https://kishormorol.github.io/CiteLens/) · 个人维护

**给科研人员的施引文献排序工具：按影响力/相关性给引用论文打分**

面向需要梳理文献引用的研究者：输入 arXiv ID、DOI、标题或 Semantic Scholar 链接，输出按多信号加权评分排序的施引论文列表，权重为影响 45%（OpenAlex 引用百分位+FWCI）、网络 25%（引用图局部 PageRank）、相关性 20%（与种子论文标题摘要的语义相似度）、语境 10%（Semantic Scholar 高影响力引用标记），每条结果附英文解释。支持年份/综述等筛选、BibTeX/CSV 导出、引用网络图与时间线视图。前端 React，后端 FastAPI，调用 Semantic Scholar/OpenAlex/arXiv 免费 API，无需付费订阅。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四维加权评分（Impact/Network/Relevance/Context）且每条结果给出分解解释
- 支持 arXiv ID/DOI/标题/Semantic Scholar URL 等多种输入格式
- 引用网络力导向图、年度时间线、BibTeX/CSV 导出与智能筛选
- 数据来自 Semantic Scholar/OpenAlex/arXiv 免费 API，演示模式无需 API key

## 适用场景

- 找出一篇高被引论文之后真正值得读的后续工作
- 按年份、综述、高影响力等条件筛选并导出施引文献清单
- 可视化观察某论文的引用增长与引用网络结构

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L27: Output: Ranked list of citing papers, each scored across four dimensions:
> L40: |**Relevance**|20%|Semantic similarity to the seed paper (title + abstract)|

## 星数曲线

```mermaid
xychart-beta
    title "kishormorol/CiteLens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c68efe75e839` · [字段定义](../../DATASET.md)*
