# priya-sundaram-dev/whoosh

⭐ 39 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/priya-sundaram-dev/whoosh) · [官网](https://priya-sundaram-dev.github.io/whoosh/) · 个人维护

**纯 Python 全文索引与搜索库：进程内 BM25 检索，无需编译或服务器**

Whoosh 的持续维护分支，提供纯 Python 实现的全文索引、BM25F 排序、布尔/短语/通配/模糊查询、分面、结果高亮与拼写纠错。索引为目录中的文件，无需守护进程或原生依赖，pip 安装即用，适用于桌面应用、CLI、静态站搜索与测试。另附 whoosh 命令行工具按文件夹建索引检索，并提供 RAG BM25 检索指南、MCP server 可选组件及 LangChain/LlamaIndex 集成包。README 声明该分支由 AI agent（Priya Sundaram）维护，变更经公开 PR 与 CI 验证，BSD 2-Clause 许可。适用规模为低百万级文档以内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Python 实现，无编译、无服务器、无原生依赖，pip 安装即用
- BM25F 排序、布尔/短语/通配/模糊查询、分面与高亮、拼写纠错
- 附 whoosh 命令行：对文件夹做词干化 BM25 检索，支持增量更新
- 可选 MCP server 与 LangChain/LlamaIndex 集成包，用于 RAG 检索

## 适用场景

- 给 Python 程序或桌面应用嵌入进程内全文搜索
- 在终端对笔记/文档/源码文件夹做带排序的全文检索
- 为 RAG 管线提供纯 Python 的 BM25/混合检索，不依赖向量数据库
- 把本地文档以 MCP search/fetch 工具形式提供给 AI agent

## 场景标签

 · 领域:信息检索/搜索库

## 证据(README 行号)

> L135:  - Whoosh for RAG: BM25 keyword retrieval & hybrid search
> L156:  LangChain and LlamaIndex integrations ship as the standalone

## 星数曲线

```mermaid
xychart-beta
    title "priya-sundaram-dev/whoosh 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-25 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4f0771d18abf` · [字段定义](../../DATASET.md)*
