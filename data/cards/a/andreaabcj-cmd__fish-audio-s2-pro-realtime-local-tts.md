# andreaabcj-cmd/fish-audio-s2-pro-realtime-local-tts

⭐ 3 · HTML · NOASSERTION · 推送 2026-10-14 · [GitHub](https://github.com/andreaabcj-cmd/fish-audio-s2-pro-realtime-local-tts) · [官网](https://andreaabcj-cmd.github.io/fish-audio-s2-pro-realtime-local-tts/) · 个人维护

**16 GB 消费级 GPU 上实时本地运行 Fish S2 Pro TTS 的实测笔记**

记录在 RTX 5060 Ti 16 GB（Windows）上让 Fish Audio S2 Pro 通过 audio.cpp 实时流式合成语音，并与 Ollama 中的 12B 对话模型共享显存的完整过程：audio.cpp 0.9.1 无法流式输出 Fish，需从源码构建（≥ commit b0feeff），文中给出 MSVC/CUDA 构建步骤、Q4/Q6/Q8 量化文件制备配方、server 配置与约 200 行 Python 适配器，并附三类量化在流式首音延迟、RTF、VRAM 与完整管线下播缓冲的基准数据，以及 Ollama 提示前缀缓存的加速技巧。实测限于一台机器、西班牙语和单一听感评审。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- audio.cpp 需从源码构建才能流式运行 Fish 模型（含 CUDA/MSVC 构建步骤）
- Q4_K GGUF 实测首音 0.14–0.31 s、生成约等于音频时长、峰值 7.0 GB VRAM
- 约 200 行适配器将 SSE 44.1 kHz 流转为 24 kHz PCM，并管理 VRAM 释放
- Ollama 提示缓存技巧把每轮 3.4 s 前缀重读降至约 1.2 s

## 适用场景

- 在 16 GB 显存上让本地 LLM 语音助手共享 GPU 同时跑对话与 TTS
- 需要低首音延迟的本地流式语音合成部署参考
- 为 sliding-window 模型优化 Ollama 每轮提示重读耗时

## 场景标签

`语音合成` `模型量化` · 领域:内容生成

## 证据(README 行号)

> L1: # Fish Audio S2 Pro as a *real-time* local voice on a 16 GB GPU — next to a 12B LLM (Windows, RTX 5060 Ti)
> L5: Field notes from building a fully local voice assistant (Spanish, voice cloning from a short reference + transcript)
> L6: Everything below was measured on **one machine**, in October 2026. Where something was *not* measured, it says so.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `bff965234943` · [字段定义](../../DATASET.md)*
