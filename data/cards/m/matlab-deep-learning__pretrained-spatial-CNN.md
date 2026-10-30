# matlab-deep-learning/pretrained-spatial-CNN

⭐ 25 · MATLAB · NOASSERTION · 推送 2026-02-17 · [GitHub](https://github.com/matlab-deep-learning/pretrained-spatial-CNN) · 组织维护

**MATLAB 预训练 Spatial-CNN 车道线检测模型**

MathWorks 维护的 MATLAB 预训练车道线检测仓库：实现以 VGG-16 为骨干的 Spatial-CNN（SCNN），在 CULane 数据集上训练，对 RGB 图像输出车道概率图与置信度，最多检测 4 条车道，置信度低于 0.5 的车道被忽略。提供单图与视频推理脚本、自定义嵌套深度学习层实现（4 个方向的消息传递层），并附 CULane 上 F-measure 评测结果。运行需 MATLAB R2021a 或更高版本及三个工具箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VGG-16 骨干 SCNN，CULane 数据集预训练
- 提供单图与驾驶场景视频推理脚本
- 最多检测 4 条车道，输出 5 通道概率图（4 车道+背景）
- 消息传递层以自定义嵌套深度学习层实现

## 适用场景

- 对行车图像或视频运行车道线检测推理
- 在自动驾驶视觉管线中集成 SCNN 车道检测
- 学习 SCNN 自定义层在 MATLAB 中的实现方式

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository implements a pretrained Spatial-CNN (SCNN)[1] lane detection model in MATLAB&reg;.
> L12: This repository implements SCNN with VGG-16 as the backbone. The pretrained network is trained to detect lanes in t

## 星数曲线

```mermaid
xychart-beta
    title "matlab-deep-learning/pretrained-spatial-CNN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fec0725bacc9` · [字段定义](../../DATASET.md)*
