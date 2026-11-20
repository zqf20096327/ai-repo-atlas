# wevote-project/crystal-text-splitter

⭐ 10 · Crystal · MIT · 推送 2026-01-20 · [GitHub](https://github.com/wevote-project/crystal-text-splitter) · 组织维护

**Crystal 的 RAG/LLM 应用文本分块库**

以 Crystal shard 形式发布的文本分块库，提供基于字符与基于单词两种切分模式，通过可配置重叠保留相邻块之间的上下文。API 含一次性返回数组的 split_text、基于块的 each_chunk 与惰性 Iterator 版本，README 给出 RAG 流水线示例与按场景的 chunk_size/chunk_overlap 配置建议表。零外部依赖，安装方式为在 shard.yml 中添加依赖后运行 shards install。README 中含两处重复的 Performance 与 Comparison 章节。

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

- 字符/单词两种切分模式，句子感知边界
- 可配置 chunk_overlap 保留块间上下文
- 惰性 Iterator API 降低大文档内存占用（README 基准：1MB 文本约 17.9MB 内存）
- 零外部依赖的纯 Crystal 实现

## 适用场景

- 为 RAG 流水线把长文档切成带重叠的分块
- 按嵌入模型的长度限制预处理文本再生成嵌入
- 为向量数据库构建保持上下文的文档分块

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L7: **Intelligent text chunking for RAG (Retrieval-Augmented Generation) and LLM applications in Crystal.**
> L28: - **RAG Systems**: Retrieving relevant context for LLM queries
> L105: Typical usage in a Retrieval-Augmented Generation system:

## 星数曲线

```mermaid
xychart-beta
    title "wevote-project/crystal-text-splitter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `cdc177d2ed68` · [字段定义](../../DATASET.md)*
