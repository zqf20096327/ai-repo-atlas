# RecursiveIntell/turbo-quant

⭐ 27 · Rust · MIT · 推送 2026-10-25 · [GitHub](https://github.com/RecursiveIntell/turbo-quant) · 组织维护

**Rust 向量压缩 sidecar 编解码库：近似候选生成+精确重排**

实现 TurboQuant、PolarQuant、QJL 研究原语的实验性 Rust crate：在保留原始精确向量为权威的基础上，构建压缩 sidecar 生成近似候选，要求精确重排后方可晋升；提供 packed wire 格式、字节账目 receipt、候选索引与 KV-cache shadow 压缩测量模式。定位为可复用的 sidecar 原语，不提供普适质量或性能保证，不做生产替代；构建 0.2.3 包需 C 编译器（GCC/Clang）。面向构建检索/记忆系统的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- TurboQuant/PolarQuant/QJL 三种量化器与近似内积估计
- TurboSidecarIndex 候选生成 + SearchReceiptV1 精确重排元数据
- 版本化 wire 格式与字节账目（CodecProfileV1/CompressionReceiptV1）
- KV-cache shadow 压缩与评分测量模式

## 适用场景

- 为语义检索系统降低候选生成成本或存储
- 测量 KV-cache 量化的工作负载影响（shadow 模式）
- 实验验证极化坐标/符号投影量化的近似精度

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: Experimental Rust codecs for derived vector-compression sidecars: PolarQuant, TurboQuant, QJL sketches, packed wire 
> L5: Exact vectors remain canonical while turbo-quant builds a compressed sidecar, generates approximate candidates, and 
> L15: - **Sidecar indexing** — `TurboSidecarIndex`, `SearchOptions`, and `SearchReceiptV1` for bounded candidate generati

## 星数曲线

```mermaid
xychart-beta
    title "RecursiveIntell/turbo-quant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-27 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0813dd105c19` · [字段定义](../../DATASET.md)*
