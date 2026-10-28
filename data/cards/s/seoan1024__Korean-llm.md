# seoan1024/Korean-llm

⭐ 114 · Python · GPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/seoan1024/Korean-llm) · [官网](korean-llm-show.vercel.app) · 个人维护

**个人环境中从零实现的韩语 1.09B 解码器 Transformer LLM**

个人学习型项目：作者在 PyTorch 中直接实现解码器风格 Transformer 的各组件（Embedding、Attention、SwiGLU FFN、RMSNorm、RoPE、权重绑定输出层），构成约 1.09B 参数模型，使用 beomi/Llama-3-Open-Ko-8B 分词器，按 Pretraining→SFT 两阶段训练（默认 100,000/10,000 步，BF16，AdamW8bit 可选），训练默认序列长度 512，带 Tkinter+Matplotlib 监控。README 记录了 v1 前 50M 到 v4 的迭代过程，v3 关注量化与轻量化，v4 重构数据与训练管线。面向想了解 LLM 构造的开发者与学习者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直接实现 Transformer 核心组件（非封装外部 LLM 类）
- 约 1.09B 参数：dim 1920 / 20 层 / 10 头 / SwiGLU / RoPE / RMSNorm
- Pretraining→SFT 两阶段训练流程，BF16 精度与 AdamW8bit 支持
- Tkinter + Matplotlib 训练监控与 .pth 检查点

## 适用场景

- 学习 LLM 内部结构与训练流程并对照源码
- 在个人环境复现小规模韩语 LLM 的预训练与 SFT
- 跟踪从 50M 到 1.09B 的模型迭代实验记录

## 场景标签

`模型训练` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L14: |목적|개인 환경에서 직접 만들어보는 한국어 LLM|
> L15: |계열|Decoder-style Transformer|
> L373: 모델의 핵심 Transformer 구성은 코드 안에서 직접 구현되어 있습니다.

## 星数曲线

```mermaid
xychart-beta
    title "seoan1024/Korean-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-28 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4e4c59c57e4e` · [字段定义](../../DATASET.md)*
