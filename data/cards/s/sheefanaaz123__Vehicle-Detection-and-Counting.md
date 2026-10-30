# sheefanaaz123/Vehicle-Detection-and-Counting

⭐ 15 · Jupyter Notebook · 推送 2026-06-08 · [GitHub](https://github.com/sheefanaaz123/Vehicle-Detection-and-Counting) · 个人维护

**从交通视频中检测、跟踪并计数车辆的 OpenCV 项目**

基于 Python + OpenCV + NumPy 的经典计算机视觉流水线：读取交通视频，通过帧差分提取运动对象，经灰度化、高斯模糊、阈值化与膨胀后检测轮廓，按最小宽高过滤，计算质心并跟踪其越过预设计数线实现自动计数，实时叠加边界框与计数显示。以 Jupyter Notebook 形式提供（可转换为 Python 脚本运行），附带示例视频。不依赖深度学习模型，无需 GPU；仓库无自动化测试，也未包含许可证文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 帧差分 + 轮廓检测的经典 CV 流水线，无需深度学习模型或 GPU
- 质心跟踪与虚拟计数线交叉实现自动计数
- 实时边界框可视化与计数叠加显示
- 以 Jupyter Notebook 交付，可通过 nbconvert 转为 Python 脚本运行

## 适用场景

- 对交通监控视频做车辆检测与计数
- 交通流量与拥堵分析的入门/原型实现
- 按参数（最小轮廓尺寸、计数线位置）定制自己的交通监测逻辑

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L14: * Motion-based object extraction using frame differencing
> L52: The application follows a classical computer vision pipeline:

## 星数曲线

```mermaid
xychart-beta
    title "sheefanaaz123/Vehicle-Detection-and-Counting 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `15bbd4e885d6` · [字段定义](../../DATASET.md)*
