# elchemista/vettore

⭐ 25 · Elixir · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/elchemista/vettore) · [官网](https://hex.pm/packages/vettore) · 个人维护

**面向 Elixir 开发者的向量检索工具包，ETS 存储 + Rust 加速**

以 ETS 为唯一权威存储的 Elixir 向量工具包，Rust(Rustler/NIF) 仅用于加速部分：SIMD/GPU 距离核、归一化、HNSW 图与 MUVERA 编码。功能包括精确 Flat 搜索、HNSW 近似搜索、Matryoshka 漏斗搜索、二值量化候选、混合候选管线重排、ColBERT 式多向量后期交互及 MUVERA 定长编码；可选通过 wgpu 使用 GPU，不依赖 Nx。集合归属创建进程，进程退出即回收；GPU top-k 上限 64，插入仅 insert-only，替换需先删除。

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

- ETS 为权威存储，Rust 仅做 SIMD/GPU/HNSW 加速
- 精确/近似/漏斗/量化/混合/多向量六类搜索路径
- MUVERA 定长编码将多向量检索降为内积搜索
- 可选 wgpu GPU 执行，不要求 Nx，兼容宿主提供的 Nx 张量

## 适用场景

- 在 Elixir/BEAM 应用内做嵌入向量检索与 RAG 召回
- ColBERT 式多向量（token/page 向量）检索
- Matryoshka 嵌入的漏斗式低成本候选筛选

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: Vettore is a small vector toolkit for Elixir that keeps your data in ETS and
> L32: - ETS-backed collections

## 星数曲线

```mermaid
xychart-beta
    title "elchemista/vettore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `81a1d3b438fa` · [字段定义](../../DATASET.md)*
