# jlin816/dynalang

⭐ 420 · Python · 推送 2026-01-07 · [GitHub](https://github.com/jlin816/dynalang) · [官网](https://dynalang.github.io) · 个人维护

**ICML 2024 论文 Dynalang 官方代码：用语言辅助世界模型的强化学习智能体**

论文 Learning to Model the World with Language 的官方实现。Dynalang 是一个利用多种语言输入（任务描述、说明书、指令等）的多模态世界模型智能体，通过语言预测未来来辅助强化学习决策。代码以 JAX 实现，覆盖四个实验环境：HomeGrid、Messenger、VLN（视觉语言导航，需 Habitat 模拟器与 Matterport3D 数据）、LangRoom，另提供在 TinyStories 上做文本预训练与加载检查点微调的流程。安装以 pip 源码方式为主，各环境依赖差异较大。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模态世界模型将语言用于预测未来
- 支持 HomeGrid/Messenger/VLN/LangRoom 四个实验环境
- 提供 TinyStories 文本预训练与世界模型检查点加载微调
- 基于 JAX，支持多 GPU 指定训练设备

## 适用场景

- 复现论文中的语言辅助世界模型实验
- 在 HomeGrid/Messenger 等环境上训练 Dynalang 智能体
- 研究语言预训练对世界模型与策略学习的影响

## 场景标签

`强化学习` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Learning to Model the World with Language
> L5: This repository contains the code for the paper Learning to Model the World with Language. We introduce Dynalang, an

## 星数曲线

```mermaid
xychart-beta
    title "jlin816/dynalang 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 419 --> 421
    line [420, 420]
```

2026-10-18 420 → 2026-10-24 420（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `10e1a9ae8a44` · [字段定义](../../DATASET.md)*
