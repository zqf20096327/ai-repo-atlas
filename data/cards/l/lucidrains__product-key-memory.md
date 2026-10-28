# lucidrains/product-key-memory

⭐ — · [GitHub]() · 个人维护

**PyTorch 实现的 Product Key Memory 模块，用于增强 Transformer**

以 PyTorch 独立模块形式实现 Product Key Memory（产品键记忆层），用于替换 Transformer 中的前馈层以扩充模型记忆容量。提供 PKM 类直接嵌入模型、为 PKM 值参数设置不同学习率的辅助函数，以及自动生成优化器参数配置的 fetch_optimizer_parameters。已实现退火 Gumbel 噪声随机化与多头式值维度缩减组合，待办项含乘性打分与坐标下降路由。README 引用 Lample 2019 等多篇相关论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PKM 模块可直接替换 Transformer 前馈层
- 提供值参数差分学习率的辅助函数与自动优化器参数配置
- 支持退火 Gumbel 噪声随机化与多头式值维度组合

## 适用场景

- 为 Transformer 模型加入大容量稀疏记忆层
- 研究中对 PKM 值参数单独调节学习率
- 复现基于产品键记忆的论文实验

## 场景标签

 · 领域:深度学习/模型组件

## 证据(README 行号)

> L7: Standalone Product Key Memory module for augmenting Transformer models
> L17: Replace the feedforwards in a Transformer with the following

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/product-key-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-28 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f3af87afe0af` · [字段定义](../../DATASET.md)*
