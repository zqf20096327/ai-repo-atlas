# licheng-xu-echo/SPMS

⭐ 13 · Jupyter Notebook · MIT · 推送 2025-11-14 · [GitHub](https://github.com/licheng-xu-echo/SPMS) · 个人维护

**基于球面投影的分子立体结构描述符生成脚本（论文配套）**

论文《A Molecular Stereostructure Descriptor based on Spherical Projection》的配套代码库：提供从 MDL SDF 文件（V2000）生成分子的球面投影立体结构描述符 SPMS 的核心脚本，以关键原子（如手性碳）为坐标原点投影分子 vdW 表面，分辨率由 desc_n/desc_m 控制；附两个 Jupyter Notebook 演示生成流程及在 Denmark 不对称硫醇加成数据集上的机器学习应用。依赖 numpy、ase、rdkit，通过 conda + pip 安装为 spms 包，机器学习演示还需 TensorFlow 1.X 等第三方包。另提供绘制 SPMS 图的网站。

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

- 从 SDF（V2000）文件生成球面投影分子立体结构描述符
- 支持指定关键原子（如手性碳）或以质心为原点
- 提供机器学习应用示例 Notebook（不对称催化数据集）
- 以 Python 包形式安装（pip install .）

## 适用场景

- 为不对称催化机器学习模型构建分子立体结构特征
- 从 SDF 文件批量生成 SPMS 描述符
- 复现论文在 N-acylimines 不对称加成数据集上的应用

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: Description of molecular stereostructure is critical for the machine learning prediction of asymmetric catalysis. We
> L9: This project provides the key script to generate SPMS based on MDL SDF files (.sdf, **V2000** version). In addition,

## 星数曲线

```mermaid
xychart-beta
    title "licheng-xu-echo/SPMS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `491b1c786b90` · [字段定义](../../DATASET.md)*
