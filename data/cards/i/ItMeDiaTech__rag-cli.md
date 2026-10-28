# ItMeDiaTech/rag-cli

⭐ 53 · Python · MIT · 推送 2026-03-22 · [GitHub](https://github.com/ItMeDiaTech/rag-cli) · 个人维护

**给开发者的 Claude Code 本地 RAG 插件：文档向量化检索注入上下文**

以 Claude Code 插件形式运行的本地检索增强系统：将 Markdown/PDF/DOCX/HTML/TXT 文档分块（500 token、100 重叠），用 sentence-transformers/all-MiniLM-L6-v2 生成 384 维向量存入 ChromaDB（HNSW 索引），通过 70% 语义 + 30% 关键词的混合检索与跨编码器重排返回上下文，并含多智能体查询路由。提供插件市场、源码手动安装与开发安装三种方式；插件模式无需 API key，独立模式需 Anthropic API key。README 顶部含作者账号被 Anthropic 封禁的警告，称已知限制见 KNOWN_ISSUES.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChromaDB 向量存储 + 语义/关键词混合检索与跨编码器重排
- 支持 MD/PDF/DOCX/HTML/TXT 多格式文档本地处理
- 三种运行模式：Claude Code 插件（免 API key）/独立/混合
- 多智能体框架（MAF）在 RAG 与代码分析智能体间路由查询

## 适用场景

- 在 Claude Code 中提问时自动获得项目文档上下文
- 为团队知识库建立本地可查询的向量索引
- 新成员入职时基于项目实际文档获得上下文相关的回答

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L9: A production-ready Claude Code plugin that combines ChromaDB vector embeddings with intelligent document retrieval a
> L42: - **Claude Code Integration**: Seamless plugin for enhanced development workflow
> L319:  - Integration with Claude Haiku (fast, accurate)

## 星数曲线

```mermaid
xychart-beta
    title "ItMeDiaTech/rag-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `43725ebf4870` · [字段定义](../../DATASET.md)*
