# ds-kimi/Auris

⭐ 40 · Lua · MIT · 推送 2026-08-24 · [GitHub](https://github.com/ds-kimi/Auris) · [官网](https://discord.gg/tnYU8DnkCe) · 个人维护

**Garry's Mod 服务器实时语音转文字模块（whisper.cpp）**

GMod 服务端二进制模块：通过进程内 SV_BroadcastVoiceData detour 捕获玩家语音，解码 Opus 音频后用 whisper.cpp 实时转录。默认本地后端离线运行需下载 ggml 模型文件；也可配置 OpenAI API key 切换远程转录后端。转录结果通过 Auris_Transcription 钩子（含玩家、SteamID64、文本、PCM 音频）分发给子模块插件，本体不决定用途。Windows 下用 premake5 生成 VS 工程编译构建。

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

- SV_BroadcastVoiceData detour 捕获并解码 Opus 语音
- 本地 whisper.cpp 与远程 OpenAI 双转录后端，钩子接口一致
- Auris_Transcription 钩子 API 向任意插件分发转录结果
- ConVar 运行时覆盖配置（语言/线程数等）

## 适用场景

- 为 GMod 服务器接入实时语音转文字能力
- 配合子模块做聊天字幕、Discord 转发或控制台日志
- 离线私有部署语音转录，不依赖外部 API

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L14: Captures player voice chat via an in-process `SV_BroadcastVoiceData` detour, decodes Opus audio, and transcribes it
> L74: |**Local (whisper.cpp)**|`openai_api_key = ""` (default)|Private, offline, no per-clip cost; uses server CPU/GPU an

## 星数曲线

```mermaid
xychart-beta
    title "ds-kimi/Auris 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f96cc7fb4ba8` · [字段定义](../../DATASET.md)*
