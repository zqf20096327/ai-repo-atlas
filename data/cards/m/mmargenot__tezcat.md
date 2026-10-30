# mmargenot/tezcat

⭐ 21 · TypeScript · GPL-3.0 · 推送 2026-03-30 · [GitHub](https://github.com/mmargenot/tezcat) · 个人维护

**Obsidian 插件：用 AI 嵌入索引笔记库并联想式检索**

面向 Obsidian 用户的笔记索引与检索插件：以 AI 嵌入向量对 vault 建库，在写作时以 remembrance agent 方式浮现相关笔记与片段，支持向量检索与向量+全文的混合检索。结果可用于插入链接、插入内容或打开来源页面。本地运行依赖 Ollama（推荐，支持 Nomic Embed v1.5 与 BGE M3），也可用 OpenAI 嵌入（非本地，可能产生费用）。安装途径为 Obsidian 社区插件市场或克隆源码 npm 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 嵌入向量索引 vault，写作时浮现相关笔记与片段级内容
- 支持朴素向量检索与向量+全文混合检索
- 本地运行支持 Ollama（Nomic Embed v1.5、BGE M3），可选 OpenAI 嵌入
- 检索结果可插入链接、插入文本或跳转来源页面

## 适用场景

- 写作时自动联想 vault 中相关的笔记与片段
- 在 Obsidian 内对个人知识库做语义检索
- 用本地 Ollama 模型嵌入，避免云端嵌入费用

## 场景标签

`知识库管理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: Tezcat is an Obsidian plugin that indexes your thoughts. It uses a aritificial intelligence (AI) embedding vectors t
> L9: This tool works best with Ollama in the current state. It frequently makes calls to generate embeddings and search i

## 星数曲线

```mermaid
xychart-beta
    title "mmargenot/tezcat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0ea7fb4d69f0` · [字段定义](../../DATASET.md)*
