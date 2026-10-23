# genicam/harvesters

⭐ 614 · Python · Apache-2.0 · 推送 2026-04-01 · [GitHub](https://github.com/genicam/harvesters) · 组织维护

**通过 GenTL Producer 采集图像的 Python 库（机器视觉）**

面向计算机视觉应用的 Python 图像采集库：通过加载 GenTL Producer 与 GenICam 兼容设备（典型为工业相机）通信，采集图像到缓冲区，并以 NumPy 数组形式交付用于后续图像处理。支持在单个脚本中加载多个 GenTL Producer、操控 GenICam 特性节点。采用 Apache-2.0 许可，通过 PyPI 分发，另有姊妹项目 Harvester GUI 提供图形界面。安装说明与教程在 docs 目录的 INSTALL.rst/TUTORIAL.rst 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 GenTL Producer 进行图像采集
- 单个脚本可加载多个 GenTL Producer 与多种传输层
- GenICam 特性节点操控（宽度/高度/像素格式等）
- 采集数据以 NumPy 数组交付，可直接进入图像处理流程

## 适用场景

- 在 Python 中从 GenICam 兼容工业相机采集图像
- 在同一脚本中组合多种传输层与多台设备
- 配合 Jupyter/Matplotlib 可视化采集结果进行调试

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L21: Harvester is a Python library that aims to make the image acquisition process in your computer vision application b
> L29: * Image acquisition through GenTL Producers
> L171: * *Harvester*: An image acquisition engine.

## 星数曲线

```mermaid
xychart-beta
    title "genicam/harvesters 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 613 --> 616
    line [614, 615, 614]
```

2026-10-18 614 → 2026-10-23 614（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `debffb3d5f07` · [字段定义](../../DATASET.md)*
