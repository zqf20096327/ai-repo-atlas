# Bayer-Group/pybalance

⭐ 15 · Jupyter Notebook · BSD-3-Clause · 推送 2026-10-22 · [GitHub](https://github.com/Bayer-Group/pybalance) · [官网](https://bayer-group.github.io/pybalance) · 组织维护

**Python 混杂变量校正库：优化人群协变量平衡**

面向非随机化人群比较的混杂校正工具集：以"平衡"（两组人群相似度）度量为目标直接优化，实现线性与非线性匹配、整数规划与进化求解器、倾向性评分匹配对照，以及 MAIC、熵平衡、IPTW 等加权方法；支持患者重加权而非剔除的场景。附带可视化工具与数据模拟功能。文档说明加权尚不支持 overlap/matching weights、CBPS、稳定 IPTW 等估计量。应用示例包括制药领域构建外部对照臂，并提供论文引用请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以平衡度量为目标的直接优化，区别于倾向性评分建模
- 线性/非线性匹配，整数规划与进化求解器
- MAIC、熵平衡、IPTW 加权方法
- 平衡度量可视化与数据集模拟

## 适用场景

- 观察性研究中调整混杂协变量后再做因果推断
- 制药场景构建外部对照臂
- 非随机化两组人群的可比性分析与匹配

## 场景标签

 · 领域:统计分析/因果推断

## 证据(README 行号)

> L38: `pybalance` is a suite of tools in python for performing confounding adjustment
> L48: The `pybalance` library implements several routines for optimizing balance. To learn more

## 星数曲线

```mermaid
xychart-beta
    title "Bayer-Group/pybalance 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `013749627b56` · [字段定义](../../DATASET.md)*
