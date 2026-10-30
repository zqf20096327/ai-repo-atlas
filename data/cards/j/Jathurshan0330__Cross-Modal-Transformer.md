# Jathurshan0330/Cross-Modal-Transformer

⭐ 77 · Jupyter Notebook · 推送 2026-02-12 · [GitHub](https://github.com/Jathurshan0330/Cross-Modal-Transformer) · 组织维护

**科研用：跨模态 Transformer 睡眠分期分类与可解释性实现**

论文官方代码库，实现 Epoch 与 Sequence 两种跨模态 Transformer 模型，用于睡眠阶段自动分类；由跨模态 Transformer 编码器与多尺度一维 CNN 组成，利用注意力模块提供可解释性输出（解释图表）。提供数据准备、训练、评估与推理解释的 Python 脚本，基于 PyTorch 与 CUDA 运行，数据集生成与推理通过 Colab 说明。面向复现论文或开展睡眠分期研究的科研人员。

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

- 实现 Epoch 与 Sequence 两种跨模态 Transformer 模型
- 利用注意力模块生成解释图表，输出保存至 interpretations 目录
- 提供数据准备、训练、评估、推理解释完整脚本

## 适用场景

- 复现论文的睡眠分期实验与结果
- 在 SleepEDF 数据上训练并评估睡眠阶段分类模型
- 查看注意力机制给出的分期解释图表

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: Accurate sleep stage classification is significant for sleep health assessment. In recent years, several deep learn
> L22: Run our algorithm using Pytorch and CUDA https://pytorch.org/

## 星数曲线

```mermaid
xychart-beta
    title "Jathurshan0330/Cross-Modal-Transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-30 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `58ff988ae919` · [字段定义](../../DATASET.md)*
