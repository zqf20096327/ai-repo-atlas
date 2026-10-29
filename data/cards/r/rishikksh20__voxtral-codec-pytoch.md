# rishikksh20/voxtral-codec-pytoch

⭐ 18 · Python · 推送 2026-03-27 · [GitHub](https://github.com/rishikksh20/voxtral-codec-pytoch) · 个人维护

**Voxtral 语音编解码器的 PyTorch 训练实现，用于 TTS**

Mistral AI Voxtral TTS 论文中 codec 组件的 PyTorch 实现：将 24 kHz 单声道语音切分为 240 样本 patch，经因果卷积-transformer 编码器降至 12.5 Hz 帧率，292 维潜变量拆分为 256 维语义 VQ（8192 码本）与 36 维声学 FSQ，每帧输出 37 个 token，码率约 2.14 kbps。支持 Whisper ASR 蒸馏、多分辨率 STFT 判别器、GAN 训练，附冒烟测试与单元测试（33 项通过）。README 声明部分论文细节为近似实现，非完整复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 292 维潜变量拆分：256 维语义 VQ + 36 维声学 FSQ，约 2.14 kbps
- Whisper 解码器隐状态蒸馏与多分辨率 STFT 判别器
- 提供冒烟训练循环 dummy_train.py 与 33 项单元测试
- 训练时量化行为：50% 量化/直通混合（语义 VQ）

## 适用场景

- 在自有 24 kHz 语音数据上训练 Voxtral 风格 codec 为 TTS 提供离散码
- 复现论文中的语义 VQ + 声学 FSQ 量化方案做实验
- 在 CPU 上运行冒烟测试验证模型接线

## 场景标签

 · 领域:语音合成/音频编解码

## 证据(README 行号)

> L3: This repository contains a PyTorch implementation of the Voxtral Codec component used to convert 24 kHz mono speech 
> L9: - Semantic vector quantization with an 8192-entry codebook
> L10: - Acoustic finite scalar quantization with 21 levels per dimension

## 星数曲线

```mermaid
xychart-beta
    title "rishikksh20/voxtral-codec-pytoch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `de2c9d316a39` · [字段定义](../../DATASET.md)*
