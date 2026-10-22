# Shaarav4795/ClippedAI

⭐ — · [GitHub]() · 个人维护

**AI 长视频转 YouTube Shorts 剪辑生成器，OpusClip 开源替代**

基于 Python 与 clipsai 库的视频剪辑工具：用 Whisper 模型转录、Pyannote 做说话人分离，按词密度（45%）、互动词比例（30%）、时长均衡（25%）打分选取片段，自动裁剪为 9:16 并生成带样式的动态字幕；标题由 Groq API（免费层）生成。需 HuggingFace token 访问 Pyannote 模型（首次下载约 2GB），FFmpeg 为必需依赖，转录模型大小可按 RAM/VRAM 配置。以源码方式运行 python main.py，许可为 CC BY-NC 4.0（禁商用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 转录 + Pyannote 说话人分离的本地处理流程
- 三因子加权（词密度/互动词/时长）的片段评分选取
- 自动 9:16 裁剪与 ASS 动态字幕（Montserrat 字体、数字高亮）
- 转录缓存与多视频批量处理，6 档模型按硬件选择

## 适用场景

- 把长视频自动切成多条 YouTube Shorts
- 不想付订阅费、需本地处理视频隐私内容时使用
- 按自己硬件选择转录模型批量出片

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: **Open-source alternative to OpusClip** - Transform long-form videos into engaging YouTube Shorts automatically usin
> L10: - **Smart Clip Detection**: AI identifies the most engaging moments in your videos
> L13: - **Viral Title Generation**: AI generates catchy, titles optimized for engagement

## 星数曲线

```mermaid
xychart-beta
    title "Shaarav4795/ClippedAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-19"]
    y-axis "stars" 217 --> 219
    line [218, 218]
```

2026-10-18 218 → 2026-10-19 218（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `84614411d3f1` · [字段定义](../../DATASET.md)*
