# LAMDA-CL/LAMDA-PILOT

⭐ 608 · Python · MIT · 推送 2026-01-29 · [GitHub](https://github.com/LAMDA-CL/LAMDA-PILOT) · [官网](https://arxiv.org/abs/2309.07117) · 组织维护 · 中文 README

**基于预训练模型的持续学习算法工具箱，复现20+方法**

南京大学 LAMDA 实验室维护的预训练模型持续学习工具箱：实现 L2P、DualPrompt、CODA-Prompt、RanPAC、EASE、TUNA 等 20 余个类增量学习算法，并支持在预训练模型（Timm 库的 ViT 等骨干）语境下评估 FOSTER、MEMO 等经典方法。通过 JSON 配置文件设置模型、增量类别数、骨干网络与记忆预算，运行 main.py 执行实验；内置 CIFAR-100 自动下载，其余 6 个数据集需自行下载并指定路径。论文发表于 SCIS 2025。

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

- 复现 20+ 持续学习/类增量学习算法并附论文链接
- 支持 Timm 库多种预训练骨干（如 ViT-B/16-IN21K）
- JSON 配置驱动实验：初始类数、每阶段增量、样本记忆策略等参数
- 覆盖 CIFAR-100、ImageNet-R、VTAB 等 7 个数据集的基准结果

## 适用场景

- 科研人员复现和对比类增量学习算法
- 在新数据集上评测自研持续学习方法的基线
- 引用工具箱论文开展预训练模型持续学习研究

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: Welcome to PILOT, a pre-trained model-based continual learning toolbox [Paper]. On the one hand, PILOT implements s
> L139:  - **backbone_type**: The backbone network of the incremental model. It can be selected from a variety of pre-trai

## 星数曲线

```mermaid
xychart-beta
    title "LAMDA-CL/LAMDA-PILOT 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 607 --> 610
    line [609, 608, 608]
```

2026-10-18 609 → 2026-10-26 608（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e3f16679df18` · [字段定义](../../DATASET.md)*
