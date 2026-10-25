# TristanBrotherton/openclaw-voice-call-realtime

⭐ 105 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/TristanBrotherton/openclaw-voice-call-realtime) · 个人维护

**给 OpenClaw 助手装上电话：经 Twilio+OpenAI Realtime 真人通话**

OpenClaw 插件，在网关内运行 HTTP 服务器，将 Twilio 媒体流的音频桥接到 OpenAI Realtime 会话，让 AI 助手拨打和接听真实电话并进行全双工语音对话。通话中可自主按键过 IVR、调用日历/家居/转发给主人等工具、产出结构化结果与 Markdown 转写。需要 OpenClaw ≥ 2026.6、Twilio 付费账户、OpenAI Realtime API 密钥和公网 HTTPS webhook（Cloudflare Tunnel/ngrok）。

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

- Twilio Media Streams 桥接 OpenAI Realtime，语音到语音单循环（STT+推理+TTS）
- 通话中工具：DTMF 按键、结果捕获、ask_assistant 中途问答、转接真人
- 每通电话生成 Markdown 转写与 AI 摘要，支持可选录音与答录机检测
- 入站呼叫有白名单、SHAKEN/STIR 验证与口令短语校验

## 适用场景

- 让助手打电话订餐厅、预约并确认细节
- 电话查询营业时间、库存、价格等信息
- 需要实时决策时助手直接打给我本人对话
- 允许名单内来电者直接呼入与我的助手对话

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: This OpenClaw plugin lets your assistant place and receive real phone calls and hold natural, full-duplex voice conv
> L64: The plugin runs an HTTP server inside the OpenClaw gateway. Twilio fetches TwiML from it and opens a bidirectional 

## 星数曲线

```mermaid
xychart-beta
    title "TristanBrotherton/openclaw-voice-call-realtime 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-25 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3c757d4cc64c` · [字段定义](../../DATASET.md)*
