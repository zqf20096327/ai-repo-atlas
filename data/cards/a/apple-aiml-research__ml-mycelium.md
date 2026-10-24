# apple-aiml-research/ml-mycelium

⭐ 79 · JavaScript · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/apple-aiml-research/ml-mycelium) · [官网](https://apple.github.io/ml-mycelium) · 组织维护

**机器学习模型结构的有向无环图可视化库**

Apple AIML Research 出品的 Svelte 图可视化库，用于快速生成机器学习模型（或任意有向无环图）的交互式图表示，是 Talaria（ACM CHI 2024）论文可视化工具的图形引擎。功能包括可自定义的节点标签与提示、层级模型节点的展开/折叠、基于 SVG 但可处理数千节点的图，并支持为自定义数据格式编写加载器。由三部分组成：Svelte 组件库、多种格式的加载器、以及用于测试开发的 SvelteKit 网页应用。通过 npm 发布，也可 pnpm pack 后 vendor 进项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持任意 DAG 的通用图可视化，非限于 ML 模型
- 层级节点展开/折叠，SVG 承载数千节点
- 可自定义数据格式加载器
- Talaria（ACM CHI 2024）的图形可视化引擎

## 适用场景

- 为 ML 模型分析工具嵌入模型结构图可视化
- 浏览大型层级模型的结构
- 以独立网页应用快速查看自定义格式的模型图

## 场景标签

 · 领域:机器学习/可视化

## 证据(README 行号)

> L3: Mycelium is a library for quickly creating graph visualizations of machine learning models (or any directed acyclic 
> L4: It was created to power the graph representations of Talaria (ACM CHI 2024 Best Paper Honorable Mention) — which is 

## 星数曲线

```mermaid
xychart-beta
    title "apple-aiml-research/ml-mycelium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-24 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `76144733ba68` · [字段定义](../../DATASET.md)*
