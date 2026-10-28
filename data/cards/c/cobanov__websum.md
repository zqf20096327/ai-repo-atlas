# cobanov/websum

⭐ 127 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/cobanov/websum) · [官网](https://pypi.org/project/websum/) · 个人维护

**网页与 YouTube 视频摘要工具，可插拔 LLM 后端**

提供 Summarizer 单一对象，输入 URL 自动识别网页或 YouTube 视频并生成摘要，另有 translate 功能。LLM 后端为 Protocol 协议，内置 OllamaBackend（本地默认、无需 key）与 OpenAIBackend，可自行实现 .build() 插入任意 LangChain chat model。长文本自动分块以适应上下文窗口。同一套代码暴露为 CLI、Python 库与 Gradio Web UI，支持 pip 安装与 Docker 运行，Python 3.10–3.13，基础安装不携带任何模型 SDK。

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

- summarize(url) 自动识别网页或 YouTube 视频
- 后端为 LLMBackend Protocol，Ollama/OpenAI 一行切换，支持自定义
- Ollama 本地后端默认可用，无需 API key
- CLI、库、Gradio UI 三种使用形态，长输入自动分块

## 适用场景

- 用本地 Ollama 模型离线摘要网页或视频
- 在 OpenAI 与本地模型间切换而不改调用代码
- 通过 Gradio 网页或命令行快速生成摘要

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L19: One object, `Summarizer`, takes a URL and works out whether it is a page or a video.
> L26: s = Summarizer(backend=OllamaBackend(model="llama3:instruct"))
> L34: - **Local by default.** Ollama is a first-class backend, so nothing has to leave the

## 星数曲线

```mermaid
xychart-beta
    title "cobanov/websum 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 125 --> 128
    line [126, 127, 127]
```

2026-10-18 126 → 2026-10-28 127（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8c5db98356fc` · [字段定义](../../DATASET.md)*
