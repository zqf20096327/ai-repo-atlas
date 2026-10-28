# EnArvy/Discord-Gemini-Chatbot

⭐ 34 · Python · GPL-3.0 · 推送 2026-01-03 · [GitHub](https://github.com/EnArvy/Discord-Gemini-Chatbot) · 个人维护

**接入 Gemini API 的 Discord 聊天机器人**

基于 Python discord-py 的 Discord 聊天机器人，调用 Google Gemini API 生成回复，支持图片、音频、文档输入与 Gemini 1.5。用户可通过 @ 提及或私信与机器人对话，每个频道/线程拥有独立上下文，可用 /forget 清除历史并可指定 persona。因 API 限制无法记住图片交互。需自备 Gemini API key 与 Discord bot token，通过克隆仓库、安装 requirements.txt 依赖并以 python main.py 运行；支持自定义对话模板、安全设置与生成参数，聊天数据用 shelve 持久化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Gemini API 生成回复，支持图片/音频/文档输入
- 每频道/线程独立上下文，/forget 清除并支持 persona
- 可配置对话模板、内容安全设置与生成参数
- 聊天数据跨运行持久化（shelve）

## 适用场景

- 在 Discord 服务器里 @ 或私信与 Gemini 对话
- 让机器人处理带图片、音频或文档的提问
- 按频道维护独立对话上下文并可随时重置

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L1: # Discord Bot to interact with Gemini API as ChatBot
> L9: This bot acts as a Chatbot. It uses Google's Gemini API which is free for upto 60 calls/min as of Jan 2023.

## 星数曲线

```mermaid
xychart-beta
    title "EnArvy/Discord-Gemini-Chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0ed319bca757` · [字段定义](../../DATASET.md)*
