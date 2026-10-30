# dubzdubz/microgpt-ts

⭐ 42 · TypeScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/dubzdubz/microgpt-ts) · [官网](https://microgpt-ts.vercel.app/) · 个人维护

**零依赖 TypeScript 从零实现的字符级 GPT（教学向）**

Karpathy microgpt 的 TypeScript 移植：~500 行零运行时依赖实现完整 GPT——自研 autograd 引擎（Value 类链式法则反向传播）、GPT 架构（嵌入、多头注意力、MLP、残差、RMSNorm）与 Adam 优化器，支持训练与推理。提供 CLI demo 与浏览器端实时训练的 Web playground（可自定义数据与架构参数）。按 bigram→MLP→autograd→注意力→完整 GPT 的分步 PR 组织，面向学习 GPT 内部原理的开发者。

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

- 零运行时依赖的 autograd 引擎（前向+反向）
- 完整 GPT 架构：多头注意力、RMSNorm、残差、Adam 优化器
- 浏览器端客户端实时训练与生成 playground
- 分步 PR 展示从 bigram 到完整 GPT 的构建过程

## 适用场景

- 逐步理解 GPT 与反向传播的实现细节
- 在浏览器中交互式训练字符级小模型
- 作为从零构建 LLM 的学习教材与代码骨架

## 场景标签

`教程课程` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L3: A TypeScript port of Andrej Karpathy's microgpt — a complete GPT built from scratch with **zero runtime dependencies
> L11: A character-level GPT that learns to generate text. Everything is built from scratch: a `Value` class that tracks c

## 星数曲线

```mermaid
xychart-beta
    title "dubzdubz/microgpt-ts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9a7c434310e4` · [字段定义](../../DATASET.md)*
