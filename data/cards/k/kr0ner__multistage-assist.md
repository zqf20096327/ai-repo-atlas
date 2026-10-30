# kr0ner/multistage-assist

⭐ 16 · Python · NOASSERTION · 推送 2026-04-10 · [GitHub](https://github.com/kr0ner/multistage-assist) · [官网](https://github.com/kr0ner/multistage-assist) · 个人维护

**给 Home Assistant 用户的多级本地语音/对话助手集成**

Home Assistant 自定义集成，通过四个处理阶段编排对话代理：Stage 0 使用 HA 内置 NLU 快速路径，Stage 1 做语义缓存命中回放，Stage 2 调用本地 Ollama（qwen3:4b-q4_K_M）识别意图，Stage 3 回退到 Google Gemini 云端并支持聊天。提供语义命令缓存、自定义房间/设备名记忆、临时控制（如开灯 10 分钟）、德语优化与容错。需 Home Assistant 2024.1.0+、Ollama 与 Gemini API Key，通过 HACS 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四级流水线：内置 NLU 快路径 + 语义缓存 + 本地 Ollama 意图 + Gemini 云端回退
- 语义命令缓存支持即时重放已学命令
- 记忆用户自定义房间与设备命名
- 本地优先运行，不强依赖高配硬件

## 适用场景

- 在 Home Assistant 中用自然语言控制家里设备
- 网络或云端不可用时仍保持本地语音助手可用
- 让助手记住我给房间和设备起的自定义名字

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L7: **Multi-Stage Assist** is a highly advanced, local-first (with cloud fallback) conversational agent for Home Assista
> L13: |Stage|Purpose|Technology|
> L17: |**Stage 2**|Local LLM intent|Ollama (qwen3:4b-q4_K_M)|

## 星数曲线

```mermaid
xychart-beta
    title "kr0ner/multistage-assist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0066626ac408` · [字段定义](../../DATASET.md)*
