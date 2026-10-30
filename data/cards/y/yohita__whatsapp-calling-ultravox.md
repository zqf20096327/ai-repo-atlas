# yohita/whatsapp-calling-ultravox

⭐ 16 · HTML · 推送 2025-12-25 · [GitHub](https://github.com/yohita/whatsapp-calling-ultravox) · [官网](https://www.youtube.com/watch?v=4DWiJec8LFo) · 个人维护

**WhatsApp 语音通话接入 AI 语音代理的示例代码与教程**

提供 Node.js 示例服务器，演示通过 WhatsApp Business Voice Calling API 实现两类来电处理：转接人工坐席（server.js）与转接 Ultravox AI 语音代理（server-ultravox.js）。面向开发者的教学仓库，附带 YouTube 视频教程，配置流程覆盖 Meta 应用与 Webhook 设置、ngrok 隧道、环境变量；文档说明印度市场的免费来电与免 TRAI 注册事项，并列出 WhatsApp 通话频次限制（7 天窗口、15 天内最多 2 次回呼）。AI 功能依赖 Ultravox API key，为可选配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Node.js 服务器示例：人工坐席与 Ultravox AI 语音代理两种模式
- 配置流程覆盖 Meta 应用、Webhook、ngrok 隧道与环境变量
- 文档化 WhatsApp 通话政策限制（用户许可、7 天窗口、回呼上限）
- 配套 YouTube 分步视频教程

## 适用场景

- 我想让 AI 语音代理接听 WhatsApp Business 来电
- 我在印度做业务，想免虚拟号码接听 WhatsApp 语音来电
- 我想把现有 VoIP 呼叫中心经 SIP 中继接入 WhatsApp 语音

## 场景标签

`语音 Agent` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L14: This repository contains **working sample code** for integrating WhatsApp Business Voice Calling API with both huma
> L19: - **AI voice agent integration** - Using Ultravox AI for intelligent call handling

## 星数曲线

```mermaid
xychart-beta
    title "yohita/whatsapp-calling-ultravox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5883f496231f` · [字段定义](../../DATASET.md)*
