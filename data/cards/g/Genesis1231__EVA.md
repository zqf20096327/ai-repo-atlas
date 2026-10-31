# Genesis1231/EVA

⭐ 26 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/Genesis1231/EVA) · 个人维护

**给个人用户的多模态实验性语音助手：可本地或 API 运行**

基于 LangGraph 框架构建的实验性语音助手，支持终端与 FastAPI/WebSocket 两种运行方式，并有 React Web 界面。功能包括语音 ID 与人脸识别的个性化交互、多语言回复、后台多任务，以及可配置的工具系统（DuckDuckGo/Tavily 搜索、YouTube 搜索、Midjourney 图像生成、Suno 音乐生成等）。LLM/TTS/STT/视觉模型均可配置，集成 OpenAI、Anthropic、Groq、Google 与 Ollama，可在带 GPU 的机器上完全本地运行，也可用免费组合。需要 Python 3.10+，从源码克隆安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 语音 ID 与人脸识别实现个性化交互
- LLM/TTS/STT/视觉模型均可配置，支持 Ollama 本地运行
- 兼容 LangChain 工具，单文件即可添加新工具
- 支持终端与 API/WebSocket，含 React Web 界面

## 适用场景

- 我想有一个能认出我声音和长相的对话式语音助手
- 我想在本地 GPU 上零成本运行一个多模态助手
- 我想通过配置不同模型和工具定制自己的助手体验

## 场景标签

`语音 Agent` `AI 助手` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L23: EVA is an experimental voice assistant that reimagines human-AI interaction through intelligent, proactive engageme
> L71: EVA is built on LangGraph framework, with some customized modules and tools. Importantly, You can run it purely loc
> L75: - Integrated with OpenAI, Anthropic, Groq, Google, and Ollama.

## 星数曲线

```mermaid
xychart-beta
    title "Genesis1231/EVA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f296b194fc68` · [字段定义](../../DATASET.md)*
