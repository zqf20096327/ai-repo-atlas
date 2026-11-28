# NaufalRizqullah/opensource-clipping

⭐ 553 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/NaufalRizqullah/opensource-clipping) · [官网](https://naufalrizqullah.github.io/opensource-clipping/) · 个人维护

**开源 AI 视频剪辑工具：把长视频/播客转成短视频**

以 Python CLI、Google Colab/Kaggle 笔记本和 GitHub Pages 网页版 Studio 三种形式提供，将 YouTube/TikTok 等长视频处理为竖版短视频。流程包括 Faster-Whisper 词级转录、LLM 分析并选取高光片段、MediaPipe 人脸追踪自动取景、卡拉OK字幕、B-roll 插入、配音与自动生成缩略图，并支持定时上传 YouTube/Facebook。需要 Python 3.10+、FFmpeg 与至少一个 AI 提供商 API key；无本地 GPU 可通过 Colab 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种运行方式：CLI、Colab/Kaggle 笔记本、GitHub Pages 网页 Studio
- Faster-Whisper 词级转录与 Pyannote 说话人分离（分屏/镜头切换）
- 支持 Gemini、NVIDIA NIM 或自托管 vLLM 作为分析后端
- 支持定时自动上传 YouTube 与 Facebook Reels

## 适用场景

- 把播客长视频批量切成 9:16 短视频片段
- 为短视频自动生成卡拉OK字幕与缩略图
- 没有本地 GPU 时在 Colab 上运行剪辑流程
- 定时自动发布剪辑结果到 YouTube/Facebook

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5:  Ultimate AI Auto-Clipper &amp; Teaser Generator
> L36: |**AI Content Curator**|**Google Gemini**, **NVIDIA NIM**, or self-hosted **vLLM** analyzes context, selects highli
> L60: - **CUDA GPU** recommended (for Whisper; CPU fallback available)

## 星数曲线

```mermaid
xychart-beta
    title "NaufalRizqullah/opensource-clipping 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 149 --> 589
    line [187, 196, 197, 199, 201, 202, 204, 207, 185, 219, 233, 240, 247, 257, 265, 285, 299, 309, 370, 450, 479, 499, 516, 525, 539, 544, 553]
```

2026-10-26 187 → 2026-11-28 553（+366）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7ac4e9f4d602` · [字段定义](../../DATASET.md)*
