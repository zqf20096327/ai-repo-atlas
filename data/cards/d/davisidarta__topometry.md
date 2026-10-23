# davisidarta/topometry

⭐ 109 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/davisidarta/topometry) · [官网](https://topometry.readthedocs.io/en/latest/) · 个人维护

**学习高维数据潜在几何的 Python 工具库，聚焦单细胞分析**

几何感知的 Python 工具包：从邻接图学习 Laplace–Beltrami 类算子，构建谱支架并精炼图，用于聚类与低维可视化布局。提供 AnnData/Scanpy 封装与 scikit-learn 风格 transformer、算子原生度量和 Riemannian 诊断。面向单细胞组学等大型数据集的分析者与科研用户。限制：不支持流式更新与逆变换（嵌入新点需重算算子），小样本场景不适用。

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

- 邻接图→Laplacian/扩散算子→谱支架→聚类与低维布局的管线
- AnnData/Scanpy 封装与 scikit-learn 风格 transformer
- 算子原生几何保持度量与 Riemannian 失真诊断
- 非破坏性流程（不改写 adata.X），输出命名空间化

## 适用场景

- 单细胞 RNA-seq 数据的几何忠实聚类与降维可视化
- 比较不同降维/参数选择下的几何保持效果
- 审计可视化失真或估计内在维度以指导模型设计

## 场景标签

 · 领域:生物信息学/单细胞分析、流形学习

## 证据(README 行号)

> L9: **TopoMetry** is a geometry-aware Python toolkit for exploring high-dimensional data via diffusion/Laplacian operato
> L11: - **AnnData/Scanpy wrappers** for single-cell workflows
> L15: - Designed for **large, diverse datasets** (e.g., single-cell omics)

## 星数曲线

```mermaid
xychart-beta
    title "davisidarta/topometry 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-23 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2f50d2efd068` · [字段定义](../../DATASET.md)*
