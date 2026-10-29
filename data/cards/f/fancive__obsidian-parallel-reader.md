# fancive/obsidian-parallel-reader

⭐ 21 · JavaScript · MIT · 推送 2026-08-01 · [GitHub](https://github.com/fancive/obsidian-parallel-reader) · 个人维护 · 中文 README

**Obsidian 阅读辅助插件：原文旁显示 AI 摘要卡片并滚动同步**

Obsidian 社区插件，提供分屏阅读：左侧原笔记，右侧 AI 生成的摘要卡片，编辑器滚动时自动高亮对应卡片，点击卡片跳回源段落。摘要由 LLM 输出结构化 JSON，通过锚点引文定位实现不依赖标题的同步；内容 SHA-1 缓存使重开笔记即时显示。支持 20+ 提供商（OpenAI/Anthropic/Gemini/Ollama 等），含 SSE 流式输出，可经社区插件市场安装，需自备 API Key 或本地模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 自适应分段生成摘要卡片，滚动同步高亮与源文定位
- 支持 20+ 提供商，含 Ollama/LM Studio 本地模型与 SSE 流式输出
- 按内容 SHA-1 + 设置指纹持久缓存，重开即时显示
- 卡片可复制/编辑/删除/跳转，可导出为 Markdown 笔记

## 适用场景

- 长文阅读时分屏对照 AI 摘要与原文
- 用本地模型（Ollama/LM Studio）无 API Key 生成摘要
- 将摘要卡片导出到仓库作为阅读笔记

## 场景标签

`知识库管理` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3:  Split-view reading for Obsidian — your original note on the left, AI-generated summary cards on the right, with scr
> L27: - **20+ providers** — Anthropic, OpenAI, Gemini, OpenRouter, Groq, DeepSeek, Moonshot, Ollama, LM Studio, and more.

## 星数曲线

```mermaid
xychart-beta
    title "fancive/obsidian-parallel-reader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `90aa3434112a` · [字段定义](../../DATASET.md)*
