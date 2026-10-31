# confidence-duku/bakaano-hydro

⭐ 15 · Python · Apache-2.0 · 推送 2026-08-28 · [GitHub](https://github.com/confidence-duku/bakaano-hydro) · 个人维护

**分布式水文引导神经网络模型：面向缺资料流域的径流预测**

将基于物理的格网产流（VegET 方法）与河流网络汇流（MFD/D8/D-infinity）同时间卷积网络（TCN）耦合，生成保持空间显式性的流域径流预测，面向水文专家、气候风险研究者与洪水预报团队。设计目标为缺资料/无资料流域。基于 TensorFlow，需 Python 3.10+，支持 CPU/GPU（GPU 需 Linux、NVIDIA 硬件与驱动，pip 安装 pinned CUDA 12 运行库）。数据需研究区 shapefile、GRDC/CSV 实测流量与 Google Earth Engine 注册。提供 Colab 笔记本与 EGUsphere 预印本引文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VegET 产流 + 河网汇流 + TCN 三组件耦合，输出空间显式径流
- 面向无资料/稀疏观测流域，静态流域描述符条件化以跨流域泛化
- 支持 ERA5/CHIRPS/CHELSA 气象输入与 GEE 检索（NDVI、AlphaEarth 嵌入等）
- 提供场景模拟与洪水制图扩展模块及 Colab 笔记本

## 适用场景

- 缺资料流域的流域尺度径流模拟与预测
- 洪水预报与洪水制图工作流
- 气候变化情景下的水文响应分析

## 场景标签

 · 领域:水文学/机器学习

## 证据(README 行号)

> L7: Bakaano-Hydro is a distributed hydrology-guided neural network model for streamflow prediction. It combines physical
> L99: A Temporal Convolutional Network (TCN), conditioned on static catchment descriptors, learns hydrological dynamics f

## 星数曲线

```mermaid
xychart-beta
    title "confidence-duku/bakaano-hydro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d6c6f521f6c2` · [字段定义](../../DATASET.md)*
