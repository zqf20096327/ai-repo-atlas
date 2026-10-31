# dimaskiddo/yaclip

⭐ 14 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/dimaskiddo/yaclip) · 个人维护

**把长 YouTube 视频自动切成竖屏短视频（Shorts/Reels/TikTok）的 CLI/WebUI 工具**

面向短视频创作者的自动剪辑工具：粘贴 YouTube 链接后自动下载视频、检测内容类型（播客/游戏/直播）、定位高光片段、转写并交由 AI 挑选最佳片段，输出带逐字动画字幕的 9:16 竖屏剪辑。AI 方案支持 Gemini/OpenAI 云端、本地转写+云端选片或全离线三种。自动下载所需工具与模型到 workspace 目录，文件不写入外部；提供预编译二进制（CPU/CUDA）、Docker 及源码三种安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 云端/混合/全离线三种 AI 管线（Gemini、OpenAI 或本地模型）
- YOLOv8n 内容类型检测 + MediaPipe 人脸跟踪智能构图
- 逐词高亮 ASS 字幕，支持约 34 种语言
- 每条剪辑自动生成标题/描述/标签的元数据文件

## 适用场景

- 把长视频或直播录像批量转成短视频平台可发布的竖屏片段
- 无剪辑经验用户粘贴链接一键获得带字幕的成片
- 用 CLI 与时间戳文件手动指定片段并自动渲染

## 场景标签

`语音识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **YaClip** automatically turns long YouTube videos into short vertical clips, ready to post on YouTube Shorts, Insta
> L10: * **🧠 AI-powered clip selection:** Uses Google Gemini, OpenAI, or local AI to read the video transcript and pick th

## 星数曲线

```mermaid
xychart-beta
    title "dimaskiddo/yaclip 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `7d0148ce489b` · [字段定义](../../DATASET.md)*
