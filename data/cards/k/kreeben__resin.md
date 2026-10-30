# kreeben/resin

⭐ 578 · C# · MIT · 推送 2026-09-28 · [GitHub](https://github.com/kreeben/resin) · 个人维护

**向量空间搜索引擎与键值存储的 .NET 库**

Resin 是一个以 C#/.NET 编写的向量空间搜索引擎、向量数据库与通用键值存储库，为老版 Resin 项目的重启。提供页面/列式结构的快速键值读写（TryPut/PutOrAppend、键集合与跨列并交操作）、字符串分析工具（StringAnalyzer、VectorOperations、相似度计算）以及构建/校验词典的命令行工具。键要求为值类型并实现 IEquatable/IComparable，值文件采用追加只写设计。README 未给出安装命令，许可证为 MIT。

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

- 页面/列式键值存储，支持链接多值与跨列集合运算（union/intersection/join）
- 字符串分析与向量运算工具库（Resin.TextAnalysis）
- 构建/校验词典与字符串比较的命令行工具
- 值流追加只写设计，偏移稳定可缓存

## 适用场景

- 在 .NET 项目中嵌入向量检索与文本相似度计算
- 需要轻依赖的磁盘键值存储与集合运算
- 构建和校验词典语料

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: Resin is a vector space search engine, a vector database and an anything key/value store. It powers efficient string
> L75: - Use `Resin.KeyValue` for fast on disk structures and efficient read/write key/value sessions.
> L76: - Use `Resin.TextAnalysis` for `StringAnalyzer`, `VectorOperations`, and similarity tooling.

## 星数曲线

```mermaid
xychart-beta
    title "kreeben/resin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 577 --> 579
    line [578, 578]
```

2026-10-18 578 → 2026-10-30 578（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `22b35c237e8c` · [字段定义](../../DATASET.md)*
