# one-bit/mnemoria

⭐ 16 · Rust · MIT · 推送 2026-03-02 · [GitHub](https://github.com/one-bit/mnemoria) · [官网](https://crates.io/crates/mnemoria) · 个人维护

**AI agent 的持久记忆存储：混合检索、git 友好**

面向 AI agent/助手的 Rust 记忆存储系统，提供跨会话的持久可搜索记忆：语义检索、BM25 全文检索及 RRF 融合的混合检索；存储为追加式二进制格式（rkyv 零拷贝序列化），可直接提交到 git 追踪历史，CRC32 校验链支持崩溃恢复。内嵌 model2vec 512 维 CPU 嵌入模型（约 130MB，首次使用下载）。提供 Rust 库与 CLI（init/add/search/ask/timeline 等命令）。限制：嵌入模型为 CPU-only，搜索索引每次打开时重建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义+BM25+RRF 混合检索
- 追加式二进制格式，可提交 git 追踪记忆历史
- CRC32 校验链与崩溃恢复、compact 清理损坏条目
- model2vec CPU 嵌入，12 种记忆条目类型分类

## 适用场景

- 给 Claude/Cursor 等 AI 助手提供跨会话长期记忆
- 团队将项目记忆随代码一起做版本管理
- 对记忆库做关键词/语义/自然语言问答检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: Mnemoria is a **memory storage system for AI agents**. It provides persistent, searchable memory that AI assistants 
> L33: - **Semantic Search** - Find memories by meaning, not just keywords
> L36: - **Git-Friendly** - Append-only binary format, version control safe

## 星数曲线

```mermaid
xychart-beta
    title "one-bit/mnemoria 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `44ec9c0d2ce7` · [字段定义](../../DATASET.md)*
