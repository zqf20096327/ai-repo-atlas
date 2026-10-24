# divyaprakash0426/autoshorts

⭐ 205 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/divyaprakash0426/autoshorts) · 个人维护

**把长视频自动切分为竖版短视频的 AI 剪辑工具**

面向内容创作者的视频处理工具：从长篇游戏录像等素材中，用 AI 场景分析（Gemini/OpenAI vision 或本地启发式）选取精彩片段，生成带样式字幕的竖版短片，支持 Whisper 转录、AI 生成字幕与可选的本地 Qwen3-TTS 多语言配音。渲染依赖 NVIDIA GPU：CUDA 解码/分析与 NVENC 编码，配音建议 6GB+ VRAM 与 16GB 内存。提供 Streamlit 仪表盘与 CLI 两种运行方式，通过 git clone 加 make install 安装，也提供 Docker 设置。云端分析会上传视频内容并可能产生 API 费用，local 模式用启发式选择但渲染仍需 NVIDIA 硬件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 种内容预设，游戏/电竞用动作启发式加 AI 排序，其他类型用 AI 优先选择
- Gemini/OpenAI vision/本地启发式三种分析模式可选
- Whisper 转录、AI 字幕、本地 Qwen3-TTS 多语言配音
- CUDA 解码与 NVENC 编码的 GPU 渲染，可配置输出比例

## 适用场景

- 把游戏直播录像自动剪成多条竖版短视频
- 播客、访谈等长内容批量生成带字幕的短片
- 为短视频添加多语言 AI 配音旁白

## 场景标签

`图像视频处理` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: Turn long-form videos into short clips with AI-assisted moment selection,
> L19: - **Content-aware clipping:** 15 presets with their own moment categories, analysis
> L22: - **Flexible analysis:** Gemini, including full-video deep analysis; OpenAI vision;

## 星数曲线

```mermaid
xychart-beta
    title "divyaprakash0426/autoshorts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-24 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e2301fb7f60c` · [字段定义](../../DATASET.md)*
