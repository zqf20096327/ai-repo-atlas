# cvlab-kaist/GARD

⭐ 54 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/cvlab-kaist/GARD) · [官网](https://cvlab-kaist.github.io/GARD/) · 组织维护

**多视图 3D 重建的特征空间扩散去噪方法（NeurIPS 2026）**

KAIST AI 与 Samsung Electronics 合作的论文官方实现：GARD 在前馈 3D 重建模型（Depth Anything 3）的特征空间中执行基于扩散的多视图复原，从含运动模糊、噪声等退化的多视图输入中同时恢复场景几何与高质量图像。仓库提供去噪器实现与预训练权重（合计约 7.6G）、Hypersim+TartanAir 训练代码、DA3-BENCH 与 DeblurNeRF 评测代码，训练需自配 GPU 数量与 CUDA 设备。

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

- 在 Depth Anything 3 特征空间做扩散去噪，单次复原同时输出几何与图像
- 提供预训练 checkpoint（denoiser 5.6G + RGB decoder 2.0G）
- Hypersim + TartanAir 合成退化训练配方
- DA3-BENCH 与 DeblurNeRF 真实运动模糊场景评测脚本

## 适用场景

- 在运动模糊/噪声等退化条件下做多视图 3D 重建
- 复现论文在 DA3-BENCH 与真实模糊数据上的评测结果
- 基于合成退化数据训练或微调去噪器

## 场景标签

`模型训练` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L32: Feed-forward multi-view 3D reconstruction models perform well under clean, ideal imaging conditions, but degrade sh
> L34: This repository provides:

## 星数曲线

```mermaid
xychart-beta
    title "cvlab-kaist/GARD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-24 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ded09295c3b2` · [字段定义](../../DATASET.md)*
