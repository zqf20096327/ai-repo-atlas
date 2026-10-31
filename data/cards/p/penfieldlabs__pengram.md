# penfieldlabs/pengram

⭐ 13 · Python · MIT · 推送 2026-05-04 · [GitHub](https://github.com/penfieldlabs/pengram) · 组织维护

**把代码、文档、视频等内容抽取成结构化知识图谱的命令行工具**

Python 命令行管道：读取代码（tree-sitter 确定性解析 25 种语言）、文档/电子书、YouTube 频道（yt-dlp 抓取字幕）、音视频（本地 faster-whisper 转写）、图像（视觉 LLM），再用 LLM 抽取实体并按 Penfield 24 类语义关系为每条边标注类型。输出 graph.json、交互式 graph.html、GRAPH_REPORT.md，并可导出 Penfield vault 或 Obsidian vault。抽取按 SHA256 内容哈希缓存、断点续跑；同输入重跑幂等，但跨机器/模型版本不保证字节级可复现。面向个人知识管理场景，README 明确不用于批量抓取受版权保护内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三通道架构：tree-sitter 确定性代码解析、本地 whisper 转写、LLM 实体与关系抽取
- 24 类 Penfield 语义关系 + 8 类代码结构关系，每条边带 EXTRACTED/INFERRED/AMBIGUOUS 置信标签
- SHA256 内容哈希缓存与逐文档落盘，崩溃后可续跑
- 输出 Penfield vault、Obsidian vault 或独立可用的 graph.json/html

## 适用场景

- 把代码仓库或文档库整理成可查询的知识图谱
- 追踪 YouTube 频道内容并生成带关系的笔记 vault
- 在 Obsidian 或 Penfield 中浏览跨内容源的实体关联

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L5: PENgram takes raw content — code, documents, YouTube channels, PDFs, audio,
> L22: 3. **LLM** — a small model (Claude Haiku / GPT-4o-mini by default) extracts

## 星数曲线

```mermaid
xychart-beta
    title "penfieldlabs/pengram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `31baa0a8ec4f` · [字段定义](../../DATASET.md)*
