# seehiong/voicedoc-agent

⭐ 34 · TypeScript · MIT · 推送 2025-12-27 · [GitHub](https://github.com/seehiong/voicedoc-agent) · [官网](https://seehiong.github.io/posts/2025/12/voice-native-document-intelligence/) · 个人维护

**用语音与文档对话的 agent：Gemini 推理 + ElevenLabs 实时语音**

为 AI Partner Catalyst 黑客松构建的语音文档对话应用：用户上传单个文本文档，通过语音全程交互。上传时自动分类文档类型（法律/金融/技术/学术等），ElevenLabs 语音 agent 据此调整语气与节奏；Gemini on Vertex AI 负责分类、推理与对话，Vertex AI Embeddings 加 Firestore 做检索。提供标准/表达双模式（后者两步生成注入情感标签）。以 Datadog HTTPS API 做 LLM 可观测性（延迟/token/成本指标、监控规则）。本地运行需 Node.js 并配置 Google Cloud 服务账号、ElevenLabs 与 Datadog API key，部署面向 Google Cloud Run。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档类型自动分类并驱动语气自适应的语音人设
- 标准/表达双模式，表达模式两步生成注入 [excited] 等情感标签
- Gemini 推理 + Vertex AI Embeddings 检索的单文档深度问答
- 通过 Datadog HTTPS API 发送延迟/token/成本等 LLM 遥测并配监控规则

## 适用场景

- 上传合同或报告后用语音提问，获取口头简报
- 开车或免打字场景下听 AI 讲解文档内容
- 演示 Google Cloud + ElevenLabs + Datadog 的组合架构

## 场景标签

`语音 Agent` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L5: VoiceDoc Agent transforms static documents into *living conversations*. Built on **Google Cloud’s partner ecosystem*
> L53: Users can interact naturally using speech:

## 星数曲线

```mermaid
xychart-beta
    title "seehiong/voicedoc-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 33 --> 36
    line [35, 34, 34]
```

2026-10-18 35 → 2026-10-27 34（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `59930fe14444` · [字段定义](../../DATASET.md)*
