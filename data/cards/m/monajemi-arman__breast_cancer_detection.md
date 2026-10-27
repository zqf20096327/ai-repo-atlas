# monajemi-arman/breast_cancer_detection

⭐ 25 · Python · MIT · 推送 2026-07-29 · [GitHub](https://github.com/monajemi-arman/breast_cancer_detection) · 个人维护

**乳腺 X 光片肿块检测：训练、推理与 API 服务工具集**

在 InBreast、CBIS-DDSM、MIAS 公开乳腺 X 光数据集上训练深度学习模型进行可疑肿块检测，支持 Detectron2 的 Faster R-CNN、YOLO 及自定义 UaNet。提供数据集格式转换（COCO/YOLO）、图像滤镜、可视化、COCOEvaluator 评估（mAP），并附带推理 Web 应用与多个 API 服务：目标检测、DICOM 转 JPEG、哈希路由、目录监听、可解释 AI（XAI）热力图与 LLM 聊天 API。需手动安装 CUDA 与 PyTorch，面向科研与本地临床集成场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Faster R-CNN/YOLO/UaNet 多模型训练与预测
- 数据集转换至 COCO/YOLO 格式及 mAP 评估
- DICOM 转 JPEG、哈希路由、目录监听等 API 服务
- XAI 分类模型生成激活热力图

## 适用场景

- 在公开乳腺 X 光数据集上训练肿块检测模型
- 部署本地推理 Web 应用供临床应用调用
- 将检测结果以 API 形式接入更大项目

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Mammography Mass Detection using Artificial Intelligence;
> L6:  Using this project you will be able to train a model on mammography images for suspicious mass detection, deploy a 

## 星数曲线

```mermaid
xychart-beta
    title "monajemi-arman/breast_cancer_detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8f948aa98f94` · [字段定义](../../DATASET.md)*
