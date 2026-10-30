# memvector/ext-memvector

⭐ 26 · C++ · MIT · 推送 2026-03-02 · [GitHub](https://github.com/memvector/ext-memvector) · [官网](https://github.com/memvector/ext-memvector) · 组织维护

**PHP 进程内向量存储与本地嵌入/重排扩展**

用 C++17 编写、带 AVX2 SIMD 加速的 PHP 扩展，在 PHP 进程内提供向量键值存储、HNSW 近似最近邻搜索、量化（F16/Int8/binary/PQ）与三种存储模式（内存/mmap 磁盘/共享内存）。可选集成 llama.cpp 以在本地运行 GGUF 嵌入与交叉编码器重排模型（24-636 MB，CPU 即可），也支持自带向量、不装 llama.cpp 的纯存储用法。面向 PHP 8.1+ 开发者，适合 OpenSwoole、ReactPHP、RoadRunner、FrankenPHP 等长驻运行时，通过 PIE 安装或源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进程内向量存储 + HNSW 搜索，无外部向量数据库
- 可选 llama.cpp 本地 GGUF 嵌入与交叉编码器重排
- F16/Int8/binary/PQ 量化与四种距离度量
- 内存/磁盘 mmap/跨进程共享内存三种存储模式

## 适用场景

- PHP 应用内做语义搜索与两阶段检索（向量搜索+重排）
- 用本地小模型替代外部嵌入 API 搭建 RAG 组件
- OpenSwoole 等长驻 worker 中常驻模型实现低延迟检索

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A high-performance PHP extension that brings local AI infrastructure and AI API to PHP developers and optimized for 
> L33: - **Text embeddings** — optional llama.cpp integration for local GGUF model inference
> L35: - **Three storage modes** — memory, disk (mmap), shared memory (cross-process)

## 星数曲线

```mermaid
xychart-beta
    title "memvector/ext-memvector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a976b16876fe` · [字段定义](../../DATASET.md)*
