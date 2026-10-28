# zhihengli-casia/AI-Paper-Trends

⭐ 212 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/zhihengli-casia/AI-Paper-Trends) · [官网](https://github.com/zhihengli-casia/AI-Paper-Trends/blob/main/docs/topic-atlas/README.md) · 个人维护 · 中文 README

**AI 论文索引与细粒度主题图谱：按年份/会议/主题浏览论文**

开源的 AI 论文与研究主题索引：从 OpenReview、DBLP、OpenAlex 等公开来源采集 2020-2026 年 159,732 篇论文元数据（覆盖 20+ 会议与 9 种期刊），用 BGE 嵌入 + UMAP + HDBSCAN 做逐年独立聚类，生成 7,483 个细粒度主题的静态 Markdown 图谱与 CSV 索引，提供中文主题名与可复现英文关键词标签。面向研究者与开发者，可用 CSV 做自定义分析，也可用脚本从缓存重建图谱；GitHub Actions 支持每周轻量检查与全量刷新（后者需自托管 runner 与外部缓存）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 159,732 篇论文、161 个会议-年度分组、7,483 个细粒度主题（2020-2026）
- BGE 嵌入 + UMAP + HDBSCAN + c-TF-IDF 的逐年独立聚类流水线
- 静态 Markdown 图谱 + topic_index.csv / venue_year_summary.csv 数据文件
- GitHub Actions 周度轻量检查与全量刷新引擎

## 适用场景

- 按年份、会议、主题浏览 AI 领域论文分布
- 对比不同会议/期刊各年的研究方向的冷热变化
- 下载 CSV 索引用于自定义分析与可视化
- 从缓存元数据重建或扩展自己的主题图谱

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: AI Paper Trends is an open-source index of AI papers and research topics. It tracks major AI conferences and selecte
> L24: |Papers|159,732|
> L132: 9. Build a static Markdown atlas for browsing and CSV indexes for analysis.

## 星数曲线

```mermaid
xychart-beta
    title "zhihengli-casia/AI-Paper-Trends 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-27", "2026-10-28"]
    y-axis "stars" 207 --> 212
    line [208, 209, 210, 211, 211]
```

2026-10-18 208 → 2026-10-28 211（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `083503cf88d5` · [字段定义](../../DATASET.md)*
