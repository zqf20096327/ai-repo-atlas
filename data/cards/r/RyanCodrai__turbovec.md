# RyanCodrai/turbovec

⭐ 17,400 · Rust · MIT · 推送 2026-10-07 · [GitHub](https://github.com/RyanCodrai/turbovec) · [官网](https://pypi.org/project/turbovec/) · 个人维护

**面向 Python/Rust 开发者的 2-4 比特量化内存向量索引库**

基于 Google Research TurboQuant 的进程内向量索引，提供 Python 与 Rust 双 API。将向量以 2 或 4 bit/维存储并用 SIMD 内核直接检索，无需训练步骤，支持增量持久化（sync 只写变更）、id 过滤搜索与微秒级删除。以库而非服务形式分发，无网络 API；x86 内核运行时按 CPU 特性选择。提供与 LangChain、LlamaIndex、Haystack、Agno 的集成包，并可从源码用 maturin 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 11.1 天,年发版 0,8 位贡献者
- 涨星:近 1 天 **+5**(自 20261016 起算)
- 安装:pypi 包 `turbovec` 月下载 36,907

## 能力要点

- 2/4 bit 每维量化存储，内存较 float32 缩小 7.8–15.5 倍
- 无需训练与重建，增删向量即时生效，sync() 增量落盘且崩溃安全
- 提供 LangChain/LlamaIndex/Haystack/Agno 的 drop-in 替代集成
- Rust API 与 Python 对应，支持 allowlist/bitmask 过滤检索

## 适用场景

- 在本机进程内为 RAG 应用存储和检索嵌入向量
- 资源受限环境下降低大规模嵌入的内存占用
- 需要完全离线嵌入+检索栈的本地部署
- 作为框架内存向量存储的替换组件接入现有检索管线

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L17: turbovec is an in-process vector index for Python and Rust. It stores each vector at 2 or 4 bits per dimension usin
> L50: Framework integrations are drop-in replacements for each framework's in-memory store — same public surface, same pe
> L95: - **You need a graph index.** turbovec scans every vector. At 100K vectors a query costs 0.13–0.25 ms on all eight 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `2a88cbd33957` · [字段定义](../../DATASET.md)*
