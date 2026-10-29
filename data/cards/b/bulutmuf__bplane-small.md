# bulutmuf/bplane-small

⭐ 24 · Python · Apache-2.0 · 推送 2026-07-06 · [GitHub](https://github.com/bulutmuf/bplane-small) · 个人维护

**军事飞机检测与分类模型：11 类，YOLOv11s，1024px**

基于 YOLOv11s 的轻量级计算机视觉模型，针对非受控环境中的军机检测与细粒度机型分类，覆盖 F-16/F-18/F-35/F-15/J-20/EF2000/Rafale/A-10/C-130/C-2 共 10 类及一个兜底 Military Aircraft 类。训练集 11,006 张图像、19,754 个标注实例，验证 mAP@50 为 0.805。提供 PyTorch 与 ONNX 导出格式，通过 bmodels Python 库运行推理（自动下载权重、GPU 优化、时序平滑）。定位为研究与教育用途，由个人开发者在 48 小时内完成训练。

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

- YOLOv11s 架构，1024×1024 原生分辨率，mAP@50 为 0.805
- 11 类细粒度机型分类，含兜底 Military Aircraft 类减少跨类误判
- 导出 PyTorch (.pt) 与 ONNX (.onnx) 两种格式
- 通过 bmodels 库运行：自动下载权重、GPU 自适应、视频/图像推理

## 适用场景

- 对监控式航拍画面做军机检测与机型识别
- 在边缘或云端部署实时飞机检测推理
- 研究非受控视角与小目标场景下的 YOLO 模型表现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: BPlane-Small-v1 is a computer vision framework built on the YOLO architecture, optimized for the detection and clas
> L24: |**Architecture**|Base Framework|YOLOv11s (Small)|

## 星数曲线

```mermaid
xychart-beta
    title "bulutmuf/bplane-small 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0c79e33e6699` · [字段定义](../../DATASET.md)*
