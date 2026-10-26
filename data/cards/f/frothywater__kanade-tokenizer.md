# frothywater/kanade-tokenizer

⭐ 119 · Python · 推送 2026-07-18 · [GitHub](https://github.com/frothywater/kanade-tokenizer) · [官网](https://frothywater.github.io/kanade-tokenizer/) · 个人维护

**面向语音建模的解耦语音 tokenizer，提取紧凑离散 token**

单层解耦语音 tokenizer，将音频提取为紧凑 token，适用于生成式与判别式建模。模型基于 WavLM-base+ 编码器，提供 12.5Hz/25Hz 多个版本（118M–142M 参数），配套 Vocos 或 HiFT vocoder，支持从 HuggingFace Hub 加载权重做推理，含语音转换示例。训练基于 Lightning 框架，通过配置文件与 CLI 完成预训练、后训练与微调；训练时推荐 FlashAttention，缺失时回退到 PyTorch SDPA（不保证论文同质量）。MIT 许可。

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

- 单层解耦 tokenizer，token 兼顾生成与判别任务
- 三个预训练模型版本（12.5Hz/25Hz/25Hz-clean，118M–142M 参数）
- 支持从 HuggingFace Hub 加载权重推理与微调
- 提供 demo.ipynb 推理示例与语音转换流程

## 适用场景

- 为语音语言模型提供离散 token 表示
- 在自己的语音数据集上微调 tokenizer
- 用 demo notebook 体验推理与语音转换

## 场景标签

 · 领域:语音处理/深度学习

## 证据(README 行号)

> L8: Kanade is a single-layer disentangled speech tokenizer that extracts compact tokens suitable for both generative and
> L32: |Model|Token Rate|Vocab Size|Bit Rate|Dataset|SSL Encoder|Vocoder|Parameters|

## 星数曲线

```mermaid
xychart-beta
    title "frothywater/kanade-tokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-26 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `432a2255b80a` · [字段定义](../../DATASET.md)*
