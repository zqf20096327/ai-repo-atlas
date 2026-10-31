# Somnius/shadowrealms-ai

⭐ 21 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Somnius/shadowrealms-ai) · 个人维护

**自托管的黑暗世界跑团 Web 应用：AI 主持人带掷骰、语音与记忆**

面向跑团玩家与主持人的自托管 Web 应用，用 AI Storyteller 运行 World of Darkness 编年史（Classic oWoD Revised 或 V5 规则）。服务器掷骰并按角色卡自动计算骰池；支持 Discord 风格聊天、角色创建、PDF 导出。通过 LM Studio 与 Ollama 接入本地模型，bge-m3 嵌入 + ChromaDB 提供长期记忆与规则书检索；可选 speech 容器提供本地 TTS 与 faster-whisper 转录。界面与主持人支持英语和希腊语；可选接入 Anthropic/OpenAI 云 API（默认关闭）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 服务器掷骰并按角色卡（专长、Hunger、损伤）计算骰池
- 本地 LLM（LM Studio/Ollama）+ bge-m3/ChromaDB 的 RAG 记忆与规则书检索
- 本地语音：Piper/Pocket TTS 朗读与 faster-whisper GPU 转录（含误听词修正）
- 按角色分配模型：英语/希腊语主持人、工具、分类器、翻译各自可设

## 适用场景

- 和朋友在线跑黑暗世界编年史，由 AI 主持人叙述与判骰
- 在自己服务器上本地运行模型与语音，故事数据不出机器
- 用希腊语或英语进行角色扮演与规则查询

## 场景标签

`Agent 记忆` `语音合成` `语音识别` · 领域:Agent 开发

## 证据(README 行号)

> L44: ShadowRealms AI is a web app for running World of Darkness chronicles with an AI Storyteller. You host it yourself:
> L5: ### Self-hosted AI Storyteller for World of Darkness chronicles
> L89: - Long-term memory and rule-book search with multilingual `bge-m3` embeddings in ChromaDB.

## 星数曲线

```mermaid
xychart-beta
    title "Somnius/shadowrealms-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3e7ef9573fab` · [字段定义](../../DATASET.md)*
