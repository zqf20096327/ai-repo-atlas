# j3soon/whisper-to-input

⭐ 141 · Kotlin · GPL-3.0 · 推送 2025-12-21 · [GitHub](https://github.com/j3soon/whisper-to-input) · 个人维护 · 中文 README

**调用 Whisper 语音转文字的 Android 输入法键盘**

Android 输入法应用（IME），通过麦克风录音并将语音识别结果直接输入文本框，支持英语、中文、日语等多语言及混合语言，台语（闽南语）转写未官方声明但有用户反馈可用。识别后端三选一：OpenAI API（需 API key）、自托管 Whisper ASR Webservice、或自托管 NVIDIA NIM（基于 Riva、TensorRT-LLM）。安装方式为下载 release 页 APK 并手动安装（会触发'不安全应用'警告），当前发布均为 debug 构建，通过 adb logcat 查看日志。GPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种可选 STT 后端：OpenAI API / Whisper ASR Webservice / NVIDIA NIM
- 支持多语言与混合语言识别，含台语（闽南语）转写反馈
- 以 Android 输入法形式将识别文本直接输入任意文本框

## 适用场景

- 在手机上用语音输入替代打字，识别结果直接进文本框
- 自托管 Whisper 服务后在本机键盘使用，不依赖 OpenAI API
- 中英日混合语音输入场景

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Whisper To Input, also known by its Mandarin name 輕聲細語輸入法, is an Android keyboard that performs speech-to-text (STT/
> L5: The STT/ASR backend service can be either OpenAI API, Whisper ASR Webservice, or NVIDIA NIM (based on NVIDIA Riva).

## 星数曲线

```mermaid
xychart-beta
    title "j3soon/whisper-to-input 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 139 --> 142
    line [140, 141, 141]
```

2026-10-18 140 → 2026-10-26 141（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c6890700dea9` · [字段定义](../../DATASET.md)*
