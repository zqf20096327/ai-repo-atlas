# gabrielmartinslascau-lsxnya/Capri

⭐ 3 · Kotlin · GPL-3.0 · 推送 2026-11-15 · [GitHub](https://github.com/gabrielmartinslascau-lsxnya/Capri) · 个人维护

**安卓手机上的傲娇 AI 悬浮助手，可代替你操作屏幕和游戏**

一个侧载在 Android 手机上的 AI agent 应用，以悬浮气泡或全屏聊天界面提供对话，并通过无障碍服务接管屏幕执行任务：理解 Android UI 层级操作应用（APP_MODE），或用多点触控序列与反射扫描器操作 OpenGL 游戏画面（GAME_MODE）。视觉上采用无网格精确像素截图加 ML Kit OCR 坐标映射。大脑可选用云端 API（Gemini/Claude/Groq/OpenRouter）或本地下载的 Gemma 离线模型。带三级持久记忆、Brain Inspector 调试时间线。v15 为 Beta/Preview，每步操作耗时约 1.2–3.5 秒，3D 游戏功能为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 双模式屏幕代理：APP_MODE 理解 Android UI 层级，GAME_MODE 面向 OpenGL 游戏画面
- 本地 Gemma 模型可 100% 离线运行（约 2.6 GB .litertlm），或接入自备 API key 的云端模型
- 三级持久记忆：战略计划、死点击黑名单、跨屏幕应用路径面包屑
- Brain Inspector 展示每步截图、OCR 检测、延迟与模型输出的时间线

## 适用场景

- 用自然语言让 AI 代为操作手机应用，如在 Spotify 播放喜欢的歌、回复短信
- 让 AI 代打 Plants vs. Zombies 或 Minecraft 等手机游戏
- 长时间刷短视频时收到针对当前应用的提醒

## 场景标签

`GUI 自动化` `AI 助手` `OCR` · 领域:效率与自动化

## 证据(README 行号)

> L3: A small, slightly chaotic tsundere AI that lives on your Android phone as a floating bubble—or inside her own full-s
> L29:  Ask her for anything—*"go on Spotify and play one of my liked songs"*, *"open mornye and play something from my li
> L60: 1. **Cloud AI (Gemini, Anthropic, Groq, or OpenRouter).** Plug in your own API key. Fastest, sharpest vision, and h

## 星数曲线

```mermaid
xychart-beta
    title "gabrielmartinslascau-lsxnya/Capri 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `27881a9bfbca` · [字段定义](../../DATASET.md)*
