# mnpinto/banet

⭐ 44 · Jupyter Notebook · Apache-2.0 · 推送 2026-05-05 · [GitHub](https://github.com/mnpinto/banet) · [官网](https://mnpinto.github.io/banet/) · 个人维护

**深度学习模型：用卫星时序影像制图并定日期火烧迹地**

BA-Net 是基于多光谱卫星影像日序列的深度学习模型，用于火烧迹地的制图与起火日期估计。以 VIIRS 750m 波段重采样到 0.01° 网格为输入，支持近实时运行，通过 active fires 数据触发更新。提供 Python 包（PyPI 可装）与源码安装两种方式，需安装 libhdf4、proj、geos 等系统依赖，并需配置 ladsweb 数据下载环境。配套论文发表于学术期刊。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 VIIRS 多光谱日序列影像的火烧迹地制图与定日期
- 支持近实时（near-real-time）运行模式
- 提供 PyPI 安装与源码 make 安装两种途径
- 配套同行评审论文（pinto2020banet）

## 适用场景

- 近实时监测区域火烧迹地并估计燃烧日期
- 基于 VIIRS 影像生成火烧范围制图
- 科研中复现或扩展火烧迹地深度学习方法

## 场景标签

 · 领域:遥感/野火监测

## 证据(README 行号)

> L1: # BA-Net: A deep learning approach for mapping and dating burned areas using temporal sequences of satellite images
> L2: > Over the past decades, methods for burned areas mapping and dating from remote sensing imagery have been the objec

## 星数曲线

```mermaid
xychart-beta
    title "mnpinto/banet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d83df8cf6913` · [字段定义](../../DATASET.md)*
