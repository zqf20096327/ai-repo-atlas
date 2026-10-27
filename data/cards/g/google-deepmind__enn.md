# google-deepmind/enn

⭐ 324 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/google-deepmind/enn) · 组织维护

**认知神经网络库：训练知道自身不确定性的神经网络**

DeepMind 开源的基于 JAX 与 Haiku 的研究库，提供认知神经网络（ENN）的设计与训练接口。ENN 除输入 x 外还接收由网络控制的认知索引 z，从而在单一网络上产生多输入的联合预测，用于区分输入歧义与训练数据不足两种不确定性。核心接口包括 EpistemicNetwork（Haiku transform + 索引采样器）、LossFn 等；同时实现了论文提出的 epinet 架构，可为任意常规网络附加不确定性估计。已在 Python 3.7 测试，提供 Colab 教程与预训练 ImageNet 示例。

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

- EpistemicNetwork / LossFn 等高层接口，基于 JAX 与 Haiku 实现
- epinet 架构：可为任意常规网络附加不确定性估计
- 提供 Colab 教程与 ImageNet 预训练 epinet 示例
- 贝叶斯神经网络等现有不确定性方法均可表达为 ENN

## 适用场景

- 研究深度学习中不确定性估计的新方法
- 在分类/回归任务中区分输入歧义与数据不足
- 复现 epinet 论文实验并加载预训练模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L27: > The `enn` library provides a lightweight interface for ENNs implemented on top of JAX and Haiku.
> L79: One of the key contributions of our [paper] is the *epinet*: a new ENN architecture that can supplement any convent

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/enn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 323 --> 325
    line [324, 324]
```

2026-10-18 324 → 2026-10-27 324（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `ca5a13dbf893` · [字段定义](../../DATASET.md)*
