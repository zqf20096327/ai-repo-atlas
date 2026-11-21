# BaumSebastian/DDACS

⭐ 11 · Jupyter Notebook · MIT · 推送 2026-09-25 · [GitHub](https://github.com/BaumSebastian/DDACS) · [官网](https://doi.org/10.18419/DARUS-4801) · 个人维护

**面向 ML 研究者的 3.2 万例钣金拉深 FEM 仿真数据集接口**

DDACS 数据集的 Python 访问包：数据集含 32,466 例两工序（拉深+切边）钣金仿真，约 640 GB HDF5，8 个输入参数，预定义训练/验证/测试划分。包内含下载 CLI、基于 Croissant 1.1 manifest 的数据读取模块、可选 PyTorch IterableDataset（支持 DDP 分片、部分下载跳过）与可视化工具。版本与数据集大版本绑定，需通过 DaRUS 获取完整数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 32,466 例仿真、~640 GB 无损 HDF5，预定义 train/val/test 划分
- Croissant 1.1 manifest 作为单一 schema 来源，可被外部 Croissant 工具消费
- 可选 PyTorch IterableDataset，支持 worker 分片与 DDP 安全切分
- 22 MB teaser 数据可在 Kaggle/Hugging Face/Zenodo 获取

## 适用场景

- 训练替代 FEA 求解器的 ML 代理模型（应力/应变/回弹预测）
- 钣金成形工艺的制造与材料研究
- 用可执行 notebook 教程学习数据集用法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: **A large-scale dataset and benchmark for training AI models that replace computationally expensive FEA simulations
> L30: A Croissant-native Python package for accessing the DDACS Dataset ships with this repo: one CLI for the download, o
> L40: - `ddacs.load(data_dir)` parses the manifest and exposes published RecordSets (`process-parameters`, `field-map`, `

## 星数曲线

```mermaid
xychart-beta
    title "BaumSebastian/DDACS 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-20", "2026-11-21"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-02 10 → 2026-11-21 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `dabeed891c53` · [字段定义](../../DATASET.md)*
