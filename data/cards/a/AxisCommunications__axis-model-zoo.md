# AxisCommunications/axis-model-zoo

⭐ 38 · C · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/AxisCommunications/axis-model-zoo) · 组织维护

**Axis 网络摄像机可用的机器学习模型集合及性能基准**

由 Axis Communications 维护的模型清单仓库：收录与 Axis 摄像机兼容的图像分类与目标检测模型，按硬件平台（ARTPEC-7/8/9、CV25、CV75）列出推理速度与精度指标，随每次 AXIS OS 版本更新速度数据。模型多为公开现成模型，链接模型文件并在公开处附 ckpt 供继续训练；附带 larod 测试框架与 model_performance_tester.py 脚本，可经 SSH 连接摄像机测量自有模型速度。README 声明这些模型仅供对比与演示，非生产级质量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按摄像机平台列出的速度/精度基准表，随 AXIS OS 版本更新
- 公开模型附 ckpt 文件链接可继续训练
- model_performance_tester.py 经 SSH 与 larod-client 测量自有模型推理速度
- 覆盖图像分类（MobileNet/EfficientNet）与目标检测（SSD/YOLOv5/YOLOv8）

## 适用场景

- 为我的 Axis 摄像机选择可运行的视觉模型
- 比较不同硬件平台上模型的推理速度与精度
- 用提供的脚本测试自有模型在摄像机上的性能

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: Axis network cameras can be used for computer vision applications and can run machine learning models to make infere
> L68: This repository aims to showcase two key performance indicators: inference speed and accuracy. In

## 星数曲线

```mermaid
xychart-beta
    title "AxisCommunications/axis-model-zoo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c40e25b151aa` · [字段定义](../../DATASET.md)*
