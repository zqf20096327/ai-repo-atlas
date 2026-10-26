# kyegomez/GPT4o

⭐ 33 · Shell · MIT · 推送 2026-10-19 · [GitHub](https://github.com/kyegomez/GPT4o) · [官网](https://discord.gg/7VckQVxvKk) · 个人维护

**GPT-4o 的社区 PyTorch 复现实现：多模态模型代码**

kyegomez 维护的 GPT-4o 社区开源 PyTorch 实现，覆盖文本、图像、音频的多模态架构。README 描述的推测性设计包括：TikToken 分词器、以 Whisper 与 ViT 类编码器处理音频与图像输入、以 DALL·E 3 作为图像输出头、Whisper 作为音频输出头、用特殊 token 标记生成图像或音频的时机。README 未给出具体安装命令或运行示例，仅列出架构要点与 MIT 许可证。面向多模态 LLM 研究与复现实验的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 实现的多模态（文本/图像/音频）模型代码
- 音频输入/输出使用 Whisper，图像编码使用 ViT 类编码器
- 图像生成输出头基于 DALL·E 3 思路

## 适用场景

- 研究 GPT-4o 推测架构的多模态实现
- 作为多模态 Transformer 实验的代码基础

## 场景标签

`多模态` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L4: Community Open Source Implementation of GPT4o in PyTorch
> L10: - Model understands Images and Audio Natively. There are 2 approaches, process them natively or use encoders for ea

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/GPT4o 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2eb6245ccb29` · [字段定义](../../DATASET.md)*
