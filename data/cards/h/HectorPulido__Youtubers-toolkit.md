# HectorPulido/Youtubers-toolkit

⭐ 61 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/HectorPulido/Youtubers-toolkit) · 个人维护

**视频编辑命令行工具箱：静音裁剪、字幕、转录翻译、短视频生成**

Python 编写的命令行视频处理工具集，面向视频编辑与 YouTube 内容制作场景。以 main.py 为入口提供 5 个子命令：可组合处理管道的视频编辑（静音裁剪、降噪、字幕、方向调整）、音频分离、SRT 字幕拆分、语音操作与短视频生成。语音与转录功能调用 Whisper、Bark 等 AI 模型实现转录、翻译与配音；降噪使用深度学习模型。通过 git clone 源码安装，需 Python 3.10+ 与多个 pip 依赖，经 config.json 配置参数。

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

- 管道式视频编辑：静音裁剪/降噪/字幕/方向调整可组合执行
- 基于 Whisper 的转录与基于翻译模型的视频翻译、Bark 配音
- 短视频生成：模糊背景基底视频与标题叠加
- SRT 字幕按词数拆分与音频分离工具

## 适用场景

- 批量去除视频中的静音片段并自动加字幕
- 将视频转录或翻译成英文并生成配音
- 为短视频生成带模糊背景和标题的基底视频

## 场景标签

`图像视频处理` `语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: This project is a comprehensive command-line toolkit designed for video editing and processing tasks. It provides a 
> L10: - **Voice Operations:** Utilizes AI models (e.g., Whisper, Bark) for video translation and audio generation.

## 星数曲线

```mermaid
xychart-beta
    title "HectorPulido/Youtubers-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-30 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `34d6ec4b0aab` · [字段定义](../../DATASET.md)*
