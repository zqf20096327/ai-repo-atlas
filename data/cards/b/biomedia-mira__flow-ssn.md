# biomedia-mira/flow-ssn

⭐ 19 · Python · 推送 2026-06-09 · [GitHub](https://github.com/biomedia-mira/flow-ssn) · 组织维护

**ICCV 2025 论文官方代码：基于流模型的随机医学图像分割**

Imperial College London 团队发布的 Flow Stochastic Segmentation Networks 官方实现：一类生成式分割模型，含离散时间自回归与连续时间流两种变体，通过学习流的基底分布建模像素级依赖，可估计任意高秩像素协方差。提供 LIDC-IDRI 与 REFUGE-MultiRater 两个医学影像基准的预训练 checkpoint（Google Drive 下载）、复现 notebook、数据集处理脚本与训练启动脚本。以 pip 可编辑模式安装，依赖声明于 setup.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自回归与连续时间流两种模型变体
- 提供预训练 checkpoint（LIDC-IDRI / REFUGE-MultiRater）与复现 notebook
- 支持自有数据训练（bash 启动脚本）
- REFUGE-MultiRater 数据集托管于 Hugging Face

## 适用场景

- 复现论文中两个医学影像基准的分割结果
- 在自己数据上训练流式随机分割模型
- 研究不确定性与多标注者分割建模

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L16: We introduce the Flow Stochastic Segmentation Network (Flow-SSN), a generative segmentation model family featuring 
> L52: |Flow-SSN|NFE|MC|GED $\downarrow$|Diversity $\uparrow$|HM-IoU $\uparrow$|Dice $\uparrow$|

## 星数曲线

```mermaid
xychart-beta
    title "biomedia-mira/flow-ssn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c6d43179c06b` · [字段定义](../../DATASET.md)*
