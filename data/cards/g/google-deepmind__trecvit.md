# google-deepmind/trecvit

⭐ 34 · Python · Apache-2.0 · 推送 2026-01-10 · [GitHub](https://github.com/google-deepmind/trecvit) · 组织维护

**高效视频建模的循环 Transformer 架构：LRU 时序混合+空间自注意力**

Google DeepMind 发布的视频模型架构 TRecViT：用门控线性循环单元（LRU）在时间维度混合信息，自注意力处理空间维度，MLP 处理通道维度，以较少参数与较小内存/FLOPs 在 SSv2 和 Kinetics400 上做视频分类。支持监督与自监督（掩码自编码）训练，依赖 recurrent_gemma 库并复用 big_vision 的分支文件，提供 Kinetics400 与 MAE 预训练检查点和 Colab 快速上手笔记本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LRU 时序混合 + 空间自注意力 + 通道 MLP 的三路分解架构
- 支持监督与自监督（掩码自编码）训练
- 发布 TRecViT-B 在 Kinetics400（监督分类）与 MAE 的预训练检查点
- 提供 quickstart Colab notebook 用于实例化模型与推理

## 适用场景

- 在 SSv2/Kinetics400 等视频基准上做视频识别研究
- 以较小参数量训练因果视频模型
- 复现论文或基于预训练检查点做视频下游任务实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: TRecViT proposes a new factorisation that relies on gated linear recurrent
> L7: and MLPs for mixing over channels. This architecture achieves SOTA results on SSv2 when compared to causal models an
> L42: We release pretrained checkpoints for supervised classification using TRecViT-B on Kinetics400:

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/trecvit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-30 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `346d4d893bcc` · [字段定义](../../DATASET.md)*
