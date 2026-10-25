# Haden-Min/CNN_YOLO_AI_accelerator

⭐ 45 · Verilog · 推送 2026-10-08 · [GitHub](https://github.com/Haden-Min/CNN_YOLO_AI_accelerator) · 个人维护

**面向 PYNQ-Z2 的 YOLOv3-Tiny INT8 卷积硬件加速器 RTL 设计**

使用 Verilog 编写的自定义 CNN 加速器 RTL 项目，目标是在 PYNQ-Z2 的可编程逻辑上运行 YOLOv3-Tiny 卷积层数据通路。分工：离线工具解析 Darknet 权重并折叠 BatchNorm、量化为 INT8；PS 侧管理 DDR 缓冲与 YOLO 解码/NMS；PL 侧执行 INT8 卷积、累加、激活与池化。当前里程碑为单个已验证的卷积层（28x28 tile 路径，100MHz 布线通过），非完整 YOLO 推理；物理板级验证为剩余步骤。面向硬件/FPGA 开发者与科研场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- INT8 卷积 tile 数据通路（IC=1 兼容与 IC=3 串行累加仿真通过）
- Tcl 脚本自动生成 Vivado 2024.1 工程并打包 PYNQ Jupyter 测试件
- 28x28 tile 默认路径与 16x16 低延迟备选路径均有文档
- Python golden 输出比对验证硬件结果

## 适用场景

- 在 PYNQ-Z2 上部署与验证自定义 CNN 卷积加速硬件
- 学习 FPGA 上 INT8 量化推理数据通路的设计流程
- 作为 YOLO 硬件加速器课程/科研项目的参考实现

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: A clean restart of a custom RTL accelerator for YOLOv3-Tiny CNN layers on the
> L13: maps through memory, and the PL side performs the expensive CNN datapath work in
> L25: |PL accelerator|Run INT8 convolution, accumulation, activation, padding, and pooling|

## 星数曲线

```mermaid
xychart-beta
    title "Haden-Min/CNN_YOLO_AI_accelerator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d49de2ab4c51` · [字段定义](../../DATASET.md)*
