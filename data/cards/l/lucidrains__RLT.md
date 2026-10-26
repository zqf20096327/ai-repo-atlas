# lucidrains/RLT

⭐ 61 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/lucidrains/RLT) · 个人维护

**循环环路 Transformer 的 PyTorch 非官方实现，供研究者实验**

实现普林斯顿 Yifan Zhang 提出的 Recurrent Looped Transformer（RLT）的 PyTorch 库，以 pip 包 rlt-pytorch 形式提供。支持变长循环块（recurrent_lengths 指定各块长度且须求和等于序列长度）、编码器与解码器间的权重共享，并可实现 Teoh 等人的 Next-Latent Prediction。附 enwik8 训练测试脚本。属非官方实现，README 未声明硬件要求或部署形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Recurrent Looped Transformer 架构
- 循环块大小可随序列变化（recurrent_lengths 参数）
- 编码器-解码器权重共享
- 支持 Next-Latent Prediction（Teoh et al.）

## 适用场景

- 复现或实验 Recurrent Looped Transformer 架构
- 在自建模型中调用 RLT 模块做序列建模研究
- 在 enwik8 数据上验证架构效果

## 场景标签

 · 领域:深度学习/模型实现

## 证据(README 行号)

> L5: Unofficial implementation of the Recurrent Looped Transformer proposed by Yifan Zhang of Princeton.
> L20: import torch

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/RLT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0c9986906e37` · [字段定义](../../DATASET.md)*
