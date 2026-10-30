# PreternaturalAI/AI

⭐ 230 · Swift · MIT · 推送 2026-03-05 · [GitHub](https://github.com/PreternaturalAI/AI) · [官网](https://preternatural.ai) · 组织维护

**Swift 开发者接入生成式 AI 的开源框架**

面向 Apple 平台开发者的 Swift 框架，通过协议导向的抽象层统一接入多家 AI API 提供商（OpenAI、Anthropic、ElevenLabs 等）：提供 LLM 客户端抽象（LLMRequestHandling）、对话补全、图像理解（Vision）、函数调用、DALLE-3 文生图、Whisper 语音转录、TTS 语音生成与文本嵌入等接口。通过 Swift Package Manager 在 Xcode 中添加安装。README 声明当前处于 alpha 开发阶段（2026-03-04），MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 客户端协议抽象，可让用户在多家提供商间选择
- 覆盖补全、视觉理解、函数调用、文生图、语音转录/生成、文本嵌入
- 支持 OpenAI、Anthropic、ElevenLabs 等提供商接入
- 通过 Swift Package Manager 集成进 Xcode 项目

## 适用场景

- 在 macOS/iOS 应用中统一封装多家 LLM API 调用
- 为 App 添加语音转录、TTS 或图像生成功能
- 利用函数调用让 LLM 返回结构化 JSON 以驱动应用逻辑

## 场景标签

`模型网关` `图像生成` `语音合成` `语音识别` · 领域:Agent 开发

## 证据(README 行号)

> L22: The definitive, open-source Swift framework for interfacing with generative AI.
> L64: ## LLM Clients Abstraction
> L75: ## Supported Models

## 星数曲线

```mermaid
xychart-beta
    title "PreternaturalAI/AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 229 --> 231
    line [230, 230]
```

2026-10-18 230 → 2026-10-30 230（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fd27e646817e` · [字段定义](../../DATASET.md)*
