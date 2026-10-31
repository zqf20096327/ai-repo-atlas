# FlineDev/IntelligenceKit

⭐ 15 · Swift · MIT · 推送 2026-02-17 · [GitHub](https://github.com/FlineDev/IntelligenceKit) · 个人维护

**Swift 开发者接入 OpenAI API 的跨平台 SDK**

面向 Swift 开发者的 OpenAI API 集成库，以 Swift Package 形式提供，支持 iOS 18+/macOS 15+ 等 Apple 平台与 Linux 服务端。覆盖 GPT-5 系列（含 reasoning 努力等级）、GPT-4.1/o3/o4-mini 等模型，提供 Responses API、JSON Schema 结构化输出、多轮对话状态管理、DALL-E 图像生成、类型化错误处理与 token 用量及成本追踪。依赖 HandySwift 与 ErrorKit，由作者从其多个 Indie 应用中抽取而来。

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

- GPT-5/GPT-5-mini/GPT-5-nano 支持，含 4 档 reasoning 努力等级
- JSON Schema 结构化输出与多轮对话状态管理
- 内置 token 用量统计与成本追踪
- Apple 平台与 Linux 服务端共用同一 API

## 适用场景

- 在 iOS/macOS 应用中接入 OpenAI 模型生成文本
- 服务端 Swift 应用调用 GPT-5 完成推理任务
- 从 GPT-4.1/o3 等旧模型迁移到 GPT-5 系列

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L3: Unified Swift package for OpenAI API integration with GPT-5 support and advanced reasoning capabilities.
> L12: - **OpenAI GPT-5 family**: GPT-5, GPT-5-mini, GPT-5-nano with reasoning capabilities
> L16: - **Cross-platform compatibility**: Apple platforms + Linux server support

## 星数曲线

```mermaid
xychart-beta
    title "FlineDev/IntelligenceKit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `983893de24bb` · [字段定义](../../DATASET.md)*
