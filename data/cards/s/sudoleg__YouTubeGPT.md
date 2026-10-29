# sudoleg/YouTubeGPT

⭐ 17 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sudoleg/YouTubeGPT) · 个人维护

**本地可运行的 YouTube 视频摘要与问答 Web 应用**

基于 LLM 的 Web 应用：抓取 YouTube 视频字幕，生成摘要并支持针对视频内容的问答，可保存与导出 Markdown 到个人库。模型可选 OpenAI API、本地 Ollama 或自定义 OpenAI 兼容端点，通过 LangChain 构建提示词并处理响应，ChromaDB 作为向量存储，Streamlit 提供界面。提供 Docker 方式运行，也支持 uv 虚拟环境开发；使用 Ollama 时默认上下文窗口 4k tokens，需手动调整。

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

- YouTube 视频摘要与问答，支持自定义摘要提示词
- 支持 OpenAI API、本地 Ollama 与自定义 OpenAI 兼容端点
- 摘要与回答可保存到库并导出 Markdown
- Docker 一键运行，可通过环境变量配置模型与参数

## 适用场景

- 快速了解长视频内容并针对内容提问
- 在本地模型上对 YouTube 视频做摘要问答
- 整理并导出视频学习笔记

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L7: YouTubeGPT is a web app that can be run fully locally and lets you **summarize and chat (Q&A)** with YouTube videos.
> L15: ### :question: Get answers to questions about the video content **VIEW DEMO**

## 星数曲线

```mermaid
xychart-beta
    title "sudoleg/YouTubeGPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aed961d7b6a0` · [字段定义](../../DATASET.md)*
