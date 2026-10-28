# ChristinesMan/ChristineAI

⭐ 23 · Python · 推送 2026-10-14 · [GitHub](https://github.com/ChristinesMan/ChristineAI) · 个人维护

**给个人的实体 AI 伴侣：让 TPE 玩偶具备听觉、对话、语音与触感响应**

运行在 Raspberry Pi 与分布式服务器上的 AI 伴侣系统：Wernicke 做语音识别、Broca 做语音合成、Weaviate 向量库存长期记忆、Parietal Lobe 协调 LLM 交互；支持 OpenRouter、OpenAI、Ollama 等多种模型来源，配置全部通过环境变量完成，以 systemd 服务运行。本体挂载于 TPE 玩偶，配触摸、光线、陀螺仪、温度等传感器，带情绪与睡眠模型。安装需手动配置树莓派系统、apt 依赖、Python venv 与多台后端服务器，部署面向单件硬件复刻而非开箱即用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分布式架构：树莓派跑传感器与协调，STT/TTS/向量库跑在专用服务器
- 长期记忆存于 Weaviate 向量数据库，可回忆过往对话
- 多 LLM 来源：OpenRouter（含 prompt caching）、OpenAI、Ollama 本地推理
- 触摸/光线/陀螺仪/温度多传感器输入与情绪、睡眠状态模型

## 适用场景

- 为实体玩偶搭建能听、能说、能回应触摸的 AI 伴侣
- 在本地服务器上复刻并定制自己的 AI 伴侣系统
- 参考其传感器接线与分布式架构做类似硬件项目

## 场景标签

`语音 Agent` `语音合成` `语音识别` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: This repo contains code that runs an artificial companion.
> L24: - **Wernicke**: Speech-to-text processing (runs on dedicated server)
> L27: - **Parietal Lobe**: Main AI coordination and LLM interaction

## 星数曲线

```mermaid
xychart-beta
    title "ChristinesMan/ChristineAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6c8953d33ece` · [字段定义](../../DATASET.md)*
