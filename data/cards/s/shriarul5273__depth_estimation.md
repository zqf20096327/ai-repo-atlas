# shriarul5273/depth_estimation

⭐ 11 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/shriarul5273/depth_estimation) · [官网](https://pypi.org/project/depth-estimation/) · 个人维护

**单目深度估计统一 Python 库：14 模型族一个 API**

面向计算机视觉研究者与开发者的单目深度估计库，统一 14 个模型族 36 个变体的 API：单行推理、视频/网络摄像头逐帧深度、可视化（深度图/对比/3D 动画）、标准基准评测、自定义数据微调、剪枝、量化与 ONNX 导出。pipeline() 一行出深度图，模型以单文件自注册方式接入。Python 3.10–3.12、PyTorch 2.6+；zoedepth 与 marigold-dc 不可导出 ONNX，量化准确率因模型而异。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 模型族 36 变体统一 API，换模型只改一个字符串
- 覆盖推理/视频/评测/微调/剪枝/量化/ONNX 导出全流程
- 提供 predict/export 等 CLI 命令
- 模型单文件自注册设计，新增模型自动被 AutoDepthModel 解析

## 适用场景

- 从单张图像或视频流生成深度图
- 在 NYU Depth V2、KITTI 等基准上对比评测多个深度模型
- 用自定义深度数据微调 Depth Anything 等可训练模型
- 导出 ONNX 并量化后部署到非 PyTorch 环境

## 场景标签

`模型评测` `图像视频处理` `微调` `模型量化` · 领域:评测与运维

## 证据(README 行号)

> L14: `depth_estimation` is a unified model framework for monocular depth estimation. It provides one consistent API acro
> L16: It covers the workflow end-to-end: run inference with one line, process video, visualize results, evaluate standard

## 星数曲线

```mermaid
xychart-beta
    title "shriarul5273/depth_estimation 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 9 --> 12
    line [10, 11]
```

2026-11-26 10 → 2026-11-27 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9c36fb2f439b` · [字段定义](../../DATASET.md)*
