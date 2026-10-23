# google-deepmind/recurrentgemma

⭐ 685 · Python · Apache-2.0 · 推送 2026-02-06 · [GitHub](https://github.com/google-deepmind/recurrentgemma) · 组织维护

**Google DeepMind 开放权重的语言模型，基于 Griffin 架构**

Google DeepMind 发布的开放权重语言模型系列 RecurrentGemma，基于 Griffin 架构：用局部注意力与线性递归的混合替代全局注意力，以在长序列生成时获得快速推理。仓库提供模型实现及采样与微调示例；推荐多数用户使用经过优化的 Flax 实现，另提供未优化的 PyTorch 参考实现。模型权重与分词器通过 Kaggle 下载（需接受 Gemma 许可条款），运行 Colab 教程需 Kaggle 账号。代码可在 CPU、GPU 或 TPU 上运行，Flax 实现针对 TPU 优化。

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

- Griffin 架构：局部注意力 + 线性递归替代全局注意力
- 提供优化版 Flax 实现与 PyTorch 参考实现
- 含采样与微调示例脚本及三个 Colab 教程
- 权重与分词器经 Kaggle 分发（2b 等规格）

## 适用场景

- 下载开放权重语言模型进行文本生成
- 在自己的任务上微调模型（如英法翻译示例）
- 研究 Griffin 架构的实现细节

## 场景标签

`微调` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: RecurrentGemma is a family of open-weights Language Models by Google DeepMind, based on the novel Griffin architectu
> L5: This repository contains the model implementation and examples for sampling and fine-tuning. We recommend most users

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/recurrentgemma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 684 --> 687
    line [686, 685]
```

2026-10-18 686 → 2026-10-23 685（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e4bf40a75b88` · [字段定义](../../DATASET.md)*
