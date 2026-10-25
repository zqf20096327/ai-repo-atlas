# google-deepmind/tips

⭐ 639 · Jupyter Notebook · Apache-2.0 · 推送 2026-08-31 · [GitHub](https://github.com/google-deepmind/tips) · [官网](https://gdm-tipsv2.github.io/) · 组织维护

**带空间感知的图文预训练视觉编码器模型实现与权重**

DeepMind 发布的 TIPS/TIPSv2 图文预训练模型代码库：提供 PyTorch 与 JAX(Scenic) 两套推理实现及多尺寸(B/14 至 g/14，最大 1.1B 视觉参数)检查点下载，模型在 9 个任务、20 个数据集上验证，覆盖零样本分割、深度与法线估计、图文检索等场景。提供 HuggingFace demo、PyTorch/JAX Colab 及任务专属 notebook。本地安装需 Conda 环境、pip 安装 PyTorch 依赖并克隆源码，检查点经脚本下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 与 JAX(Scenic) 双实现及多尺寸检查点（85.7M–1.1B 视觉参数）
- 零样本分割、深度/法线估计、图文检索等任务 notebook
- HuggingFace demo 与两个推理 Colab
- 9 任务 20 数据集的评测结果表

## 适用场景

- 为 CV/多模态应用选型视觉编码器
- 跑零样本分割或深度法线估计推理
- 复现论文实验或对比视觉编码器基准

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L20: The **TIPS** series of models (**T**ext-**I**mage **P**retraining with **S**patial Awareness) are foundational imag
> L51: - `tips/pytorch/`: PyTorch inference for the model.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/tips 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 638 --> 640
    line [639, 639]
```

2026-10-18 639 → 2026-10-25 639（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `c08d706525da` · [字段定义](../../DATASET.md)*
