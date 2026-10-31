# Senzo13/JoyBoy

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Senzo13/JoyBoy) · [官网](https://github.com/Senzo13/JoyBoy) · 个人维护

**本地优先 AI 工作站：聊天/生图/修图/视频一站操作**

面向终端用户的一体化本地 AI 工作站：通过 Ollama 运行本地聊天模型，提供图像生成、画笔遮罩修图/外扩/放大、图生视频与视频续写、模型管理、画廊、依赖体检（Doctor）与引导流程。默认无需云端账号，密钥可选，支持 OpenAI/OpenRouter/DeepSeek 等云 provider 及 MCP 连接器、Browser Use、本地私有扩展包。按平台脚本启动，浏览器访问 127.0.0.1:7860，覆盖 8GB 显存到 A100 级的 GPU 配置档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama 本地聊天、模型切换与运行时内存卸载
- SDXL/Flux 风格图像生成与画笔遮罩修图、外扩、放大
- 图生视频/视频续写，GPU 档位（8GB/24GB/40GB）适配
- MCP 连接器、Browser Use 与本地扩展包机制

## 适用场景

- 在本机私有化跑聊天、生图与修图全流程
- 8GB 显存消费级显卡上做 Stable Diffusion 生成与局部重绘
- 通过 MCP 连接 GitHub、数据库等外部工具扩展工作流
- SSH 隧道连远端 GPU 机器私有使用

## 场景标签

`AI 助手` `图像生成` `视频生成` · 领域:对话与助手

## 证据(README 行号)

> L3: **JoyBoy is a local-first AI workstation for chat, coding, image generation, image editing, video experiments, model
> L17: - **Chat** with local Ollama models or optional cloud providers.
> L20: - **Image editing and inpainting** with brush masks, quick prompts, outpaint/expand, upscale, and before/after view

## 星数曲线

```mermaid
xychart-beta
    title "Senzo13/JoyBoy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [20, 19, 19]
```

2026-10-18 20 → 2026-10-31 19（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `195543334b6e` · [字段定义](../../DATASET.md)*
