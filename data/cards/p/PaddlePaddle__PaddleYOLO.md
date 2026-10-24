# PaddlePaddle/PaddleYOLO

⭐ 667 · Python · GPL-3.0 · 推送 2026-01-14 · [GitHub](https://github.com/PaddlePaddle/PaddleYOLO) · [官网](https://github.com/PaddlePaddle/PaddleYOLO) · 组织维护 · 中文 README

**面向开发者的飞桨 YOLO 系列目标检测模型库**

基于 PaddleDetection 的 YOLO 系列模型实现库，只包含 YOLO 相关代码：支持 YOLOv3/v5/v6/v7/v8/v10、PP-YOLOE+、RT-DETR、RTMDet、YOLOX 等模型的训练、验证、预测与部署；提供脚本化一键运行、ONNX 导出、PaddleSlim 剪裁/量化、多端推理部署方案及 COCO/VOC 预训练权重。代码库协议为 GPL-3.0，要求 Python>=3.7 与 PaddlePaddle>=2.4.2（Windows 需 develop 版），YOLO 训练建议总 batch_size 大于 64。另附 PaddleDetection 套件的特性与模型性能对比介绍。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持十余种 YOLO 系列及 RT-DETR/RTMDet 模型的训练/验证/预测
- 脚本化一键运行训练与部署流程，改两行即可切换模型
- 支持 ONNX 导出、PaddleSlim 剪裁/量化/蒸馏与多端部署
- 提供 COCO/VOC 预训练权重及垂类检测配置（pphuman/ppvehicle/visdrone 等）

## 适用场景

- 在自定义数据集上训练 YOLO 系列目标检测模型
- 获取 COCO 预训练权重并导出部署到多硬件
- 对比各 YOLO 模型在 COCO 上的精度与速度选型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: **PaddleYOLO**是基于PaddleDetection的YOLO系列模型库，**只包含YOLO系列模型的相关代码**，支持`YOLOv3`、`PP-YOLO`、`PP-YOLOv2`、`PP-YOLOE`、**`PP-YO
> L10:  - **PaddleYOLO**代码库**推荐使用paddlepaddle-2.4.2以上的版本**，请参考官网下载对应适合版本，**Windows平台请安装paddle develop版本**；
> L22: git clone https://github.com/PaddlePaddle/PaddleYOLO  # clone

## 星数曲线

```mermaid
xychart-beta
    title "PaddlePaddle/PaddleYOLO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 666 --> 668
    line [667, 667]
```

2026-10-18 667 → 2026-10-24 667（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2f8d802d44fb` · [字段定义](../../DATASET.md)*
