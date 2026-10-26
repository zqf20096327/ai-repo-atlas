# Leask/halbot

⭐ 103 · JavaScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/Leask/halbot) · [官网](https://leaskh.com/2023/03/13/halbot/) · 个人维护

**AI 驱动的 Telegram 机器人，接入多种模型提供对话与多模态能力**

面向 Telegram 用户的 Node.js AI 机器人：聚焦 OpenAI 风格 API 接入，推荐通过 OpenRouter 获取多模型访问，也支持 OpenAI API Key 与本地 Ollama。功能包括对话、语音转文字、文字转语音、图像与视频生成、OCR/物体检测、DeepSearch（需 Google API Key）、网页与 YouTube 内容注入提示词、函数调用工具、多模态输入输出与流式响应。采用中间件式工作流便于扩展，支持私人与公开模式及多种认证方式。可通过 npx 直接运行或作为 npm 包集成到项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚焦 OpenAI 风格 API，推荐 OpenRouter 多模型访问
- 支持语音转文字、文字转语音、图像/视频生成、OCR/物体检测
- 中间件式工作流，可注入网页/YouTube/PDF/Office 文档到提示词
- npx halbot 一条命令运行，流式实时响应

## 适用场景

- 在 Telegram 里与多种 AI 模型对话并处理图文音视频
- 通过本地 Ollama 运行私有模型供 Telegram 使用
- 把网页、YouTube 视频、PDF 等资料喂给 AI 增强回答

## 场景标签

`聊天机器人` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L6: Just another AI powered Telegram bot, which is simple design, easy to use, extendable and fun.
> L28: - Telegram Bot (`Telegram Bot` token required)

## 星数曲线

```mermaid
xychart-beta
    title "Leask/halbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-26 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f412c6854c5a` · [字段定义](../../DATASET.md)*
