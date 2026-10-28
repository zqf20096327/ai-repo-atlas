# Teichlab/celltypist

⭐ 515 · Python · MIT · 推送 2026-05-22 · [GitHub](https://github.com/Teichlab/celltypist) · [官网](https://www.celltypist.org/) · 组织维护

**scRNA-seq 数据的细胞类型自动注释工具**

面向单细胞 RNA 测序数据分析者的 Python 工具：基于经随机梯度下降优化的逻辑回归分类器，对输入细胞做细胞类型预测。可下载内置模型（当前聚焦免疫细胞亚群）或使用自定义模型；输入支持 count 表（txt/csv/tsv/mtx 等）与 Scanpy 生成的 AnnData；提供 best match 与概率匹配两种预测模式、多数投票，以及导出 csv/xlsx 表格、AnnData 与 UMAP 可视化的函数。以 pip（PyPI）与 conda（bioconda）方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于逻辑回归分类器（SGD 优化）的细胞类型预测
- 内置模型可下载与更新，支持自定义模型
- 支持 count 表与 AnnData 输入，两种预测模式（best match / prob match）
- 结果可导出为表格、AnnData 与 UMAP 可视化图

## 适用场景

- 对我的 scRNA-seq 数据自动标注细胞类型与亚型
- 跨数据集大规模标签迁移
- 用自定义训练的模型注释自己的数据集

## 场景标签

 · 领域:生物信息学/单细胞测序

## 证据(README 行号)

> L3: CellTypist is an automated cell type annotation tool for scRNA-seq datasets on the basis of logistic regression clas
> L9: Using CellTypist for cell type classification Open In Colab

## 星数曲线

```mermaid
xychart-beta
    title "Teichlab/celltypist 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 513 --> 516
    line [514, 515, 515]
```

2026-10-18 514 → 2026-10-28 515（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `56a58ff67c94` · [字段定义](../../DATASET.md)*
