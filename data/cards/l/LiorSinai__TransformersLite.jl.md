# LiorSinai/TransformersLite.jl

⭐ 43 · Julia · 推送 2026-10-29 · [GitHub](https://github.com/LiorSinai/TransformersLite.jl) · 个人维护

**Jula 语言的轻量 Transformer 层与模型教学库**

面向学习场景的 Julia Transformer 基础包，基于 Flux 实现 Attention is all you need 论文中的多头注意力与正弦位置编码，提供 Indexer、MultiHeadAttention、TransformerBlock 等层，以及 TransformerClassifier 和 TransformerGenerator 两个现成模型，可搭配 Flux.Chain 使用并支持 CUDA/cuDNN GPU 运行。配套博客文章与独立示例仓库；未在 Julia 注册表中注册，需 clone 后以 pkg dev 方式安装；作者声明功能远少于 Transformers.jl。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Attention is all you need 的多头注意力与正弦位置编码层
- 提供 TransformerClassifier / TransformerGenerator 现成模型
- 基于 Flux，可加入 Flux.Chain 并支持 CUDA/cuDNN GPU 运行
- 配套博客文章与独立示例仓库（TransformersLite-Examples）

## 适用场景

- 在 Julia 中从零学习 Transformer 架构实现
- 用少量代码搭建小型文本分类或自回归生成模型
- 阅读可修改的源码对照原论文理解注意力机制

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L10: This package is designed to work with Flux. It implements multi-head attention as described in the paper Attention 
> L12: It comes with the following layers:

## 星数曲线

```mermaid
xychart-beta
    title "LiorSinai/TransformersLite.jl 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-28 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `84868bc0bcb6` · [字段定义](../../DATASET.md)*
