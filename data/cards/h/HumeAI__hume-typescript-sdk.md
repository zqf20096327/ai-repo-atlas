# HumeAI/hume-typescript-sdk

⭐ 84 · TypeScript · MIT · 推送 2026-08-18 · [GitHub](https://github.com/HumeAI/hume-typescript-sdk) · [官网](https://hume.ai) · 组织维护

**Hume AI 官方 TypeScript SDK，接入共情语音与 TTS API**

面向 Node 应用与前端项目的 Hume AI API 客户端 SDK，以 npm 包 hume 分发。覆盖 Empathic Voice（共情语音）与 text-to-speech 两类 API，各按命名空间组织；支持 WebSocket 与 REST 两种交互方式，可发送与接收音频。内置错误处理（HumeError/HumeTimeoutError）、对 409/429/5xx 的两次指数退避重试（maxRetries 可配）及默认 60 秒超时（timeoutInSeconds 可配）。官方声明 SDK 处于 beta，版本间可能出现非大版本号的破坏性变更，建议锁定包版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖 Empathic Voice 与 text-to-speech API，命名空间组织
- 支持 WebSocket 与 REST 两种交互方式
- 内置指数退避重试（两次）与可配置超时（默认 60s）
- HumeError/HumeTimeoutError 错误类型体系

## 适用场景

- 在 Node 或前端项目中集成 Hume 共情语音接口
- 通过 WebSocket 收发音频实现语音助手
- 调用 TTS API 并控制重试与超时行为

## 场景标签

`语音 Agent` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3:  Integrate Hume APIs directly into your Node application or frontend
> L29: This SDK contains the APIs for empathic voice and text-to-speech. Even

## 星数曲线

```mermaid
xychart-beta
    title "HumeAI/hume-typescript-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-24 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c77876c51532` · [字段定义](../../DATASET.md)*
