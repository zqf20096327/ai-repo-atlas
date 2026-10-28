# Yashwanth-pilli/ILLIP

⭐ 27 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/Yashwanth-pilli/ILLIP) · 个人维护

**本地优先的个人 AI 平台：多 agent、记忆与本地模型商店**

面向个人用户在自有设备上运行的离线优先 AI 平台（React + FastAPI）：包含 27 个内置 agent、Qdrant 向量记忆与知识图谱、Stable Diffusion 图像生成、本地 Whisper 语音识别、Playwright 浏览器自动化、12 个社区插件与技能系统。支持 Ollama/llamafile/AirLLM 本地模型及 OpenRouter/Groq 云端模型，按硬件（GPU/RAM）推荐可运行模型；提供 Agent SDK 自建 agent、Telegram 远程访问与多设备同步。限制：模型策略屏蔽 DeepSeek，仅允许 Llama/Mistral/Phi/Gemma 等家族。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 27 个内置 agent（Planner/Builder/Reviewer 等）+ Agent SDK 自建扩展
- 本地模型自动检测与按硬件推荐（4GB 笔记本到大型 GPU）
- Qdrant 向量记忆 + 自动知识图谱 + 结构化 Memory Ball
- 本地 Whisper STT、Piper TTS、Stable Diffusion 图像生成

## 适用场景

- 在本机离线运行带记忆与多 agent 的私人 AI 助手
- 通过 Telegram 从手机访问留在电脑上的本地 AI
- 用浏览器自动化与插件/技能系统扩展日常工作流

## 场景标签

`AI 助手` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: ILLIP AI is a portable, private, self-improving AI system that runs on your own hardware. It is not a chatbot. It i
> L56: ### 27 Agents
> L66: ### Local Model Support

## 星数曲线

```mermaid
xychart-beta
    title "Yashwanth-pilli/ILLIP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7bb5c424796a` · [字段定义](../../DATASET.md)*
