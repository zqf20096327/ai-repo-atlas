# integrallis/vectors

⭐ 18 · Java · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/integrallis/vectors) · [官网](https://integrallis.github.io/vectors/) · 组织维护

**面向 JVM 的嵌入式向量搜索与持久化库（Java 25）**

在 JVM 应用进程内提供索引化相似度搜索、本地持久化与元数据过滤，无需独立向量数据库服务。基于 JDK Vector API 实现 SIMD 距离内核，提供 FLAT/HNSW/Vamana/IVF 系列索引、八种量化器、mmap 代际原子持久化引擎，以及 Spring AI 与 LangChain4j 适配器。要求 JDK 25，需以 incubator 模块参数运行；单一持久化集合目录仅支持单写入进程。核心库 Apache-2.0，分布式层模块采用 FSL-1.1-ALv2 许可（到期转 Apache-2.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HNSW/Vamana/IVF-Flat/IVF-PQ 索引与八种量化器
- 基于 JDK Vector API 的 SIMD 距离内核与 mmap 代际持久化
- Spring AI / LangChain4j 一级适配器与 Spring Boot 自动配置
- 基础依赖仅 9 个 JAR、小于 1 MiB，可选 S3/Arrow 运行时

## 适用场景

- JVM 应用需要向量检索但不想部署外部向量数据库
- 为 Spring AI / LangChain4j 应用提供进程内持久化向量存储
- 本地语义缓存与混合（稠密+全文）检索

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L20: first-class Spring AI and LangChain4j adapters.
> L122: |Integration|Spring AI, LangChain4j, Spring Boot auto-configuration, semantic-cache adapters|

## 星数曲线

```mermaid
xychart-beta
    title "integrallis/vectors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `20bb98545aa8` · [字段定义](../../DATASET.md)*
