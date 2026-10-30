# DuckTapeKiller/horme

⭐ 22 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/DuckTapeKiller/horme) · 个人维护

**面向 Obsidian 的本地优先 AI 助手插件，带 RAG 笔记记忆**

Obsidian 社区插件，通过本地 LLM（默认 Ollama 或 LM Studio，无需 API key）为笔记库提供聊天问答。核心机制 Vault Brain 是本地 RAG 引擎：索引只存字符偏移与嵌入指纹不存原文，自动检测笔记修改并后台更新索引，采用标题感知分块、多查询融合与混合相关性评分（语义向量+元数据+正文关键词）。另提供实时相关笔记发现、语义标签建议、语法校对（可索引用户自己的语法手册）、frontmatter 摘要生成及可扩展的 HTTP 技能调用；启用云端模型时通过隐私防火墙保护数据，API key 存于 Obsidian Secret Storage。需 Obsidian v1.11.4+，手动放置三个文件安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Vault Brain 本地 RAG：索引存字符偏移与嵌入，自动后台增量更新
- 混合相关性评分：向量相似度 69%、元数据 17.2%、正文深扫 13.8%
- 支持语义标签建议、语法手册索引校对、frontmatter 摘要生成
- 内置 Wikipedia/Wiktionary/DuckDuckGo 等技能，可自定义 HTTP 技能接任意 REST API

## 适用场景

- 在我的 Obsidian 笔记库上用本地模型做问答检索
- 写作时自动发现与当前笔记语义相关的其他笔记
- 管理数千个标签并自动生成笔记摘要

## 场景标签

`AI 助手` `聊天机器人` `知识库管理` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L79: > When using local providers (Ollama/LM Studio), no data leaves your machine and no API keys are required. If you u
> L105: The Vault Brain gives the AI long-term memory of your entire knowledge base. It uses a high-performance, private R

## 星数曲线

```mermaid
xychart-beta
    title "DuckTapeKiller/horme 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `55b7b2e3d039` · [字段定义](../../DATASET.md)*
