# tuned-org-uk/arrowspace-rs

⭐ 43 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/tuned-org-uk/arrowspace-rs) · [官网](https://tuned-org-uk.github.io/) · 个人维护

**基于谱/色散模型的 Rust 向量分析与搜索库**

Rust 编写的向量数据库库：以 λτ（lambda-tau，Rayleigh-Laplacian 混合）索引为核心，在行主序稠密数组上为每行计算谱感知得分，构建向量搜索友好的查找表；支持 λτ 相似度搜索、范围查询、行级 superposition 与逐元素乘法等组合操作，另提供图构建（Laplacian 图、超图覆盖、集成变体）与可选 filter-bank 特征（默认关闭）。面向需要在谱特征上找匹配的开发者，提供 Python 绑定，通过 Cargo 依赖或源码编译安装，要求 Rust 1.90+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- λτ 索引：Rayleigh-Laplacian 评分构建谱感知向量搜索
- λ 图、超图覆盖与集成变体等图构建模式
- 行级 superposition 与逐元素乘法等代数操作
- 提供 Python 绑定与示例（如蛋白 lookup 范围查询）

## 适用场景

- 在高维向量数据上做谱感知的相似度搜索与范围查询
- 对数据集做图表征与谱特征分析
- 常规距离度量排序不理想时寻找备选匹配方式

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: `arrowspace` is a database for vectors supported by a graph representation and a key-value store. The main use-cases
> L11: `ArrowSpace` is the data structure that encapsulates the use of `λτ` (lambda-tau) indexing; a novel scoring method 

## 星数曲线

```mermaid
xychart-beta
    title "tuned-org-uk/arrowspace-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0d8440d234e8` · [字段定义](../../DATASET.md)*
