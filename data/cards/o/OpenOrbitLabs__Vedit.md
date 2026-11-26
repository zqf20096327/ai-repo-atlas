# OpenOrbitLabs/Vedit

⭐ 3 · Python · MIT · 推送 2026-11-13 · [GitHub](https://github.com/OpenOrbitLabs/Vedit) · 个人维护

**给内容创作者的 AI 视频剪辑 CLI：自动剪口误并加字幕**

面向内容创作者的开源视频编辑工具，输入原始录像，自动去除停顿、填充词与废镜头，生成逐词动画字幕、竖版裁切、缩略图与章节。以 CLI 运行，也可注册为 Claude Code skill，由 Claude 读取词级转写与视频帧做编辑决策。剪辑以 JSON 格式的 edl.json 存储，可版本控制与复现。支持 YouTube/Shorts/TikTok/Reels 等预设、品牌套件、照片加脚本的故事模式与 Fact Reels 套件。需要 Python 3.9+ 与含 libass 的 FFmpeg；转写基于 faster-whisper，首次运行需下载约 500 MB 模型。

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

- 词级精确剪辑：去除死气、填充词与废镜头
- 逐词动画字幕与 .srt 导出，多格式导出与人脸感知裁切
- 剪辑以 edl.json 存储，可审查、重复与版本控制
- 可作为 Claude Code skill，由 Claude 做编辑决策并渲染

## 适用场景

- 把口播录像一键剪成 YouTube/Shorts 成片
- 批量处理整个文件夹的视频并按平台预设导出
- 用照片加脚本生成带 AI 旁白的 Fact Reels
- 多机位播客自动同步与发言人切换

## 场景标签

`视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: **An open-source AI video editor for content creators. Raw footage in, finished video out.**
> L25: **vedit automates that work.** It runs as:
> L273: 1. **Analyze** extracts facts: a word-level transcript (faster-whisper), silences, scene changes, loudness and fra


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `227cc6183771` · [字段定义](../../DATASET.md)*
