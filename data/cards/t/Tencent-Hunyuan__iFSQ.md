# Tencent-Hunyuan/iFSQ

⭐ 107 · Python · NOASSERTION · 推送 2026-01-27 · [GitHub](https://github.com/Tencent-Hunyuan/iFSQ) · 组织维护 · 中文 README

**改进图像生成量化器 FSQ 的官方 PyTorch 实现**

腾讯混元团队发布的 iFSQ 论文官方实现：将 FSQ 中的 tanh 激活替换为分布匹配激活 y=2σ(1.6x)-1，使无界高斯潜变量映射到有界均匀分布，以一行代码改动缓解信息效率与重建保真的冲突。仓库同时提供 LlamaGen-REPA（将 Representation Alignment 用于自回归图像生成）与 DiT-REPA 的训练/评测代码，并基于 iFSQ 统一量化器对比 AR 与扩散模型。面向图像生成研究者，提供 conda 环境搭建与多卡 torchrun/accelerate 训练脚本，主体以 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码改动：以分布匹配激活替换 FSQ 的 tanh
- LlamaGen-REPA 将 Representation Alignment 适配到自回归生成模型
- 支持多码本量化（每 token 多索引）
- 以 iFSQ 为统一量化器对比 AR 与扩散模型（50k 图像 FID 评测）

## 适用场景

- 训练图像 tokenizer 并验证 iFSQ 的重建效果
- 复现论文中 AR 与扩散模型的基准对比
- 在 LlamaGen 或 DiT 上应用 REPA 表征对齐训练

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L11: The key insight is replacing the $$y = \tanh(x)$$ function in the original FSQ with a distribution-matching activat
> L16: * ⚡️ **Benchmarking:** We use iFSQ as a unified tokenizer to benchmark AR against diffusion models.
> L20: * 🛸 **Extension:** We introduce **LlamaGen-REPA**, adapting Representation Alignment to AR models to enhance semant

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/iFSQ 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-27 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `dc98fbfba765` · [字段定义](../../DATASET.md)*
