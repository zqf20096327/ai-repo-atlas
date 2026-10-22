# alondmnt/joplin-plugin-jarvis

⭐ 364 · TypeScript · AGPL-3.0 · 推送 2026-09-09 · [GitHub](https://github.com/alondmnt/joplin-plugin-jarvis) · 个人维护

**Joplin 笔记的 AI 助手插件：对话、语义搜索与文献综述**

运行于 Joplin（桌面与移动端）的 AI 笔记助手插件，接入在线与离线 LLM（OpenAI、Google AI、Hugging Face、Universal Sentence Encoder 等，需在设置中配置 API key）。提供侧边栏/笔记内对话（可用个人笔记作上下文）、本地默认的语义搜索与相关笔记查找、笔记自动标注（标题/摘要/链接/标签）、基于 Semantic Scholar/Crossref/Elsevier/Springer/Wikipedia 的自动文献综述、文本续写与编辑等命令。插件会将查询发送至所选模型，README 附有各命令数据发送范围表格；移动端支持见 MOBILE.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话模式支持将个人笔记作为附加上下文（Chat with your notes）
- 语义搜索默认本地离线运行，可选在线模型
- 自动文献综述整合 Semantic Scholar/Crossref/Elsevier/Springer/Wikipedia 数据库
- 笔记自动标注（标题、摘要、链接、标签）与文本续写/编辑命令

## 适用场景

- 在 Joplin 中与 AI 对话并引用自己的笔记内容
- 按语义相似度查找相关笔记
- 让 AI 自动生成文献综述并写入笔记
- 自动为笔记添加标题、摘要与标签

## 场景标签

`AI 助手` `语义搜索` `科研工具` · 领域:对话与助手

## 证据(README 行号)

> L5: Jarvis (Joplin Assistant Running a Very Intelligent System) is an AI note-taking assistant for Joplin (desktop and m
> L17:  - Find notes based on semantic similarity to the currently open note, to selected text, or to search queries. By d

## 星数曲线

```mermaid
xychart-beta
    title "alondmnt/joplin-plugin-jarvis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 363 --> 365
    line [364, 364]
```

2026-10-18 364 → 2026-10-21 364（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `890623e4fa9b` · [字段定义](../../DATASET.md)*
