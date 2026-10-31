# Cecoming/COPE

⭐ 15 · Python · 推送 2026-06-03 · [GitHub](https://github.com/Cecoming/COPE) · 组织维护

**遮挡行人重识别研究代码：CVPR 2026 论文官方复现**

CVPR 2026 论文 COPE 的官方 PyTorch 仓库，针对遮挡行人重识别（Occluded Person Re-ID）提供训练与推理入口、数据集准备说明、人工解析标签（来自 BPREID）与训练权重。在 Occluded-Duke 上报告 82.4% Rank-1 与 76.4% mAP；另提供可迁移到其他 Re-ID 方法的后处理模块 PSS 与免训练的 NPSS。面向计算机视觉研究人员，通过 conda 环境与配置文件复现实验。

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

- 在 4 个遮挡与 2 个整体 Re-ID 数据集上的训练与推理代码
- 提供 stride 16 的已训练权重以支持复现
- PSS 后处理可导出 gallery prompt scores 复用于其他 Re-ID 方法
- NPSS 为免训练即插即用后处理，无需人工解析标签

## 适用场景

- 复现论文在遮挡 Re-ID 基准上的结果
- 将 PSS/NPSS 后处理迁移到自己的 Re-ID 流水线
- 下载训练权重对其他方法做对比评测

## 场景标签

 · 领域:计算机视觉/行人重识别

## 证据(README 行号)

> L5: Welcome to the official repository of our CVPR 2026 paper, "_COPE: Consistent Occlusion and Prompt Enhancement Netwo
> L7: COPE is designed for **occluded person re-identification** and delivers strong performance on both occluded and holi
> L14:  🏆 In particular, it achieves **82.4% Rank-1 accuracy** and **76.4% mAP** on the challenging **Occluded-Duke** benc

## 星数曲线

```mermaid
xychart-beta
    title "Cecoming/COPE 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `17febb97289c` · [字段定义](../../DATASET.md)*
