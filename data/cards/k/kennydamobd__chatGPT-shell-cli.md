# kennydamobd/chatGPT-shell-cli

⭐ 50 · Shell · MIT · 推送 2026-11-05 · [GitHub](https://github.com/kennydamobd/chatGPT-shell-cli) · 个人维护

**终端调用 OpenAI 聊天与 DALL-E 图像生成的 shell 脚本**

用 bash 编写的轻量命令行脚本，通过 curl 调用 OpenAI API（/chat/completions 与 images/generations 端点），无需安装 Python 或 Node.js。支持聊天模式、管道与脚本参数输入、聊天历史与上下文、列出模型、设置 temperature/max-tokens 等请求参数，并可用 command: 前缀生成并在终端执行命令（执行前确认）。默认模型 gpt-3.5-turbo，可切换 gpt-4 及其他 OpenAI 模型。需自备 curl、jq 与 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 终端内与 ChatGPT 模型对话及 DALL-E 文生图
- 管道、脚本参数、交互聊天三种输入方式
- command: 前缀生成命令并在终端执行（执行前询问）
- 可设置初始角色提示词与请求参数（temperature/model/max-tokens/图像尺寸）

## 适用场景

- 在终端直接向 ChatGPT 提问或生成图片
- 通过管道把文本送入模型处理并取回结果
- 让模型生成 shell 命令并确认后执行

## 场景标签

`聊天机器人` `AI 助手` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L3: A simple, lightweight shell script to use OpenAI's chatGPT and DALL-E from the terminal without installing python or
> L8: - Chat with the ✨ official ChatGPT API ✨ from the terminal
> L9: - Generate images from a text prompt

## 星数曲线

```mermaid
xychart-beta
    title "kennydamobd/chatGPT-shell-cli 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-18"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-11-08 50 → 2026-11-18 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `42958a239d94` · [字段定义](../../DATASET.md)*
