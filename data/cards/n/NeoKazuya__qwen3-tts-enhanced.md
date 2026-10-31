# NeoKazuya/qwen3-tts-enhanced

⭐ 20 · Python · Apache-2.0 · 推送 2026-02-02 · [GitHub](https://github.com/NeoKazuya/qwen3-tts-enhanced) · 个人维护

**Qwen3-TTS 语音克隆增强图形界面，多参考样本与变体生成**

为 Qwen3-TTS 模型提供 Gradio 图形界面的语音克隆工具：支持最多 5 个参考音频样本合成克隆、一次生成 1-5 个变体供挑选、音频自动归一化与可选降噪，另有预设说话人情感控制、从文本描述设计声音、以 .pt 文件保存与加载声音等功能。面向拥有 NVIDIA GPU（8GB+ VRAM）的个人用户，完全本地运行；Windows 提供 install.bat 一键安装，Linux 走 Docker，首次运行下载约 4GB 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 最多 5 个参考音频的多参考克隆
- 一次生成 1-5 个变体供挑选
- 音频自动归一化与可选降噪
- 声音可保存为便携 .pt 文件

## 适用场景

- 用几秒到几十秒的音频样本克隆声音
- 生成多个语音变体挑选最满意的结果
- 无需命令行，通过界面使用 Qwen3-TTS 本地合成语音

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: Clone any voice in seconds. 100% local, runs on your GPU.
> L5: An enhanced interface for Qwen3-TTS with multi-reference cloning, variation generation, and audio preprocessing.

## 星数曲线

```mermaid
xychart-beta
    title "NeoKazuya/qwen3-tts-enhanced 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d35cb24c552b` · [字段定义](../../DATASET.md)*
