# Rayyan9477/Solace-AI

⭐ 21 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Rayyan9477/Solace-AI) · 个人维护

**面向用户的共情式心理健康 AI 陪伴应用**

一个心理健康陪伴型对话应用：用户通过文本或语音与其对话，系统经由多 Agent 架构（情绪、安全、治疗、人格、诊断等 Agent，LLM 底座为 Google Gemini）生成个性化回应。功能包括文本与语音情绪识别（Whisper V3 Turbo ASR）、Big Five/MBTI 人格评估适配、CBT 等循证治疗技术整合、GAD-7/PHQ-9/PSS 心理筛查、危机检测干预、向量记忆（ChromaDB）以及名人声音克隆。以 Python 源码与 Docker 提供，含 Streamlit 界面、CLI 与 REST API 服务器。

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

- 多 Agent 编排架构（情绪/安全/治疗/人格/诊断 Agent），底座为 Google Gemini
- 文本与语音情绪识别，Whisper V3 Turbo ASR 支持 40+ 语言
- 整合 GAD-7/PHQ-9/PSS 筛查与 CBT、正念等循证治疗技术
- 向量数据库语义记忆，支持跨会话上下文

## 适用场景

- 通过文字或语音对话获得情绪疏导与陪伴
- 进行人格与焦虑/抑郁/压力水平自评筛查
- 长期记录并可视化自己的情绪变化模式

## 场景标签

`聊天机器人` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L10:  An advanced mental health AI companion that understands your emotions and personality to provide personalized supp
> L45: - **🌐 Multi-Agent Architecture**: Orchestrates specialized agents (emotion, safety, therapy, personality, diagnosis
> L342:  LLM Foundation (Google Gemini)

## 星数曲线

```mermaid
xychart-beta
    title "Rayyan9477/Solace-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9dcf810956f8` · [字段定义](../../DATASET.md)*
