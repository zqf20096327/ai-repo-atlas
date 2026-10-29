# winci-ai/resa

⭐ 27 · Python · Apache-2.0 · 推送 2025-11-23 · [GitHub](https://github.com/winci-ai/resa) · 组织维护

**ICML 2025 论文 ReSA 正反馈自监督学习方法的官方实现**

ICML 2025 论文 ReSA 的官方代码实现：一种正反馈自监督学习框架，利用编码器输出的稳定聚类特性，通过在线自聚簇机制在训练中迭代优化自身目标。提供在 ImageNet 上以多种 epochs/批次规模预训练的 ResNet-50 模型权重与完整 checkpoint 下载，训练使用 torchrun 多卡命令，评估覆盖线性分类、K-NN 分类与半监督低样本分类。面向复现实验或进行下游迁移的计算机视觉研究者。

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

- 正反馈 SSL 框架与在线自聚簇机制
- 提供 5 组 ImageNet 预训练 ResNet-50 权重（100-800 epochs）
- 单卡/多卡 torchrun 预训练命令与线性/K-NN/半监督评估脚本

## 适用场景

- 复现 ReSA 自监督预训练实验
- 下载预训练 ResNet-50 用于下游分类任务
- 在低标注比例下做半监督评估

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: ReSA: positive-feedback self-supervised learning
> L6: ReSA is designed within our positive-feedback SSL framework, which directly leverages the stable and semantically me
> L13: You can choose to download only the weights of the pretrained encoder used for downstream tasks, or the full checkp

## 星数曲线

```mermaid
xychart-beta
    title "winci-ai/resa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d2018d2408a3` · [字段定义](../../DATASET.md)*
