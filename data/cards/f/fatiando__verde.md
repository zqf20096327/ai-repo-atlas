# fatiando/verde

⭐ 675 · Python · BSD-3-Clause · 推送 2026-09-29 · [GitHub](https://github.com/fatiando/verde) · [官网](https://www.fatiando.org/verde) · 组织维护

**地球科学空间数据处理与网格化插值的 Python 库**

Fatiando a Terra 项目下的 Python 库，用于处理地形、点云、测深、地球物理测量等空间数据，并在 2D 表面上进行网格化插值。插值方法受机器学习启发，接口设计与 scikit-learn 类似；另提供趋势去除、分块/窗口操作、交叉验证等配套分析方法。支持标量与矢量数据网格化（如风速、GPS 速度），兼容笛卡尔与地理坐标，并与 numpy/pandas/scikit-learn/xarray 集成。项目自称稳定版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 机器学习风格接口的空间数据网格化插值
- 支持标量与矢量数据（风速、GPS 速度等）
- 支持笛卡尔与地理坐标
- 提供趋势去除、分块/窗口操作、交叉验证

## 适用场景

- 对地形、测深等地学测量数据进行网格化插值
- 对重力、磁力等地球物理调查数据做处理与成图前准备
- 去除空间数据趋势并做交叉验证

## 场景标签

 · 领域:地球科学/空间数据处理

## 证据(README 行号)

> L22: **Verde** is a Python library for processing spatial data (topography, point
> L26: Our core interpolation methods are inspired by machine-learning.

## 星数曲线

```mermaid
xychart-beta
    title "fatiando/verde 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 674 --> 676
    line [675, 675]
```

2026-10-18 675 → 2026-10-26 675（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ff731e95f5a5` · [字段定义](../../DATASET.md)*
