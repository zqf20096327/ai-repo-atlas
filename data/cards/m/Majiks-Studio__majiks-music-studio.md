# Majiks-Studio/majiks-music-studio

⭐ 15 · Swift · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/Majiks-Studio/majiks-music-studio) · [官网](https://majiks.studio) · 组织维护

**macOS 本地 AI 音乐生成 DAW：文本生成多轨歌曲并可编曲混音**

面向音乐创作者的开源 macOS 桌面应用：用 ACE-Step 1.5（MLX + Metal）在 Apple Silicon 本地从文本生成完整多轨歌曲，落到时间线为小节对齐的分轨，并支持 revise/extend/layer/cover 等生成式时间线操作。内含完整 DAW 功能（Rust 实时音频引擎、混音器、自动化、LUFS 母带表、录音与分轨分离），以及应用内 AI 制作人 Sterling 与 localhost MCP 服务器（148 个工具）供外部 AI agent 驱动；编辑经哈希链日志记录并可溯源导出。限制：无 VST/AU/CLAP 插件宿主，无 MP3 导出。架构为 SwiftUI 前端 + Rust 引擎 + Python 生成后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ACE-Step 1.5 本地文本生成多轨歌曲（Apple Silicon MLX + Metal）
- 148 工具的 localhost MCP 服务器，外部 AI agent 可驱动项目
- 哈希链日志构成撤销栈，逐剪辑溯源与导出清单
- Sterling 应用内 copilot 与 UI 走同一命令总线，编辑可撤销可归因

## 适用场景

- 在本地用一句话生成完整多轨歌曲并继续编曲混音
- 让应用内 AI 制作人 Sterling 或外部 agent 按自然语言编曲、混音、导出
- 在 DAW 内做 revise/extend/layer/cover 等生成式剪辑操作

## 场景标签

 · 领域:音乐生成/音频制作

## 证据(README 行号)

> L25: - 🎼 **Music from a sentence — on your machine.** Describe a track and **ACE-Step 1.5** generates a full song locall
> L7: **A macOS DAW built around three ideas the others aren't: music you _generate_ on your own machine, a studio an _AI 

## 星数曲线

```mermaid
xychart-beta
    title "Majiks-Studio/majiks-music-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `48d8c9b05baf` · [字段定义](../../DATASET.md)*
