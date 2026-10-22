# DigitalSlideArchive/HistomicsTK

⭐ 491 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/DigitalSlideArchive/HistomicsTK) · [官网](https://digitalslidearchive.github.io/HistomicsTK/) · 组织维护

**病理全切片图像分析的 Python 算法工具包**

面向数字病理学的 Python 库，提供颜色归一化、颜色解卷积、细胞核分割与特征提取等基础图像分析算法；可独立作为 Python 包使用，也可作为 Digital Slide Archive（DSA）平台的插件，通过 HistomicsUI 以容器化模块/流水线形式在 Web 端调用。借助 large_image 库读取多分辨率全切片与显微图像格式，可通过 slicer_cli_web 扩展开发者自有算法并发布到 DSA。由 NIH 资助（U24-CA194362），服务病理学家/生物学家与算法研究者。

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

- 提供颜色归一化/解卷积、细胞核分割、特征提取等基础算法
- 可作为独立 Python 包或 DSA 平台插件两种方式使用
- 基于 large_image 读取全切片与显微图像多分辨率格式
- 通过 slicer_cli_web 可将开发者算法集成进 DSA 并经 HistomicsUI 发布

## 适用场景

- 病理学家对全切片图像做细胞核分割与特征分析
- 算法研究者开发并分发新的病理图像分析算法
- 在 Digital Slide Archive 平台以容器化流水线运行图像分析任务

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L23: `HistomicsTK`_ is a Python package for the analysis of digital pathology images. It can function as a stand-alone l
> L29: - **As a pure Python package**: enables application of image analysis algorithms to data independent of the `Digita

## 星数曲线

```mermaid
xychart-beta
    title "DigitalSlideArchive/HistomicsTK 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 489 --> 492
    line [490, 491]
```

2026-10-18 490 → 2026-10-22 491（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e7ef0383e69e` · [字段定义](../../DATASET.md)*
