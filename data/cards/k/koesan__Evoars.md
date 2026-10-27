# koesan/Evoars

⭐ 24 · Python · Apache-2.0 · 推送 2026-06-01 · [GitHub](https://github.com/koesan/Evoars) · [官网](https://koesan-mangaspaces.hf.space) · 个人维护

**面向漫画/视频创作者的多模型 AI 媒体处理 Web 平台**

基于 Flask/PyTorch 的 Web 平台，自动化处理漫画与视频：用预训练神经网络给黑白漫画上色；用 PaddleOCR 检测文本、DeepL 翻译、LAMA inpainting 去字并回填译文；用 Whisper 转录生成 SRT 字幕并翻译；用 TTS 语音克隆生成多语言配音并与原视频同步。技术栈含 PyTorch 2.2.2、OpenCV、FFmpeg、MoviePy。需自备 DeepL API key 与从 Google Drive 下载模型权重，提供 Docker 与手动两种安装方式，README 标注 V3 架构开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 黑白漫画深度学习上色（预训练 generator 模型）
- OCR 检测+DeepL 翻译+LAMA inpainting 的漫画翻译流水线
- Whisper 转录生成带时间戳的 SRT 字幕并翻译
- TTS 语音克隆生成多语言配音并与原视频同步

## 适用场景

- 把黑白漫画页自动上色成彩色
- 将漫画翻译成其他语言并保留原对话框排版
- 为视频自动生成并翻译字幕
- 用克隆的原说话人声音做多语言配音

## 场景标签

`语音合成` `语音识别` `OCR` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L54: **Evoars** is an AI-powered web platform that fully automates the processing of manga, comics, and videos. Using ad
> L92: 2. **Speech Recognition**: OpenAI Whisper transcribes audio to text with timestamps

## 星数曲线

```mermaid
xychart-beta
    title "koesan/Evoars 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bdd95672404a` · [字段定义](../../DATASET.md)*
