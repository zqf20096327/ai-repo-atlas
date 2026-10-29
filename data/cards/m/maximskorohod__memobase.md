# maximskorohod/memobase

⭐ 22 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/maximskorohod/memobase) · 个人维护

**hermes-agent 的本地知识库插件：对文件/网页/YouTube/Obsidian 做引用可验证的问答**

面向 hermes-agent 用户的文档知识库插件：将 PDF/DOCX/HTML/MD/CSV、网页、YouTube 视频与频道、音频及 Obsidian 笔记（只读）摄入单个本地 SQLite 库，通过 FTS5+BM25 与向量检索（RRF 融合、Cohere 重排）做混合搜索，回答仅基于检索片段并附逐字核验的引文（含页码/时间码），无法验证时返回拒答。无密钥时可降级到纯全文检索；--local 模式用本地 ONNX 嵌入（约 2.2GB 下载）。内置 SSRF 检查、注入防护等 6 个固定安全机制，支持访客集合与配额。需 Python 3.11+，一条脚本命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四步防幻觉流程：充分性门控→仅基于片段生成→逐字引文核验→无确认引文即拒答
- FTS5 俄语词干化 + 向量检索（BGE-M3）RRF 融合并经 Cohere 重排
- 支持 PDF/DOCX/网页/YouTube 频道/音频 STT（Whisper 带时间码）/Obsidian vault 只读摄入
- --local 模式本地 fastembed 嵌入，完全无密钥运行

## 适用场景

- 让 agent 基于我的 PDF、笔记和 YouTube 收藏回答并给出可核验引文
- 本地保存知识库数据，避免文档上传第三方云
- 为访客开通受限的知识库集合并设定配额

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L37: MemoBase закрывает обе дыры. Это как **NotebookLM, но локально и прямо внутри агента**: вы загружаете источники, а 
> L68: - **Ответы без выдумок и честный отказ.** Гейт достаточности → ответ tool-less-моделью только по фрагментам → досло

## 星数曲线

```mermaid
xychart-beta
    title "maximskorohod/memobase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bc877684bd68` · [字段定义](../../DATASET.md)*
