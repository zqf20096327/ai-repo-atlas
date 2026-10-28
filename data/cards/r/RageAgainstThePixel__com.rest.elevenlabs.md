# RageAgainstThePixel/com.rest.elevenlabs

⭐ 109 · C# · MIT · 推送 2026-03-09 · [GitHub](https://github.com/RageAgainstThePixel/com.rest.elevenlabs) · [官网](https://try.elevenlabs.io/rage-against-the-pixel) · 个人维护

**Unity 平台的 ElevenLabs 语音合成非官方客户端**

基于 ElevenLabs-DotNet 封装的 Unity (UPM) 包，为 Unity 游戏引擎提供 ElevenLabs REST API 的 C# 客户端，支持文本转语音与流式合成、语音库/语音设计/语音克隆管理、配音（Dubbing）与转录获取，并提供 Unity Editor 内的 Dashboard 窗口（合成片段可自动导入项目）。API key 支持 4 种加载方式，另给出通过 ASP.NET Core 代理保护前端密钥的方案。需自备 ElevenLabs 账号与 API 访问权限，与 ElevenLabs 官方无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Unity 内文本转语音与流式合成，音频片段可直接导入项目
- 语音管理：共享语音库、语音设计、语音克隆、样本下载/删除
- 音频/视频文件配音（Dubbing）及字幕转录导出
- Editor Dashboard：在 Unity 编辑器内完成官网同等操作

## 适用场景

- 在 Unity 游戏中调用 ElevenLabs 生成角色语音
- 在编辑器内设计、克隆和管理语音并下载到项目
- 通过代理服务器架构避免前端暴露 ElevenLabs API key

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: A non-official ElevenLabs voice synthesis RESTful client for the Unity Game Engine.
> L214: ### Text to Speech

## 星数曲线

```mermaid
xychart-beta
    title "RageAgainstThePixel/com.rest.elevenlabs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-28 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fd0b32055c13` · [字段定义](../../DATASET.md)*
