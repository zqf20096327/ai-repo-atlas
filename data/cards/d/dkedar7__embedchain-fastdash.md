# dkedar7/embedchain-fastdash

⭐ 66 · Python · MIT · 推送 2026-07-05 · [GitHub](https://github.com/dkedar7/embedchain-fastdash) · [官网](https://embedchain-fastdash.fly.dev/) · 个人维护

**对话式 RAG 应用：通过聊天添加资料源并给出带引用的回答**

基于 Fast Dash 聊天模式构建的会话式 RAG 应用：用户在对话中分享网页、PDF、YouTube 视频或粘贴文本，LangGraph ReAct agent 通过 add_source 工具本地嵌入（FastEmbed）并存入会话级向量库，再以 search_knowledge 检索并生成带 [1][2] 行内引用的回答。LLM 经 OpenRouter 运行，嵌入本地计算、无需嵌入 API key。本地通过 uv 运行，部署提供 Dockerfile 与 gunicorn 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话中添加 URL/PDF/YouTube/文本作为知识源
- 本地 FastEmbed 嵌入，无需嵌入 API key
- 回答仅基于检索片段并带行内引用
- 每个会话独立的向量库与多轮记忆

## 适用场景

- 把网页或 PDF 资料喂进对话后直接提问并获得有出处的回答
- 在会话中逐步积累私有资料源做问答
- 部署一个可分享的知识库聊天 demo

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L9: Share a **web page, PDF, YouTube video, or pasted text** by chatting, then ask questions — the agent ingests your so
> L22: - **`add_source`** — load a URL / YouTube link / PDF / text, chunk it, embed it locally (FastEmbed), and store it i
> L23: - **`search_knowledge`** — semantic retrieval; the agent answers only from the retrieved passages and cites them `[

## 星数曲线

```mermaid
xychart-beta
    title "dkedar7/embedchain-fastdash 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-26 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `35ef4a13593c` · [字段定义](../../DATASET.md)*
