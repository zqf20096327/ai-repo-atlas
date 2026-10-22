# Project-MONAI/MONAILabel

⭐ 906 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Project-MONAI/MONAILabel) · [官网](https://monai.readthedocs.io/projects/label/en/latest/) · 组织维护

**给放射/病理/内镜标注者的医学影像 AI 标注与主动学习工具**

服务器-客户端架构的开源医学影像标注系统：通过 MONAI Label Server 以 serverless 方式部署标注应用，内置分割、DeepGrow、DeepEdit、SAM2 等模型，在标注过程中持续从用户交互中学习。开发者可编写自定义标注应用，最终用户（临床医生、标注员）通过 3D Slicer、OHIF、QuPath、CVAT 等查看器交互标注。支持本地数据集与 DICOMWeb 连接，可运行于单机单卡或多卡 GPU 环境。以 pip、Docker 或源码方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标注应用以 serverless 方式通过 MONAI Label Server 暴露为服务
- 支持 Radiology/Pathology/Video/Bundle 四类应用，含 DeepGrow、DeepEdit、SAM2 等模型
- 集成 3D Slicer、MITK、OHIF、QuPath、Digital Slide Archive、CVAT 等查看器
- DICOMWeb 连接与本地数据集两种数据准备方式

## 适用场景

- 临床医生在 3D Slicer 中交互式完成器官与肿瘤分割标注
- 病理研究者用 QuPath 做细胞核分割与分类标注
- 结合 CVAT 实现内镜视频的全自动主动学习训练流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: MONAI Label is an intelligent open source image labeling and learning tool that enables users to create annotated d
> L29: - Framework for developing and deploying MONAI Label Apps to train and infer AI models

## 星数曲线

```mermaid
xychart-beta
    title "Project-MONAI/MONAILabel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 903 --> 906
    line [904, 905, 905]
```

2026-10-18 904 → 2026-10-22 905（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `448903a7db79` · [字段定义](../../DATASET.md)*
