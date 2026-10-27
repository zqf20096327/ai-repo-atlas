# panagiotisanagnostou/HiPart

⭐ 56 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/panagiotisanagnostou/HiPart) · [官网](https://hipart.readthedocs.io/) · 组织维护

**分裂式层次聚类算法库：可交互可视化操纵聚类过程**

纯 Python 实现的开源分裂式层次聚类工具箱，提供 DePDDP 等算法的执行、聚类预测输出及交互式可视化界面，用户可在可视化中直接操纵执行步骤干预聚类结果。支持 KernelPCA 结合与距离矩阵输入，面向大数据场景关注计算效率，依赖均为内置或稳定维护的外部包。要求 Python 3.8 及以上，pip 安装，仓库附带多个示例文件与完整文档，成果有论文可引用。

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

- DePDDP 等分裂式层次聚类算法的 fit_predict 接口
- 交互式可视化允许直接操纵执行步骤干预聚类结果
- 支持 KernelPCA 方法与距离矩阵输入
- 面向大数据应用关注计算效率

## 适用场景

- 对高维数据做可解释的分裂式层次聚类
- 通过交互式可视化逐步检查并干预聚类过程
- 基于距离矩阵或相似度矩阵进行聚类

## 场景标签

 · 领域:数据挖掘/机器学习

## 证据(README 行号)

> L10: This repository presents the HiPart package, an open-source native python library that provides efficient and inter
> L28: clustered_class = DePDDP(max_clusters_number=6).fit_predict(X)

## 星数曲线

```mermaid
xychart-beta
    title "panagiotisanagnostou/HiPart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-27 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `323a16b923d3` · [字段定义](../../DATASET.md)*
