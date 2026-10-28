# FlorianBruniaux/youtube-video-insights

⭐ 24 · Python · 推送 2026-09-22 · [GitHub](https://github.com/FlorianBruniaux/youtube-video-insights) · 个人维护

**把 YouTube 字幕变成本地可检索研究库并产出带引用档案**

面向内容研究者的本地优先工具：用 yt-dlp 获取频道/视频的 VTT 字幕，构建 SQLite 目录与 FTS5 时间戳全文索引，支持 CLI 与仅绑定 127.0.0.1 的双语网页应用进行检索、覆盖率/新鲜度评估；研究循环采用人工把关——发现候选最多 10 个、需逐一批准 1-5 个精确视频 ID 后才采集。洞察与 Shorts 片段生成调用本地或云端 LLM（每次最多 10,000 字符，截断不缓存），而目录导入、索引与搜索不依赖 LLM。另提供只读 MCP 服务供 Claude Code、Codex 查询语料，导出确定性的 dossier.md 与 manifest.json。不做音频转录，源码安装（未发布 PyPI），需 Python 3.11+ 与 PATH 中的 yt-dlp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- VTT 采集 → SQLite 目录 → FTS5 时间戳全文索引的四层本地数据结构
- 人工把关的研究循环：候选发现与精确 ID 批准分离，每次 1-5 个
- 只读 MCP 服务（4 个工具）供 Claude Code / Codex 查询语料
- 确定性导出 dossier.md / manifest.json，可直接接入 RAG 或数据集

## 适用场景

- 为内容创作建立多频道可搜索的 YouTube 字幕资料库
- 竞品监控与编辑分析：评估证据覆盖与新鲜度后产出带时间戳引用的档案
- 在 Claude Code 或 Codex 中通过 MCP 查询本地字幕语料

## 场景标签

`科研工具` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L50: |Analyze a channel|`uv run yt-insights run https://www.youtube.com/@ChannelName`|Transcripts, structured insights, 
> L60: Analysis uses a local or cloud LLM. Catalog import, transcript indexing, and
> L95: Point it at a YouTube channel to keep the VTT sources locally, generate one

## 星数曲线

```mermaid
xychart-beta
    title "FlorianBruniaux/youtube-video-insights 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `51bce2e24827` · [字段定义](../../DATASET.md)*
