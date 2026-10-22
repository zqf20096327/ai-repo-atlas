# phurwicz/hover

⭐ 330 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/phurwicz/hover) · [官网](https://phurwicz.github.io/hover) · 个人维护

**面向向量化数据的批量标注工具：在散点图上圈选打标**

基于 Bokeh 的 Python 数据标注工具：将可表示为向量的数据点渲染为语义散点图，用户通过悬停查看、套索圈选、表格检视与搜索组件筛选数据，批量赋予标签供监督学习使用。附带补充视图：按条件过滤的 Finder、基于模型预测分数的 SoftLabel 主动学习、自定义标注/过滤函数的 Snorkel。支持 Python 3.8+ 与 Linux/macOS/Windows，通过 PyPI 与 Conda 安装，提供浏览器内代码运行与无代码 Binder 两种在线演示。

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

- 语义散点图 + 套索圈选的批量标注交互
- SoftLabel 主动学习：模型预测分数参与标注循环
- Snorkel 自定义函数用于标注与过滤
- 支持 3D/4D 维度切换、跨视图连续选择与异常点剔除

## 适用场景

- 为监督学习模型准备带标签训练数据
- 对高维向量数据做聚类检视与批量打标
- 结合主动学习降低标注工作量

## 场景标签

 · 领域:机器学习/数据标注

## 证据(README 行号)

> L18: `hover` is a tool for mass-labeling data points that can be represented by vectors.
> L57:  `SoftLabel`: active learning by in-the-loop model prediction score

## 星数曲线

```mermaid
xychart-beta
    title "phurwicz/hover 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 329 --> 331
    line [330, 330]
```

2026-10-18 330 → 2026-10-22 330（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `64c58475632e` · [字段定义](../../DATASET.md)*
