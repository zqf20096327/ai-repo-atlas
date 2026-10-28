# PolarBean/DeepSlice

⭐ 134 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/PolarBean/DeepSlice) · [官网](https://www.deepslice.com.au) · 组织维护

**深度学习自动对齐小鼠/大鼠脑切片至脑图谱的 Python 库**

DeepSlice 是用深度学习将组织学脑切片自动对齐到 Allen 脑图谱共同坐标框架（小鼠）与 Waxholm 大鼠脑图谱（大鼠，测试版）的 Python 库。无需预处理、适用于任意染色，对明场图像表现最好；当前仅支持冠状切面，可容纳非正交切面并为每张切片生成标注。对齐结果可在 QuickNII 中查看与细化，并集成 QUINT 工作流；另有 DeepSlice Flask 网页版可上传数据获取对齐结果。通过 pip 安装，需要 Python 3.11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 深度学习自动确定脑切片在图谱中的位置并生成逐片标注
- 无需预处理、适用任意染色，支持非正交切面
- 对齐结果可用 QuickNII 查看与细化，集成 QUINT 工作流
- 提供 DeepSlice Flask 网页版上传即用

## 适用场景

- 将小鼠脑组织切片自动配准到 Allen CCF 坐标框架
- 将大鼠脑切片对齐到 Waxholm 图谱（测试版）
- 在 QUINT 工作流中完成脑切片配准与定量

## 场景标签

 · 领域:神经科学/医学图像分析

## 证据(README 行号)

> L6: DeepSlice is a python library which automatically aligns mouse histology with the allen brain atlas common coordinat
> L11: DeepSlice automates the process of identifying exactly where in the brain a section lies, it can accomodate non-ort

## 星数曲线

```mermaid
xychart-beta
    title "PolarBean/DeepSlice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-28 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `19620a2ee993` · [字段定义](../../DATASET.md)*
