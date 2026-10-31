# AndraxDev/speak-gpt-web

⭐ 33 · JavaScript · 推送 2026-10-14 · [GitHub](https://github.com/AndraxDev/speak-gpt-web) · [官网](https://assistant.teslasoft.org) · 个人维护

**基于 ReactJS 的开源网页版 AI 聊天助手（SpeakGPT Web）**

SpeakGPT 的 Web/桌面版本，用 ReactJS 与 Material Design 3 构建，作为本科论文成果发布。面向终端用户提供聊天、DALL·E 图像生成、GPT-4 Vision、系统消息、提示词商店、Playground、AI 照片编辑等功能；除 OpenAI API 外，通过 OpenRouter 支持 LLaMA、Gemini、Mistral、Perplexity、Claude 等模型，并支持自定义 API 端点与微调模型。API key 存储在本地设备，提供 iframe 嵌入式助手（payload 定制名称/图标/初始消息）与 Chrome 扩展目录。署名使用要求，版权归作者所有。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天、DALL·E 图像生成、GPT-4 Vision、Playground、AI 照片编辑
- 通过 OpenRouter 支持 LLaMA/Gemini/Mistral/Claude 等多家模型，支持自定义 API 端点
- iframe 嵌入式助手，可用 base64 payload 定制
- API key 本地存储，不收集个人数据

## 适用场景

- 在浏览器中使用自己的 API key 与多种模型对话
- 把 AI 助手嵌入自己的网站或应用
- 在网页端生成图像与编辑照片

## 场景标签

`聊天机器人` `AI 助手` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L23: - [x] Chat
> L24: - [x] Images generation (DALL-e)
> L36: - [x] Supported models from OpenRouter like LLama, Gemini, Mistral, Perplexity, Claude and more

## 星数曲线

```mermaid
xychart-beta
    title "AndraxDev/speak-gpt-web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2799609a0828` · [字段定义](../../DATASET.md)*
