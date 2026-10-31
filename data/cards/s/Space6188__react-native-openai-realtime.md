# Space6188/react-native-openai-realtime

⭐ 27 · TypeScript · MIT · 推送 2026-01-23 · [GitHub](https://github.com/Space6188/react-native-openai-realtime) · 个人维护

**React Native 中接入 OpenAI Realtime 语音/文本聊天的库**

面向 React Native 开发者的库，封装与 OpenAI Realtime API 的 WebRTC 连接：处理 SDP 交换、DataChannel、本地/远程音频流、事件路由、内置 VAD 与音频转录、function calling 工具调用及内置聊天存储。提供 React Provider 组件、useRealtime 等钩子与命令式 ref API，支持 middleware 拦截事件与并发调用保护。需要开发者自行搭建返回临时令牌的服务端；限制：不支持运行中动态重新协商 SDP 以切换文本/语音模式，需在初始会话配置中启用 VAD 与转录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 WebRTC + DataChannel 与 OpenAI Realtime 的连接全流程
- 内置 ChatStore 消息流构建与 incoming/outgoing middleware
- 支持 VAD（turn_detection）、音频转录、function calling 工具
- 提供 React Provider、useRealtime/useSpeechActivity 等钩子与命令式 ref API

## 适用场景

- 在 React Native 应用中构建 OpenAI Realtime 语音助手
- 实现带实时转录与工具调用的文本/语音聊天界面
- 通过 middleware 定制实时事件的处理逻辑

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: **Библиотека - готовый каркас для голосового/текстового чата с OpenAI Realtime (WebRTC + DataChannel) в React Native
> L62: Библиотека делает за вас всю «тяжелую» работу по Realtime с OpenAI: WebRTC-подключение, SDP-обмен, DataChannel, лок
> L97: - **RealTimeClient** — React-провайдер. Создаёт RealtimeClientClass, подписывается на статусы, создаёт встроенный ч

## 星数曲线

```mermaid
xychart-beta
    title "Space6188/react-native-openai-realtime 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5cc1f1e424af` · [字段定义](../../DATASET.md)*
