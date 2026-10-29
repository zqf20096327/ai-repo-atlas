# Mobile-Artificial-Intelligence/babylon

⭐ 41 · C++ · MIT · 推送 2026-04-14 · [GitHub](https://github.com/Mobile-Artificial-Intelligence/babylon) · 组织维护

**C/C++ 本地离线 TTS 与字素转音素库**

用 C/C++ 实现的图素到音素（G2P）转换与神经语音合成库，推理全部经 ONNX Runtime 在本地运行，无需联网。支持三个 TTS 引擎：Kokoro（24kHz、54+ 多语言音色）、kittenTTS（轻量多音色模型）与 VITS（兼容 Piper 模型转换后使用）；音素化由约 13 万词条发音词典支撑的 Open Phonemizer 完成。提供 CLI（phonemize/tts/serve 子命令）、REST API（含 Web 前端）及 C/C++ API，覆盖 Linux/macOS/Windows/Android，通过 CMake 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三引擎 TTS：Kokoro / kittenTTS / VITS（兼容 Piper 模型）
- G2P 由约 130,000 词条发音词典的 Open Phonemizer 支撑
- 全部推理本地 ONNX Runtime，无需联网
- 提供 CLI、REST API（含 Web 前端）与 C/C++ API

## 适用场景

- 在本地应用中离线合成语音或做文本音素化
- 通过 REST 服务为其他程序提供 TTS 与 G2P 能力
- 在 Android 等多平台嵌入神经语音合成

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L10: Babylon.cpp is a C and C++ library for grapheme-to-phoneme (G2P) conversion and neural text-to-speech (TTS) synthes
> L14: - **Kokoro** — High-quality multi-voice neural TTS at 24 kHz with 54+ voices across multiple languages.

## 星数曲线

```mermaid
xychart-beta
    title "Mobile-Artificial-Intelligence/babylon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ab5b2fc81c5c` · [字段定义](../../DATASET.md)*
