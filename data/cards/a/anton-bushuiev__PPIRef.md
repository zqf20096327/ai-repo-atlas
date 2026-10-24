# anton-bushuiev/PPIRef

⭐ 110 · Jupyter Notebook · MIT · 推送 2026-09-19 · [GitHub](https://github.com/anton-bushuiev/PPIRef) · [官网](https://ppiref.readthedocs.io) · 组织维护

**蛋白质相互作用三维结构的数据集与Python工具包**

基于 Protein Data Bank (PDB) 全部蛋白质-蛋白质相互作用 (PPI) 构建的 PPIRef 数据集及配套 Python 包。功能包括：从 .pdb 文件提取 PPI 界面、可视化与分析 PPI 性质、比较/去重/聚类界面、按界面结构或序列从 PDB 检索相似 PPI，以及为机器学习应用下载、切分和采样准备好的数据。数据通过 Zenodo 下载，含 6A 与 10A 界面版本及基于 PDB-REDO 的版本。仓库声明仍在开发中。面向机器学习与数据科学研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖 PDB 全部 PPI 的数据集（PPIRef50K 含 51,755 条样本）
- 从 .pdb 文件提取、可视化、比较、去重与聚类 PPI 界面
- 按界面结构或序列从 PDB 检索相似 PPI
- 为机器学习应用提供下载、切分与采样工具

## 适用场景

- 为蛋白质相互作用机器学习模型准备标准化数据集
- 从 PDB 结构中提取并分析蛋白界面
- 对 PPI 数据集去重与聚类以避免数据泄漏

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: PPIRef is a Python package for working with 3D structures of protein-protein interactions (PPIs). It is based on th
> L16: - ⭐ **Downloading, splitting and subsampling** prepared PPIs for machine learning applications.

## 星数曲线

```mermaid
xychart-beta
    title "anton-bushuiev/PPIRef 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-24 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `fd871d3fd5b9` · [字段定义](../../DATASET.md)*
