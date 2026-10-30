# jg-you/dyvider

⭐ 16 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/jg-you/dyvider) · 个人维护

**网络一维线性聚类的动态规划精确算法库**

dyvider 是一个 Python 小型包，实现用于网络精确线性聚类的动态规划算法。算法处理节点具有一维位置的网络，返回最优划分；典型流程是先用一维谱嵌入为节点赋分，再从中检索最优线性聚类。仅依赖 networkx 和 numpy，需 Python 3.10+，支持 uv 或 pip 安装，附 Jupyter 教程笔记本。算法出自 Patania、Allard 与 Young 的论文（arXiv:2301.10403），代码由 Jean-Gabriel Young（佛蒙特大学）编写。适用对象是做网络聚类研究的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 动态规划求网络一维线性聚类的精确最优解
- 仅依赖 networkx 和 numpy
- 提供 Jupyter 教程笔记本覆盖全部 API 调用

## 适用场景

- 对具有一维节点位置的网络求最优划分
- 结合谱嵌入做网络线性聚类分析
- 复现论文中的算法与实验

## 场景标签

 · 领域:图算法/网络科学

## 证据(README 行号)

> L3: **dyvider** is a small package implementing dynamic programming algorithms for exact linear clustering in networks.
> L4: Its algorithms process networks whose nodes have positions in one dimension, and return their optimal partition.
> L52: The following minimal example first assigns scores to nodes with a one-dimensional spectral embedding and then retr

## 星数曲线

```mermaid
xychart-beta
    title "jg-you/dyvider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `697dc92f8d42` · [字段定义](../../DATASET.md)*
