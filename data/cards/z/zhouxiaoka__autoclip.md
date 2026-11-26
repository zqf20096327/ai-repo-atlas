# zhouxiaoka/autoclip

⭐ 16,120 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/zhouxiaoka/autoclip) · [官网](https://zhouxiaoka.github.io/autoclip_intro/) · 个人维护 · 中文 README

**长视频一键剪成短视频的本地 AI 剪辑桌面工具**

AutoClip 接收视频链接、本地文件或直播回放（OBS/Twitch/YouTube/Kick/Discord），自动定位精彩片段、跟踪说话人、烧录字幕、生成封面与发布文案，导出适配 TikTok、Shorts、Reels、抖音、小红书、Bilibili 等平台的短视频。剪切与渲染在本地完成；分析可自带 API key 使用云端模型，也可用 Ollama/LM Studio + Whisper/SenseVoice 完全离线。提供桌面安装包、CLI/MCP、Docker Web 三种使用方式，13 种语言界面，MIT 许可，个人维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持链接、本地文件与 6 种直播回放来源，自动剪辑并烧录字幕
- 本地优先：剪切与渲染在本地运行，可选 Ollama/LM Studio 全离线
- 一键切换目标平台导出，生成封面与发布文案
- 提供桌面安装包、CLI/MCP（uvx/npx）与 Docker Web 部署

## 适用场景

- 把播客、访谈、课程长视频批量剪成各平台短视频
- 游戏直播结束后从 OBS/Twitch 回放快速产出高光片段
- 无 API key 环境下用本地模型离线完成剪辑流程

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: Open-source, local-first AI clipping for **podcasts, interviews, and gaming streams** — with smart reframing, captio
> L37: Drop in a link, local video, or **live stream replay** — AutoClip finds the best moments, tracks the speaker, burns
> L167: |**AI agents / CLI / MCP**|`uvx autoclip-mcp` or `npx skills add zhouxiaoka/autoclip`|Python 3.10+ (3.11 recommend

## 星数曲线

```mermaid
xychart-beta
    title "zhouxiaoka/autoclip 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 9022 --> 16765
    line [9667, 9690, 9715, 9755, 9781, 9820, 9856, 9874, 9896, 9911, 9690, 10125, 10255, 10311, 10364, 10404, 10454, 10509, 10599, 10673, 10795, 11162, 12122, 12776, 13372, 14431, 16120]
```

2026-10-24 9,667 → 2026-11-26 16,120（+6,453）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4479ad4b35f7` · [字段定义](../../DATASET.md)*
