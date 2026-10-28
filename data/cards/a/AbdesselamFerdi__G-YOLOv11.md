# AbdesselamFerdi/G-YOLOv11

⭐ 20 · Python · GPL-3.0 · 推送 2026-04-29 · [GitHub](https://github.com/AbdesselamFerdi/G-YOLOv11) · [官网](https://www.sciencedirect.com/science/article/abs/pii/S1746809425013722) · 个人维护

**轻量级骨折检测模型：儿童腕部 X 光片定位创伤**

基于 YOLOv11 并引入 ghost 卷积的轻量级计算机辅助诊断检测器，用于儿童腕部 X 光图像中的骨折定位。ghost 卷积以更少线性运算生成同等数量特征图，降低计算资源需求；在 GRAZPEDWRI-DX 数据集上评估，mAP@0.5 为 0.535，参数量 7.794M，推理时间 2.4 ms（NVIDIA A10 GPU）。代码基于 ultralytics 与 YOLOv9-Fracture-Detection 构建，配有关联论文（ScienceDirect）。README 未给出安装与运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ghost 卷积降低检测器计算资源需求
- GRAZPEDWRI-DX 上 mAP@0.5 0.535、推理 2.4 ms（A10 GPU）
- 参数量 7.794M，较 YOLOv11l 尺寸减少 68.7%
- 基于 ultralytics 与 YOLOv9-Fracture-Detection 构建

## 适用场景

- 儿童腕部 X 光片的骨折定位辅助诊断
- 资源受限临床环境下运行轻量检测模型
- 医学影像检测模型的效率基准参考

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L14: Computer-aided diagnosis (CAD) systems have greatly improved the interpretation of medical images by radiologists a
> L30: The code is built with ultralytics and YOLOv9-Fracture-Detection.

## 星数曲线

```mermaid
xychart-beta
    title "AbdesselamFerdi/G-YOLOv11 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `053e9dff3ba9` · [字段定义](../../DATASET.md)*
