# rishabkumar7/twilio-cr-gemini-python

⭐ 32 · Python · 推送 2026-02-19 · [GitHub](https://github.com/rishabkumar7/twilio-cr-gemini-python) · 个人维护

**用 Twilio 电话与 Gemini API 实现双向语音对话的 AI 助手**

Python/FastAPI 应用：拨打 Twilio 号号后，经 ConversationRelay 建立 WebSocket 连接，Twilio 转写用户语音为文本，服务端调用 Google Gemini（gemini-2.5-flash）生成回复，再由 Twilio 内置 TTS 播放，实现电话两轮对话。运行需 Python 3.10+、Twilio 账号与号码、Google AI API key，并通过 ngrok 暴露本地 8080 端口。安装方式为 git clone 源码加 pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Twilio ConversationRelay 的 WebSocket 双向通话
- 调用 Gemini gemini-2.5-flash 生成对话回复
- FastAPI 服务端处理 /twiml 与 /ws 端点
- 使用 Twilio 内置 TTS 播放回复

## 适用场景

- 搭建可拨打电话咨询的 AI 语音助手
- 学习 Twilio ConversationRelay 与 Gemini API 的集成方式
- 为业务电话线路接入 AI 自动应答

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L7: This application allows users to call a Twilio number and interact with an AI assistant powered by Google's `gemini-
> L65: 4. The server sends the transcribed text to the **Google Gemini API** and gets a response.

## 星数曲线

```mermaid
xychart-beta
    title "rishabkumar7/twilio-cr-gemini-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1336be160c5c` · [字段定义](../../DATASET.md)*
