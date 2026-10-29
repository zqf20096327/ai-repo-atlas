# MarcoPorcellato/logseq-matryca-parser

⭐ 28 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/MarcoPorcellato/logseq-matryca-parser) · 组织维护

**确定性 Logseq Markdown 解析库：保留父子层级供 RAG 使用**

由 Matryca.ai 出品的 Python 库与 CLI，用确定性 Stack-Machine 将 Logseq Markdown 大纲文件解析为类型化 AST 与图谱：每个块携带 parent_id/path/left_id，解析块引用 ((uuid))、属性继承、别名、大小写不敏感查找，支持按文件失效的增量监视。提供面向 RAG 的 LangChain 文档与增强 chunk 导出（LlamaIndex 经未发布的独立伴生包）、JSON/Markdown 序列化、Obsidian vault 生成与交互式图谱可视化。解析只读、本地优先、零遥测；不读取 Logseq DB 图谱，313 份官方文档语料通过兼容检查（作者亦声明结果限于该语料）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性 Stack-Machine 解析为类型化 AST，保留块级 parent/path/left 关系
- 解析 ((uuid)) 块引用、属性继承、别名与大小写不敏感页面查找
- 导出 LangChain 文档与上下文增强 chunk 用于 RAG
- CLI 支持 parse/scan/export/visualize，含 per-file 增量监视与原子写

## 适用场景

- 把 Logseq 笔记转为结构化 chunk 喂给 RAG 管线
- 在不打开笔记应用的情况下用 Python/CLI 查询 Logseq 知识图谱
- 将 Logseq vault 导出为 Obsidian vault 或交互式引用拓扑图

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L41: - **Build RAG context:** export LangChain documents and enriched chunks; use
> L84: It acts as the strict **File System Driver** for your LLM OS. A deterministic
> L148: |**Export and integrate — SYNAPSE, FORGE, LENS**|Lineage-aware LangChain exports and context-enriched chunks; Llam

## 星数曲线

```mermaid
xychart-beta
    title "MarcoPorcellato/logseq-matryca-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `58cdd2bdef53` · [字段定义](../../DATASET.md)*
