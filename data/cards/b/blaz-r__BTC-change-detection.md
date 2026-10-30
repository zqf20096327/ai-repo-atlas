# blaz-r/BTC-change-detection

⭐ 42 · Python · MIT · 推送 2025-12-01 · [GitHub](https://github.com/blaz-r/BTC-change-detection) · 组织维护

**遥感变化检测模型库：系统分析设计选择并训练检测双时相影像变化**

卢布尔雅那大学团队随 IEEE TGRS 2025 论文发布的遥感变化检测代码库：系统研究预训练策略、数据增强、损失函数与学习率调度等设计选择对深度学习变化检测的影响，并在此基础上提出 BTC 基线模型（encoder→diff→decoder 流水线）。支持 6 个数据集（oscd96/levir/sysu/egybcd/clcd/gvlm），数据默认从 HuggingFace 自动下载，也支持自定义目录与 HDF5 格式；训练、评估、推理性能基准与 Slurm 作业脚本均包含。面向遥感与深度学习研究者，需从源码以 conda 环境运行。

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

- 系统分析预训练/增强/损失/调度器对变化检测的影响
- BTC-T/BTC-B 模型权重发布于 HuggingFace 与 Google Drive
- 支持 6 个变化检测数据集及自定义目录/HDF5 格式
- 包含推理速度与效率基准代码及 Slurm 作业脚本

## 适用场景

- 在遥感双时相影像上做变化检测的训练与评估
- 复现论文中的设计选择分析与基准结果
- 对比变化检测方法或作为进一步研究的基线

## 场景标签

`模型训练` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L19: The work systematically investigates the impact of fundamental design choices in deep learning-based change
> L21: Building on these insights, we introduce BTC, a simple yet strong baseline that leverages these core components
> L45: python train.py --config configs/exp/BTC-B.yaml

## 星数曲线

```mermaid
xychart-beta
    title "blaz-r/BTC-change-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d264b4f26564` · [字段定义](../../DATASET.md)*
