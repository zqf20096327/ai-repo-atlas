# jjiantong/Awesome-KV-Cache-Optimization

⭐ 428 · Python · 推送 2026-11-26 · [GitHub](https://github.com/jjiantong/Awesome-KV-Cache-Optimization) · [官网](https://jjiantong.github.io/Awesome-KV-Cache-Optimization/) · 组织维护 · 中文 README

**LLM 推理 KV Cache 优化论文的持续更新清单**

配套 ACL 2026 Findings 综述论文的论文集合仓库，维护一个持续更新的 system-aware、serving-time、KV-centric 优化方法收藏。按系统行为导向的分类法组织文献：Temporal（何时访问/计算 KV）、Spatial（KV 放置与迁移）、Structural（KV 表示与管理）三大维度。不重训、不改架构，聚焦提升系统指标的方法。每条以表格列出论文、类型描述与代码链接，并附 News 更新日志与工具/仿真/基准资源章节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 Temporal/Spatial/Structural 系统行为分类法组织 KV Cache 优化文献
- 持续更新：2026-10 新增 63 篇、2026-06 新增 51 篇
- 收录 FlashInfer、Mooncake、SGLang 等带代码与星标的项目
- 配套交互式论文浏览器网站与工具/基准资源章节

## 适用场景

- 调研 LLM serving 与 KV Cache 优化相关论文
- 为推理系统设计查找调度、缓存管理等方向的相关工作
- 跟踪 KV Cache 优化领域的最新进展

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L9: This repository accompanies our survey paper (**ACL 2026 Findings**):
> L15: This repository maintains a continuously updated collection of **system-aware, serving-time, KV-centric** optimizat

## 星数曲线

```mermaid
xychart-beta
    title "jjiantong/Awesome-KV-Cache-Optimization 星数(近 9 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-31", "2026-11-08", "2026-11-10", "2026-11-13", "2026-11-16", "2026-11-25", "2026-11-28"]
    y-axis "stars" 421 --> 429
    line [423, 422, 423, 425, 427, 426, 427, 428, 428]
```

2026-10-26 423 → 2026-11-28 428（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `8e670765dce4` · [字段定义](../../DATASET.md)*
