# KupynOrest/s3od

⭐ 51 · Python · MIT · 推送 2026-06-03 · [GitHub](https://github.com/KupynOrest/s3od) · [官网](https://s3odproject.github.io/) · 个人维护

**合成数据训练的显著目标检测/抠图模型，含 14 万张合成数据集**

ICLR 2026 论文官方仓库：提供 140K 张扩散模型生成的合成图像及高质量掩码数据集（含 ImageNet 1000+ 类别，约 35GB Parquet 格式），以及在其上训练并经真实数据微调的显著目标检测模型。支持单步高分辨率背景移除推理，提供 5 个模型变体（通用/DIS/SOD/COD/纯合成）对应不同基准，训练基于 Hydra 与 PyTorch Lightning，数据生成管线依赖 FLUX 扩散模型与 OpenAI API（仅用于生成描述）。MIT 许可，面向计算机视觉研究者与开发者。

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

- 140K 扩散模型合成的图像+掩码数据集，经 HuggingFace datasets 加载
- 5 个模型变体覆盖背景移除、DIS/SOD/COD 任务
- 训练代码基于 Hydra + PyTorch Lightning，支持 1-8 GPU 配置
- 提供本地 Gradio demo 与 eval.py 复现基准结果

## 适用场景

- 对图像做单步高分辨率背景移除
- 研究合成数据到真实的迁移与零样本检测
- 在 DIS/SOD/COD 学术基准上复现评估结果

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L10: **S3OD** is a large-scale fully synthetic dataset for salient object detection and background removal, with 140K hi
> L73: from s3od import BackgroundRemoval

## 星数曲线

```mermaid
xychart-beta
    title "KupynOrest/s3od 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-27 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1f502680bf82` · [字段定义](../../DATASET.md)*
