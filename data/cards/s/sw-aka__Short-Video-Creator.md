# sw-aka/Short-Video-Creator

⭐ 185 · Python · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/sw-aka/Short-Video-Creator) · 个人维护

**本地生成带 AI 字幕与背景视频的短视频剪辑工具**

Python CLI 工具，将输入视频自动剪辑为带背景视频与 AI 生成字幕的短视频，可用于 YouTube Shorts、TikTok、Instagram Reels、Snapchat Spotlight。字幕通过 NVIDIA Parakeet TDT 0.6B v3 模型在本地转录（onnx-asr 运行时，默认 CPU，Windows/macOS/Linux 可用），模型约 600MB 首次运行时从 Hugging Face 下载并缓存，无需任何 API key。FFmpeg 由 imageio-ffmpeg 捆绑提供，无需单独安装。支持文件夹批量处理，并提供 create_short 库 API。许可为 CC BY-NC-SA 4.0（非商业）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地转录字幕，无需 API key，CPU 默认运行
- 背景视频叠加与多平台短视频格式输出
- 文件夹批量处理 CLI，失败汇总并以非零状态退出
- 提供 Python 库 API（create_short）

## 适用场景

- 批量生成带字幕和背景视频的短视频内容
- 离线环境制作 YouTube Shorts / TikTok 视频
- 通过库 API 集成到自己的视频生产流程

## 场景标签

`语音识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: Tool to automatically create short clips with a background video and AI-generated captions.
> L16: Captions are transcribed locally with NVIDIA's
> L19: Windows, macOS and Linux, CPU-only by default). The model (~600 MB) is

## 星数曲线

```mermaid
xychart-beta
    title "sw-aka/Short-Video-Creator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 183 --> 186
    line [184, 185, 185]
```

2026-10-18 184 → 2026-10-30 185（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c809f75f63cf` · [字段定义](../../DATASET.md)*
