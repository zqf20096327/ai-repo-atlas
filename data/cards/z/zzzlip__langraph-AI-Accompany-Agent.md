# zzzlip/langraph-AI-Accompany-Agent

⭐ 21 · Python · 推送 2025-11-03 · [GitHub](https://github.com/zzzlip/langraph-AI-Accompany-Agent) · 个人维护 · 中文 README

**AI 角色扮演陪伴应用：持久记忆的对话与社交生成**

基于 Flask 与 langgraph 的 AI 角色扮演聊天应用：用户创建 AI 角色并对话，agent 可判断并生成分享图片；集成 Google Gemini、Qwen、Moonshot-Kimi 等多种 LLM API。记忆系统分为短期与休眠长期记忆，通过 langgraph hook 节点自动总结短期记忆入库，长期记忆用 ChromaDB 向量库与 HuggingFace 嵌入做 RAG 检索。另含 AI 角色朋友圈与日记功能，由独立线程并行生成。需自行配置 API key，通过 pip 安装依赖后以 python app.py 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 短期/长期记忆融合机制，通过 langgraph hook 节点自动总结入库
- 长期记忆 RAG：ChromaDB 向量库 + HuggingFace 嵌入检索
- AI 角色朋友圈与日记由独立线程并行生成
- 对话中按需生成图片（few-shot + COT 提示架构）

## 适用场景

- 与自建 AI 角色进行持久记忆的角色扮演对话
- 查看 AI 角色自动生成的朋友圈动态与日记
- 自部署无广告免费的陪伴类聊天应用

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: This is a Flask-based AI role-playing agent developed using the langgraph agent architecture. It allows users to cre
> L30: - The memory module is divided into two parts: 1. Short-term memory 2. Dormant long-term memory.

## 星数曲线

```mermaid
xychart-beta
    title "zzzlip/langraph-AI-Accompany-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `219d9ad02c95` · [字段定义](../../DATASET.md)*
