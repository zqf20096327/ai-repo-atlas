# JuliaML/MLDatasets.jl

⭐ 239 · Julia · MIT · 推送 2026-10-21 · [GitHub](https://github.com/JuliaML/MLDatasets.jl) · [官网](https://juliaml.github.io/MLDatasets.jl/stable) · 组织维护

**Julia 机器学习基准数据集的下载与访问通用接口包**

JuliaML 生态的社区项目，为 Julia 提供访问常用机器学习数据集的统一接口，专注于下载、解压和访问基准数据集，基于 DataDeps.jl 构建，不提供通用数据处理或可视化功能。数据集按图结构、杂项、文本、视觉四类组织，覆盖 MNIST、CIFAR10、Cora、Iris 等。通过 Julia 原生包管理器 Pkg.add 安装，MIT 许可，欢迎以 PR 形式贡献新数据集。

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

- 图结构、杂项、文本、视觉四类基准数据集
- 基于 DataDeps.jl 实现下载、解压与访问
- Julia 原生包管理器一行安装

## 适用场景

- Julia 项目中加载 MNIST、CIFAR 等常用基准数据集
- 图机器学习任务中获取 Cora、PubMed、CiteSeer 数据集
- 实验复现时统一获取基准数据

## 场景标签

 · 领域:机器学习/数据集

## 证据(README 行号)

> L7: This package represents a community effort to provide a common interface for accessing common Machine Learning datas
> L8: In contrast to other data-related Julia packages, the focus of MLDatasets.jl is specifically on downloading, unpacki

## 星数曲线

```mermaid
xychart-beta
    title "JuliaML/MLDatasets.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-27 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1e2ff366c335` · [字段定义](../../DATASET.md)*
