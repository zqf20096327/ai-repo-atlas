# timmyy123/LLM-Hub

⭐ 667 · C · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/timmyy123/LLM-Hub) · [官网](https://llm-hub.app) · 个人维护

**本地运行 LLM 与图像/视频/音乐生成的多端应用**

开源应用，在 Android/iOS 及 Windows/macOS/Linux（LLM Hub Desktop）上本地运行模型：多轮对话（RAG 记忆、联网搜索、TTS、多模态输入）、Stable Diffusion 文生图、LTX-Video/Stable Video Diffusion 文生视频、Magenta Realtime 2/SoundGen 音乐生成、Whisper 转写、离线翻译等 16 个工具。桌面版可运行 Claude Code 与 Codex 于本地模型，并提供 OpenAI/Anthropic 兼容 API。全部推理在设备端完成，无账号与云端；应用自带修补版 llama.cpp 预编译库，支持 Hexagon NPU、Vulkan、Metal 等后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天/图像/视频/音乐/转写等 16 个本地 AI 工具
- AI Agent 支持设备功能调用与 MCP 工具，可起草并编辑 Termux shell 命令
- 自带修补版 llama.cpp，覆盖 Snapdragon NPU/Vulkan/Metal 后端
- 100% 设备端推理，无账号、无数据收集

## 适用场景

- 手机上离线使用本地模型聊天和生成图像视频
- 在设备端用本地模型运行 Claude Code 或 Codex 写应用
- 对相册照片和视频做本地语义搜索
- 对隐私敏感的用户在本地转写语音和翻译

## 场景标签

`聊天机器人` `图像生成` `视频生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: **LLM Hub** is an open-source mobile app for on-device LLM chat, image generation, video generation, and music gener
> L105: - **100% on-device processing** - no internet required for inference
> L118: ### LLM Hub's patched llama.cpp (Aion, flash streaming, NPU/GPU fixes)

## 星数曲线

```mermaid
xychart-beta
    title "timmyy123/LLM-Hub 星数(近 23 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 617 --> 671
    line [621, 622, 623, 624, 627, 628, 629, 622, 638, 641, 643, 646, 647, 651, 654, 656, 658, 659, 661, 663, 665, 667, 667]
```

2026-10-23 621 → 2026-11-25 667（+46）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `ee5692bb84e3` · [字段定义](../../DATASET.md)*
