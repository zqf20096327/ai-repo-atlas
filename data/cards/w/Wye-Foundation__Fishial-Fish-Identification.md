# Wye-Foundation/Fishial-Fish-Identification

⭐ 130 · Jupyter Notebook · MIT · 推送 2026-04-09 · [GitHub](https://github.com/Wye-Foundation/Fishial-Fish-Identification) · [官网](https://www.fishial.ai) · 组织维护

**鱼类识别平台官方训练脚本与预训练模型：分割/检测/分类**

Fishial.ai 鱼类识别平台的官方仓库，提供基于 Detectron2 的分割训练脚本（含 Copy-Paste 增强）、YOLO 目标检测脚本，以及交叉熵与 Triplet/Quadruplet 度量损失的分类训练脚本。最新分类模型为 DinoV2 + ViT，覆盖 866 个鱼类物种，公开测试准确率 93.22%。附带浏览器端 3D 嵌入空间查看器（UMAP 投影）与多版本预训练权重（多数提供 TorchScript 导出），可通过 Colab 或本地 Python 环境运行。

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

- 分割/检测/分类三类任务的官方训练与验证脚本
- 最新分类模型 DinoV2 + ViT 覆盖 866 个鱼类物种，公开准确率 93.22%
- 浏览器端 3D 嵌入查看器：866 物种 UMAP 投影与近邻对比
- 多版本预训练权重下载，多数提供 TorchScript 导出

## 适用场景

- 在自己的鱼类图像数据上训练分割、检测或分类模型
- 直接下载预训练权重做鱼类识别或检测
- 浏览 866 个鱼类物种的嵌入空间与相似物种对比

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L11: This repository contains the official training and validation scripts for the **Fishial.ai** fish segmentation, det
> L115: - **Classification**: Cross-entropy and metric-based training scripts plus inference helpers that produce class em

## 星数曲线

```mermaid
xychart-beta
    title "Wye-Foundation/Fishial-Fish-Identification 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 128 --> 131
    line [129, 130, 130]
```

2026-10-18 129 → 2026-10-28 130（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `2e72b8b2029e` · [字段定义](../../DATASET.md)*
