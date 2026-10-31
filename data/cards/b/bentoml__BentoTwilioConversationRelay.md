# bentoml/BentoTwilioConversationRelay

⭐ 14 · Python · 推送 2026-07-14 · [GitHub](https://github.com/bentoml/BentoTwilioConversationRelay) · 组织维护

**BentoML+Twilio 构建开源 LLM 语音聊天机器人的示例项目**

演示如何用 Twilio 与 BentoML 搭建语音聊天机器人：Twilio 负责语音传输、STT/TTS 与打断检测，BentoML 服务处理文本输入并以生产者-消费者模式流式返回 LLM 响应，使用 vLLM 异步引擎以降低延迟并支持取消流。默认使用 Llama-3.1-70B-Instruct，暴露 /chat/start_call 与 /chat/ws 两个端点。面向希望在电话语音场景部署开源 LLM 的开发者，支持扩展 RAG，可部署到 BentoCloud。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Twilio 双向 WebSocket 实时语音流（/chat/ws）
- vLLM 异步引擎流式输出并支持打断取消
- 维护一致的消息历史
- 提供 BentoCloud 部署与 OCI 镜像导出路径

## 适用场景

- 搭建电话语音 LLM 聊天机器人
- 参考 BentoML 流式 LLM 服务的实现模式
- 基于此示例扩展 RAG 等功能

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: This repository demonstrates how to build a voice chatbot using an open-source Large Language Model (LLM). It levera
> L5: This example uses the Llama-3.1-70B-Instruct model. It is designed to be customizable and you can extend it by addin

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/BentoTwilioConversationRelay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8aa7fe9bb7f3` · [字段定义](../../DATASET.md)*
