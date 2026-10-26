# cgoliver/rnaglib

⭐ 46 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/cgoliver/rnaglib) · [官网](https://rnaglib.org) · 组织维护

**面向 RNA 2.5D/3D 结构的深度学习工具包与注释数据库**

Python 包 rnaglib 用于研究 RNA 2.5D 与 3D 结构：提供带注释的 RNA 结构数据集（含二级结构、3D 坐标、Leontis-Westhof 碱基对分类、蛋白/小分子结合等标注，源自 x3dna-dssr），支持按 PDB ID 获取、从 Zenodo 下载全库、用 fr3d-python fork 注释自有结构。面向七个生物学任务的 ML 基准，基于 Task/Representation/模型三要素训练评估，并提供 2.5D 图可视化与图编辑距离比较。安装步骤见 INSTALL.md。限制：fr3d 注释暂不支持非标准残基。

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

- 7 个生物学任务的 RNA 3D 结构 ML 基准数据集与任务创建工具
- 全库注释结构可经命令行从 Zenodo 下载（最新版含 8441 条 RNA）
- Leontis-Westhof 相互作用提取，3D 结构转 2.5D 图（fr3d-python fork）
- 2.5D 图可视化与图编辑距离比较

## 适用场景

- 在 RNA 结构数据上训练与基准评测深度学习模型
- 按 PDB ID 获取带多层注释的 RNA 结构图数据
- 将自有 3D 结构转换为 2.5D 图并提取碱基对几何分类

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: `RNAglib` is a Python package for studying RNA 2.5D and 3D structures. Functionality includes automated data loading
> L32: We now provide datasets of RNA 3D structures ready-to-use for machine learning model benchmarking in seven

## 星数曲线

```mermaid
xychart-beta
    title "cgoliver/rnaglib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dbc0558f7372` · [字段定义](../../DATASET.md)*
