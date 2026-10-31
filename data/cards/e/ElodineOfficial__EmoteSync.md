# ElodineOfficial/EmoteSync

⭐ 14 · Python · MIT · 推送 2026-06-02 · [GitHub](https://github.com/ElodineOfficial/EmoteSync) · [官网](https://www.youtube.com/@ElodineCodes) · 个人维护

**为视频创作者自动生成 PNGTuber 情绪动画视频的桌面工具**

基于 tkinter GUI 的 Python 应用：读取音频文件，用 OpenAI Whisper 做语音识别、Hugging Face Transformers 做情绪检测，再按检测到的情绪将对应情绪图片叠加到背景视频或透明背景上生成视频。支持 7 种基础情绪图片（可扩展）、弹跳动画、同情绪片段合并等选项。需 Python 3.7+ 与 FFmpeg，从源码运行，首次运行时下载模型。README 声明已过时，软件近期经过大幅重构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 语音识别 + Transformers 情绪检测的管线
- 情绪图片叠加到背景视频或透明背景（输出 mp4/webm）
- 弹跳动画、同情绪片段合并、缺失图片回退 neutral.png
- tkinter 图形界面，无需订阅

## 适用场景

- 给配音音频自动生成带情绪变化的 PNGTuber 视频
- 为直播或视频内容制作透明背景的情绪动画素材
- 批量将语音转为配图视频内容

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: EmoteSync is a Python application that analyzes audio files, detects emotions using AI models, and generates videos 
> L11: - **Audio Emotion Detection**: Analyze audio files and detect emotions in speech using AI models.

## 星数曲线

```mermaid
xychart-beta
    title "ElodineOfficial/EmoteSync 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c96451c4e8ed` · [字段定义](../../DATASET.md)*
