# kamalesh404/ai-studio

⭐ 14 · TypeScript · MIT · 推送 2026-06-11 · [GitHub](https://github.com/kamalesh404/ai-studio) · 个人维护

**本地 AI 应用平台：聊天、生图、图生视频，先跑 mock 再接真模型**

Next.js + Tailwind 前端配 FastAPI 网关的应用，提供流式聊天、扩散模型生图、图生视频与双图插值（FILM/RIFE 风格）。开箱即在 mock 模式本地运行，无需下载模型；通过 .env.local 配置端点切换到真实开源模型，上游失败时自动回退 mock。推荐 Qwen2.5、Llama-3.1、SDXL 等本地模型栈，并提供 Google Colab 免 GPU 部署 notebook（FastAPI 网关 + Cloudflare Tunnel）。MIT 许可，路线图中认证、Whisper 语音转文字与提示词库尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mock 模式开箱即跑，配置环境变量切换真实开源模型
- 聊天/生图/图生视频/双图插值四类能力与动态模型切换
- Google Colab 一键部署 notebook（FastAPI 网关 + Cloudflare Tunnel）
- 上游模型失败或超时时自动回退 mock 响应

## 适用场景

- 不下载模型先预览 AI 应用界面与交互
- 本地或 Colab 上接入 Qwen/SDXL 等开源模型做原型开发
- 没有 GPU 时用 Colab 免费跑聊天与生图

## 场景标签

`聊天机器人` `图像生成` `视频生成` · 领域:对话与助手

## 证据(README 行号)

> L12: A modern, responsive Next.js application that runs instantly in **mock mode** and seamlessly scales to use **real o
> L16: - 💬 **Interactive Chat:** High-performance chat interface with real-time streaming output.
> L17: - 🎨 **Image Generation:** Create stunning visuals using top-tier diffusion models.

## 星数曲线

```mermaid
xychart-beta
    title "kamalesh404/ai-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `cd578089b977` · [字段定义](../../DATASET.md)*
