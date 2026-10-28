# jchunk-io/jchunk

⭐ 19 · Java · Apache-2.0 · 推送 2026-08-20 · [GitHub](https://github.com/jchunk-io/jchunk) · [官网](https://docs.jchunk.io/) · 组织维护

**Java 文本分块库：为 RAG 应用提供多种切分策略**

面向 Java 应用的轻量级文本分块库，提供固定长度、递归字符、语义三类分块器，以 Maven/Gradle 依赖形式发布（jchunk-fixed、jchunk-recursive-character、jchunk-semantic 等独立 artifact），供 RAG 应用在检索前对文本进行切分。项目使用 Maven 构建（mvnw），提供测试、格式化与 javadoc 构建命令。注意：README 首行声明该项目已停止维护、正式结束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供固定、递归字符、语义三种分块策略
- 以 Maven/Gradle 依赖形式按策略独立引入
- Apache 2.0 许可证

## 适用场景

- RAG 流水线中在嵌入前对文档做文本切分
- Java 项目中按需选用固定/递归/语义分块策略

## 场景标签

 · 领域:LLM 基础设施/RAG 预处理

## 证据(README 行号)

> L10: JChunk project is simple library that enables different types of text splitting strategies, essential for RAG appli
> L46: ### Semantic Chunker

## 星数曲线

```mermaid
xychart-beta
    title "jchunk-io/jchunk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9f6ac61ea7e0` · [字段定义](../../DATASET.md)*
