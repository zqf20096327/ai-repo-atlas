# zeiss-microscopy/OAD

⭐ 174 · HTML · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/zeiss-microscopy/OAD) · 组织维护

**蔡司 ZEN Blue 显微成像自动化脚本与工具集合**

Carl Zeiss Microscopy 维护的开源工具集，用于在 ZEN Blue 显微成像平台上自动化实验工作流，覆盖采集、图像分析与图像处理。核心组件包括 CZI 图像格式及读写 API（.NET/C++/Python）、基于 IronPython 的 OAD Simple API 脚本、TCP-IP/COM 等外部接口，以及通过在线图像分析实现的自适应采集（Experiment Feedback）。脚本与 ZEN 实验配置免费提供，但不附带任何保证，需配合 ZEN 软件使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python 脚本（OAD Simple API）自动化显微采集与分析工作流
- CZI 格式读写 API：ZeissImgLib(.NET)、libCZI(C++)、pylibCZIrw
- Experiment Feedback 基于在线图像分析的自适应采集
- 与 Fiji、CellProfiler、KNIME、MATLAB 等软件的数据交换

## 适用场景

- 我需要用 Python 脚本自动化 ZEN Blue 显微镜的采集流程
- 我想在采集中根据在线图像分析结果实时调整实验
- 我需要在自研软件中读写 CZI 图像数据

## 场景标签

`工作流自动化` `图像视频处理` · 领域:效率与自动化

## 证据(README 行号)

> L31: - Create **“smart”** experiments with **Experiment Feedback** and modify the acquisition **On-the-fly** based on **
> L12: - **Python Scripting (OAD Simple API) using IronPython**

## 星数曲线

```mermaid
xychart-beta
    title "zeiss-microscopy/OAD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 173 --> 175
    line [174, 174]
```

2026-10-18 174 → 2026-10-26 174（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b2c99d9612ed` · [字段定义](../../DATASET.md)*
