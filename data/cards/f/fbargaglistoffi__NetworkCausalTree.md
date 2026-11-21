# fbargaglistoffi/NetworkCausalTree

⭐ 10 · R · NOASSERTION · 推送 2026-11-16 · [GitHub](https://github.com/fbargaglistoffi/NetworkCausalTree) · 组织维护

**面向科研人员的网络干扰下异质处理效应 R 分析包**

R 语言包，用树算法结合 Horvitz-Thompson 估计量，在聚类网络干扰下识别处理效应与溢出效应的异质性子群。适用于随机干预实验且干扰限于簇内、邻居暴露可表示为至少一个已处理邻居、个体分配服从已知独立 Bernoulli 设计的场景；含隔离节点的网络会被拒绝输入。要求输入为有限二元对称无跨簇边的邻接矩阵。安装方式为 devtools 从 GitHub 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 树发现与 leaf 级 design-based 估计相结合的直接/溢出效应异质性识别
- 输出四种对比效应，拒绝含隔离单元的网络
- 内置 data_generator_direct 与 data_generator_direct_indirect 数据生成器

## 适用场景

- 分析社交网络中随机干预实验的直接与溢出效应异质性
- 为政策干预寻找应优先投放的子群体
- 在干扰限于簇内的实验设计中估计 leaf 级效应

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: The `NetworkCausalTree` package introduces a machine learning method that uses tree-based algorithms and an Horvitz-
> L7: `NetworkCausalTree` is intended for researchers analyzing randomized interventions in populations with observed netw

## 星数曲线

```mermaid
xychart-beta
    title "fbargaglistoffi/NetworkCausalTree 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `2f9cf345a478` · [字段定义](../../DATASET.md)*
