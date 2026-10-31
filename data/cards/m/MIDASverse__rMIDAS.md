# MIDASverse/rMIDAS

⭐ 37 · Python · NOASSERTION · 推送 2026-03-13 · [GitHub](https://github.com/MIDASverse/rMIDAS) · 组织维护

**R 缺失数据多重插补包，已弃用并由 rMIDAS2 取代**

基于深度学习的缺失数据多重插补 R 包，提供 convert/train/complete/combine 四步工作流：预处理、训练 MIDAS 插补模型、生成多个完整数据集并按 Rubin 组合规则跑回归。通过 reticulate 接口调用 Python（TensorFlow<2.12），支持 Python 3.6-3.10，可自动或手动配置环境，附 conda 环境文件。注意本包已官方声明弃用，仅保留在 CRAN 供既有用户使用，不再新增功能或修复，官方建议迁移至 PyTorch 后端的 rMIDAS2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- convert/train/complete/combine 四步插补工作流
- 基于 reticulate 调用 Python/TensorFlow 后端
- 支持 data.table/mltools 优化的大数据集处理
- 提供 conda 环境文件与四个 vignette（含迁移指南）

## 适用场景

- 对含缺失值的数据集做多重插补再回归分析
- 在 R 中使用 MIDAS 深度学习插补方法（既有项目维护）
- 按 Rubin 组合规则分析多个完整数据集

## 场景标签

 · 领域:统计/数据处理

## 证据(README 行号)

> L29: **rMIDAS** is an R package for accurate and efficient multiple
> L34: - `train()` constructs and trains a MIDAS imputation model

## 星数曲线

```mermaid
xychart-beta
    title "MIDASverse/rMIDAS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f1e143a8f9f8` · [字段定义](../../DATASET.md)*
