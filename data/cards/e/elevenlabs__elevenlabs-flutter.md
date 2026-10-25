# elevenlabs/elevenlabs-flutter

⭐ 39 · Dart · MIT · 推送 2026-06-02 · [GitHub](https://github.com/elevenlabs/elevenlabs-flutter) · [官网](https://elevenlabs.io) · 组织维护

**ElevenLabs 官方 Flutter SDK：构建实时语音对话应用**

ElevenLabs 官方发布的 Flutter/Dart SDK（elevenlabs_agents），用于接入 ElevenAgents 平台构建语音应用。基于 WebRTC（LiveKit 基础设施）实现全双工实时音频流，支持会话中发送文本消息与上下文更新、注册客户端工具供 agent 调用、会话级配置覆盖、agent 回应点赞/点踩反馈、自定义 API 端点与区域部署（数据驻留）。ConversationClient 继承 ChangeNotifier 提供 Flutter 响应式状态管理。私有 agent 需后端生成会话令牌（依赖 ElevenLabs API key，不得在客户端暴露）。支持 Android（API 21+）与 iOS（13.0+），需配置麦克风权限。

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

- WebRTC（LiveKit）全双工实时语音流
- 客户端工具注册：agent 可调用设备端函数（如定位）并回传结果
- 支持自定义 API 端点与区域部署（数据驻留）
- 基于 ChangeNotifier 的响应式状态管理与全事件回调

## 适用场景

- 在 Flutter 应用中接入 ElevenAgents 做实时语音对话
- 让 agent 调用设备端能力（定位、相机等客户端工具）
- 需要区域数据驻留的企业部署场景

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L8: Official Flutter SDK for ElevenAgents. Build voice-enabled applications with real-time bidirectional audio communica
> L14: - **Client Tools** - Register device-side functions that agents can invoke

## 星数曲线

```mermaid
xychart-beta
    title "elevenlabs/elevenlabs-flutter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4426f928aa9c` · [字段定义](../../DATASET.md)*
