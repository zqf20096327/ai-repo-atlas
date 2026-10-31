# jimpames/rentahal

⭐ 23 · Python · NOASSERTION · 推送 2026-09-01 · [GitHub](https://github.com/jimpames/rentahal) · [官网](https://rentahal.com) · 个人维护

**面向 Ollama 的多用户语音 Web 前端与 AI 应用平台**

RENT-A-HAL（MTOR）是以语音为主要交互方式的本地 AI 前端与编排平台：通过 Web 界面（localhost:9100）与语音输入输出进行 AI 对话、视觉识别（LLAVA）与图像生成（Stable Diffusion），后端支持 Ollama/Llama 原生 FastAPI 通道及 Claude、HuggingFace API。设计为事件驱动、无状态的'AI 操作域'，可由多个后端工作节点组成，另有 Kokoro TTS 微服务安装器与联邦多用户模式。Windows 二进制安装包未签名，源码 GPL3 且声明商业使用需另行获得许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音输入/输出 + Web 界面访问 Ollama 后端的 AI 对话、视觉与图像生成
- Ollama/Llama 走原生 FastAPI 通道，另支持 Claude API、HuggingFace API、Stable Diffusion API
- 多节点后端编排（stable diffusion 节点、realm 编排器、chat/vision 节点）
- 附带 Kokoro TTS 微服务安装器与联邦多用户模式

## 适用场景

- 在本机或小办公网络用语音与本地 AI 模型对话
- 通过统一 Web 界面同时使用对话、视觉识别与图像生成
- 搭建多用户、多后端节点的本地 AI 服务

## 场景标签

`语音 Agent` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L179: An Open-Source Speech-Enabled Web gui For Ollama
> L185: - Ollama - native fastapi()
> L43: supports AI chat (gpt4all,claude,many others) , AI vision (LLAVA via Ollama) and AI imagine (automatic1111, stable 

## 星数曲线

```mermaid
xychart-beta
    title "jimpames/rentahal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `86b5728b93c6` · [字段定义](../../DATASET.md)*
