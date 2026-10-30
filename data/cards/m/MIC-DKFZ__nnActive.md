# MIC-DKFZ/nnActive

⭐ 24 · Python · Apache-2.0 · 推送 2026-03-12 · [GitHub](https://github.com/MIC-DKFZ/nnActive) · 组织维护

**3D 生物医学分割主动学习评测框架与基准**

面向 3D 生物医学影像主动学习研究的开源框架：扩展 nnU-Net 支持部分标注训练与 3D patch 级查询选择，在四个数据集上系统评测 8 种查询策略（含 Foreground Aware Random 基线与 ClaSP PE 策略），并提出前景效率标注成本指标。提供 CLI 完成数据准备（nnU-Netv2 格式）、实验运行、结果分析与可视化；通过 register_strategy/register 机制注册新查询方法与实验配置；基准结果托管于 Hugging Face。要求 PyTorch 2.4.0 + CUDA 12.4，推荐 swap ≥128GB。附两篇 TMLR 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩展 nnU-Net 支持部分标注训练与 3D patch 级查询选择
- 8 种查询策略 × 4 数据集 × 3 种标注体制的大规模评测
- Foreground Aware Random 基线与前景效率指标
- register_strategy/register 扩展机制注册新查询方法与实验配置

## 适用场景

- 跑主动学习基准复现论文结果（benchmark 分支）
- 评测自研主动学习查询策略与随机基线的对比
- 分析标注预算与查询策略对分割性能的影响

## 场景标签

`模型评测` `目标检测` · 领域:评测与运维

## 证据(README 行号)

> L1: ### :scroll: A Framework for Evaluation of Active Learning in 3D Biomedical Segmentation
> L34: > Semantic segmentation is crucial for various biomedical applications, yet its reliance on large annotated dataset
> L45: - **nnActive**

## 星数曲线

```mermaid
xychart-beta
    title "MIC-DKFZ/nnActive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `eab2c5d30e02` · [字段定义](../../DATASET.md)*
