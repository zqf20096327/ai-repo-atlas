# zhangyi-3/IDR

⭐ 130 · Python · MIT · 推送 2026-01-16 · [GitHub](https://github.com/zhangyi-3/IDR) · 组织维护

**CVPR2022 自监督图像去噪方法 IDR 的官方 PyTorch 实现**

CUHK-SenseTime 联合实验室发布的 IDR（Self-Supervised Image Denoising via Iterative Data Refinement, CVPR2022）官方 PyTorch 实现，通过迭代数据精炼实现自监督图像去噪；另包含 N2N 等无监督去噪方法的个人实现。支持 Slurm 训练与 python test.py 测试，覆盖高斯、脉冲、二项等多种噪声类型；同时发布 SenseNoise 数据集 v4（Raw 图、sRGB 图及镜头阴影等元信息），提供预训练模型下载，测试环境为 PyTorch 1.5.0 + bm3d + scipy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IDR 自监督去噪的官方 PyTorch 实现（CVPR2022）
- 附 N2N 等无监督去噪方法的实现
- SenseNoise 数据集 v4：Raw/sRGB 图像与元信息
- 支持多种噪声类型测试与 Slurm 训练，提供预训练模型

## 适用场景

- 复现或研究自监督图像去噪方法
- 在 Kodak/BSDS300/BSD68 等数据集上评估去噪效果
- 获取真实噪声图像数据集训练去噪模型

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # IDR: Self-Supervised Image Denoising via Iterative Data Refinement
> L13: This repository is the official PyTorch implementation of IDR.

## 星数曲线

```mermaid
xychart-beta
    title "zhangyi-3/IDR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-26 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fadd9a251bd3` · [字段定义](../../DATASET.md)*
