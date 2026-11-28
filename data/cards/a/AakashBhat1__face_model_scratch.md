# AakashBhat1/face_model_scratch

⭐ 10 · Python · 推送 2026-04-09 · [GitHub](https://github.com/AakashBhat1/face_model_scratch) · 个人维护

**从零训练人脸嵌入模型的 PyTorch 度量学习核心**

提供人脸嵌入模型训练与推理的核心实现：数据按 VGGFace2 子集风格的 train/val 目录组织，训练管线包含数据增广、CNN 骨干（resnet50/mobilenet_v2）、嵌入投影与度量学习损失（arcface/triplet），默认配置面向 Colab。推理时将人脸图像转为向量，通过余弦相似度与已存嵌入比对，返回最接近身份及 match/no-match 判定。README 明确本阶段不包含大规模基准测试与生产部署，验证仅做轻量的相似度统计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 resnet50（默认）与 mobilenet_v2 两种骨干，嵌入维度 128/512 可选
- 损失函数支持 arcface（默认）与 batch-hard triplet
- 提供 Colab 自动下载数据集、分步训练与从 last.pt 断点续训的脚本
- 推理输出嵌入向量、余弦相似度比对与 match/no-match 判定

## 适用场景

- 在 VGGFace2 风格数据上从零训练人脸嵌入模型
- 为图库比对场景构建人脸验证流程
- 在 Colab 上低成本运行度量学习训练

## 场景标签

`模型训练` `人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L7: Train a model that maps a face image to an embedding vector such that:
> L47: 5. Compute metric-learning loss.
> L54: 3. Compare with stored embeddings using cosine similarity.

## 星数曲线

```mermaid
xychart-beta
    title "AakashBhat1/face_model_scratch 星数(近 2 点)"
    x-axis ["2026-11-14", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-14 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `1a4606e30f2a` · [字段定义](../../DATASET.md)*
