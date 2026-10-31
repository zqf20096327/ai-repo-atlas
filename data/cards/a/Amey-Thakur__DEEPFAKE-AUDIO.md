# Amey-Thakur/DEEPFAKE-AUDIO

⭐ 76 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/Amey-Thakur/DEEPFAKE-AUDIO) · [官网](https://huggingface.co/spaces/ameythakur/Deepfake-Audio) · 个人维护

**基于 SV2TTS 的零样本人声克隆语音合成工作室**

实现 SV2TTS（Transfer Learning from Speaker Verification to Multispeaker TTS）的多阶段神经语音合成平台：用说话人编码器从参考音频提取声音嵌入，经 Tacotron 2 合成器与 WaveGlow 声码器生成目标文本的克隆语音，基于 Corentin Jemine 的 Real-Time-Voice-Cloning 构建。以 Gradio Web 界面（PWA）与命令行脚本两种方式运行，需自行放置预训练权重文件，另提供 Hugging Face Space 与 Google Colab 环境。面向学习与研究用途，采用 MIT 许可。

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

- SV2TTS 三阶段管线：LSTM 说话人编码器 + Tacotron 合成器 + WaveGlow 声码器
- Gradio Web 工作室可安装为 PWA 桌面应用
- 支持预设身份或自定义语音文件的命令行合成脚本
- 提供 Hugging Face Space 在线演示与 Google Colab 云端环境

## 适用场景

- 学习零样本人声克隆与 SV2TTS 迁移学习原理
- 用参考音频为目标文本生成克隆语音
- 作为深度学习或声学课程的实验参考项目

## 场景标签

`语音合成` `教程课程` · 领域:内容生成

## 证据(README 行号)

> L8:  An advanced neural voice synthesis platform implementing Transfer Learning from Speaker Verification to Multispeake
> L29: **Deepfake Audio** is a multi-stage neural voice synthesis architecture designed to clone speaker identities and ge

## 星数曲线

```mermaid
xychart-beta
    title "Amey-Thakur/DEEPFAKE-AUDIO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-31 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `aeb052d2ee41` · [字段定义](../../DATASET.md)*
