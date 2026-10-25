# yangcaoai/CoDA_NeurIPS2023

⭐ 224 · Jupyter Notebook · MIT · 推送 2026-05-28 · [GitHub](https://github.com/yangcaoai/CoDA_NeurIPS2023) · [官网](https://yangcaoai.github.io/publications/CoDA.html) · 组织维护

**开放词汇 3D 目标检测论文官方代码（NeurIPS2023/TPAMI2025）**

港科大与华为诺亚方舟实验室合作论文 CoDA 及 CoDAv2 的官方实现：通过协同新类框发现与跨模态对齐，在 ScanNet 与 SUN RGB-D 数据集上进行开放词汇 3D 目标检测的训练、评估与推理。基于 PyTorch 1.8.1 与 CUDA 10.1，需编译 pointnet2 层与 Cython 化 gIOU；提供 OV 设定数据集、预训练模型与示例脚本下载运行。面向 3D 视觉方向的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 协同新类框发现与跨模态对齐的开放词汇 3D 检测
- 提供 OV 设定 ScanNet 与 SUN RGB-D 数据集及预训练模型
- 含两阶段训练、评估与示例运行脚本
- CoDAv2（TPAMI2025）代码与模型在独立分支发布

## 适用场景

- 复现论文的开放词汇 3D 目标检测实验
- 在 ScanNet/SUN RGB-D 上评测预训练模型
- 基于代码开展 3D 检测方法的后续研究

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: ## :book: CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection 
> L65: To achieve the OV setting, we re-organize the original ScanNet and SUN RGB-D and adopt annotations of more categori

## 星数曲线

```mermaid
xychart-beta
    title "yangcaoai/CoDA_NeurIPS2023 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 222 --> 225
    line [223, 224]
```

2026-10-18 223 → 2026-10-25 224（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `495fda371398` · [字段定义](../../DATASET.md)*
