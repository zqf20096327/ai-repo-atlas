# ArgoHA/D-FINE-seg

⭐ 247 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/ArgoHA/D-FINE-seg) · [官网](https://dfine-seg.argoai.space) · 组织维护

**实时目标检测/关键点/实例与语义分割训练部署框架**

单一代码库通过一个配置项切换四种任务（detect/segment/sem_seg/kpts），提供 N 到 X 五种模型规模，覆盖数据准备、训练（DDP、EMA、AMP、mosaic、知识蒸馏）、导出（ONNX/TensorRT/OpenVINO/CoreML）与多后端推理的端到端流程。支持 COCO/YOLO 标注格式与 RGB+热成像/深度 4 通道输入，附带 C++ 核心 libdfine.so 用于嵌入机器人与 Jetson。以 PyPI 包和源码方式提供，预训练权重从 Hugging Face 自动下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个配置项在检测/实例分割/语义分割/关键点四任务间切换，五种模型规模
- 导出与多后端推理：ONNX、TensorRT、OpenVINO、CoreML，含 INT8 量化
- 支持 RGB+热成像/深度/NIR 的多通道 .npy 输入训练
- C++ 核心 libdfine.so 融合 CUDA 前后处理，面向机器人与 Jetson 部署

## 适用场景

- 训练自有的检测/分割/关键点模型并导出部署
- 在边缘设备（Jetson）上做实时推理
- 用 RGB+热成像双模态数据训练检测模型
- 用 SAM3 自动标注生成训练数据

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L21: D-FINE-seg is a framework for real-time **object detection**, **keypoint estimation**, **instance** and **semantic 
> L53: pip install dfine-seg           # inference + training

## 星数曲线

```mermaid
xychart-beta
    title "ArgoHA/D-FINE-seg 星数(近 16 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-16", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 217 --> 249
    line [220, 219, 220, 221, 222, 223, 224, 219, 224, 225, 226, 227, 242, 245, 247, 247]
```

2026-10-24 220 → 2026-11-26 247（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `62592f28bf34` · [字段定义](../../DATASET.md)*
