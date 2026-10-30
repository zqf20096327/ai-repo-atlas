# KyungsuKim42/tokensynth

⭐ 98 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/KyungsuKim42/tokensynth) · [官网](https://tinyurl.com/tokensynth-demo) · 个人维护

**从 MIDI 与音色嵌入生成乐器音频的神经合成器（ICASSP 2025）**

TokenSynth 官方实现（ICASSP 2025 论文）：基于 decoder-only transformer 与神经音频 token 的神经合成器，读取 MIDI 与音色嵌入，生成多声部单乐器音频；采用 CLAP 音色条件与 DAC 解码器，支持乐器克隆、文本转乐器（text-to-instrument）与音色操控，无需微调即可进行声音设计。初始化时自动下载预训练权重，以 pip 包形式提供，另附 quickstart 脚本；代码与权重基于 DAC 与 CLAP 的已有成果。

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

- 从 MIDI 与音色嵌入生成多声部单乐器音频
- CLAP 音色条件支持乐器克隆与 text-to-instrument
- 无需微调的音色操控
- 初始化时自动下载预训练权重

## 适用场景

- 给定 MIDI 与参考音色克隆乐器音色
- 用文本描述生成乐器音色
- 音频/音乐研究中的神经合成实验复现

## 场景标签

 · 领域:音频/音乐生成

## 证据(README 行号)

> L12: ### **Official implementation** of "TokenSynth: A Token-based Neural Synthesizer for Instrument Cloning and Text-to
> L14: TokenSynth is a token-based neural synthesizer that generates polyphonic single-instrument musical audio from MIDI 

## 星数曲线

```mermaid
xychart-beta
    title "KyungsuKim42/tokensynth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-30 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7b858a707185` · [字段定义](../../DATASET.md)*
