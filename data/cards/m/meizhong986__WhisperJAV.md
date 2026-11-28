# meizhong986/WhisperJAV

⭐ 2,512 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/meizhong986/WhisperJAV) · [官网](https://github.com/meizhong986/WhisperJAV/releases/latest) · 个人维护

**为 JAV 音频生成日文字幕的本地 ASR 字幕工具**

在本地运行的日语语音转字幕工具，面向成人影片这类低信噪比、非语音发声密集的长时长音频。流程为音频抽取→场景切分→VAD 语音分段→ASR→后处理，后处理包含句尾助词感知的重组、幻觉与重复删除、纯拟声行删除与时间轴修复；支持 Qwen3-ASR、anime-whisper、Faster-Whisper、OpenAI Whisper 等多后端，提供两遍 ensemble 合并与五维可组合策略，含 Windows 安装包、GUI、CLI 与 Colab/Kaggle notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 场景切分 + VAD 钳制 + 防御性解码三重抗幻觉机制
- 两遍 ensemble：双识别器加双 VAD 合并结果（多种 merge 策略）
- pipeline × 场景检测 × 预处理 × VAD × ASR 模型五维自由组合
- 日语感知后处理：助词重组、幻觉清理、时间轴修复

## 适用场景

- 为日语视频批量生成 .srt/WebVTT 字幕
- 处理嘈杂、非语音密集的长录音并抑制转写幻觉
- 在 Colab/Kaggle 免费算力上运行转写流水线

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L13: A subtitle generator for Japanese Adult Videos. Free, runs on your own machine, no cloud upload of your media.
> L29: - **Scene-based segmentation** — split the audio at natural acoustic boundaries so the model always processes a coh
> L87: |**qwen** (ChronosJAV)|Qwen3-ASR|Modern text-first recognizer|

## 星数曲线

```mermaid
xychart-beta
    title "meizhong986/WhisperJAV 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 2361 --> 2525
    line [2376, 2378, 2383, 2387, 2392, 2400, 2411, 2413, 2374, 2442, 2449, 2451, 2455, 2462, 2464, 2467, 2470, 2476, 2480, 2485, 2487, 2493, 2499, 2502, 2505, 2511, 2512]
```

2026-10-26 2,376 → 2026-11-28 2,512（+136）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `f7a51883234e` · [字段定义](../../DATASET.md)*
