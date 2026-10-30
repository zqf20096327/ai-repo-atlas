# ZhuBit/cowork-semantic-search

⭐ 29 · Python · AGPL-3.0 · 推送 2026-03-24 · [GitHub](https://github.com/ZhuBit/cowork-semantic-search) · 个人维护

**本地文档语义搜索 MCP 服务器：让 AI 工具检索你的文件**

面向 MCP 客户端的语义检索插件：将本地 txt/md/pdf/docx/pptx/csv 文档分块、用 paraphrase-multilingual-MiniLM-L12-v2 生成 384 维向量并存入 LanceDB 本地文件，向 Claude Code、Cursor、Windsurf、Cline 等 MCP 客户端暴露 index_folder、semantic_search 等 4 个工具。全离线运行（首次下载 ~120MB 嵌入模型），支持 SHA-256 增量索引、向量+全文混合检索（RRF）、50+ 语言，也可作为 Python 库使用。安装方式为 git clone 后 pip install -e ".[all]"。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全离线运行，数据不出本机，LanceDB 本地文件存储无需服务器
- SHA-256 内容哈希增量索引，仅重处理变更文件
- 语义+全文关键词混合检索（Reciprocal Rank Fusion）
- 支持 6 种文档格式与 50+ 语言，兼容任意 MCP 客户端

## 适用场景

- 让 Claude Code/Cursor 等 AI 编码工具检索本地项目文档
- 把 Obsidian 笔记库变成 AI 工具可查询的知识库
- 在无网络、不外发数据的前提下做跨文件语义检索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L22: This plugin bridges that gap. It indexes your local documents into a small, fast vector database. When you ask a qu
> L37: - **Any MCP client** -- works with Claude Code, Cursor, Windsurf, Cline, and any other MCP-compatible tool.
> L157:   main.py       # MCP server + tool definitions

## 星数曲线

```mermaid
xychart-beta
    title "ZhuBit/cowork-semantic-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b61d8f2b064a` · [字段定义](../../DATASET.md)*
