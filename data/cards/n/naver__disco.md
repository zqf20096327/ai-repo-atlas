# naver/disco

⭐ 76 · Python · NOASSERTION · 推送 2025-11-27 · [GitHub](https://github.com/naver/disco) · [官网](https://disco.naverlabs.com) · 组织维护

**控制生成模型输出分布以匹配人类偏好的微调工具包**

NAVER 维护的生成模型分布控制工具包：先通过在样本上定义特征（无需可微）并以目标矩表示偏好，构造与原模型 KL 散度最小的能量模型（EBM），再用分布策略梯度（DPG/CDPG）调参逼近该目标分布，支持 f-divergence 全类（前向/反向 KL、JS、总变差）与 Quasi-Rejection Sampling。基于 PyTorch 与 HuggingFace Transformers，可控制因果与 seq2seq 语言模型，提供 JSON/WandB/Neptune 日志。面向做模型对齐与受控生成的开发者与研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以非可微特征+目标矩定义偏好，EBM 表示目标分布并避免灾难性遗忘
- 支持全类 f-divergence（前向/反向 KL、JS、总变差），不限于 RLHF 的反向 KL
- Quasi-Rejection Sampling 进一步提升采样代表性
- 支持条件生成（CDPGTuner），可控制 seq2seq 模型（NMT、摘要等）

## 适用场景

- 让语言模型以指定比例呈现某特征（如某词出现率、代码可编译率）
- 在保留原模型能力的前提下按人类偏好做分布级对齐微调
- 研究不同 f-divergence 下的受控生成

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: The 🕺🏽 **disco** toolkit allows to control language models and other generative systems to match human preferences w
> L17: To generate samples from the target distribution we can tune a model to approximate it. We do this by minimizing th
> L123: Given an EBM target distribution, we now want to train a model to approximate it so that we can use it to generate

## 星数曲线

```mermaid
xychart-beta
    title "naver/disco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-27 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4d2ad70bc8de` · [字段定义](../../DATASET.md)*
