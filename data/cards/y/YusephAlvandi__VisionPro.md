# YusephAlvandi/VisionPro

⭐ 15 · Python · 推送 2026-06-22 · [GitHub](https://github.com/YusephAlvandi/VisionPro) · 个人维护

**离线 YOLOv8m 物体检测与人脸计数桌面工具**

基于 Python、OpenCV 与 CustomTkinter 构建的桌面 GUI 工具，使用 YOLOv8m 深度神经网络对图像中的物体与人脸进行检测、标注与计数。提供两种模式：仅人脸（只检测计数人员）与全部物体（检测 80 类）。带置信度滑块控制检测灵敏度，支持批量文件夹处理，完全离线运行。依赖通过 pip 安装，模型文件（48MB）首次运行时自动下载。

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

- YOLOv8m 检测 80 类物体与人脸
- Faces Only / All Objects 两种检测模式
- 置信度滑块与边界框标签可视化
- 批量文件夹处理，离线运行

## 适用场景

- 对图片中的人员或物体进行检测与计数
- 批量处理文件夹中的图像并输出检测结果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This is an AI-powered face detection and object counting (all-in-one) tool. YOLOv8m (a deep neural network trained o
> L9: VisionPro detects, labels, and counts objects and persons in images. Two modes available:

## 星数曲线

```mermaid
xychart-beta
    title "YusephAlvandi/VisionPro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3cc01a59cb21` · [字段定义](../../DATASET.md)*
