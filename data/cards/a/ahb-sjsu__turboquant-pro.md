# ahb-sjsu/turboquant-pro

⭐ 27 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ahb-sjsu/turboquant-pro) · 组织维护

**面向下游消费者度量的嵌入索引与 LLM KV 缓存压缩库**

PyPI 发布的 Python 压缩工具包，核心主张是按下游消费者实际使用的指标（检索 recall、attention/困惑度）而非重建余弦来压缩张量。提供 PCAMatryoshka 谱分配、TurboQuant、残差编码 IVF 索引、架构感知的非对称 K/V 量化、CUDA/Triton 内核与 vLLM KV connector。另带证书/回放体系：tqp certify/verify 产出分布无关的 rank 下界，CLAIMS.md 记录每个头条数字的复现状态，CI 门控的头条数为约 9.6× 压缩、GloVe-100 recall@10≈0.999。核心安装仅依赖 numpy，加速与 torch 功能为可选 extras。当前发布为 2.0.0a3 预发布，connectors API 在 2.0.0 前可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- PCAMatryoshka 谱分配量化与残差编码 IVF，支持压缩域检索与大于内存的分片 memmap 索引
- 架构感知 KV 缓存量化：per-channel key + PolarQuant value，AutoConfig 按模型名自动配置
- tqp certify/verify 分布无关 rank 证书与一键 replay 复现机制
- vLLM KV connector 集成与 pgvector/FAISS/NATS 等集成路径

## 适用场景

- 压缩向量索引以降低存储并在压缩域直接检索
- 为 LLM 推理压缩 KV 缓存并保持困惑度接近 fp16
- 对压缩部署做证书化验证与第三方复核

## 场景标签

`向量数据库` `模型量化` · 领域:知识与检索

## 证据(README 行号)

> L10: **Consumer-aware compression for embedding indexes and LLM KV caches.** TurboQuant Pro compresses each vector by th
> L82: |Integrate (pgvector, FAISS, NATS, vLLM, …)|Integrations|

## 星数曲线

```mermaid
xychart-beta
    title "ahb-sjsu/turboquant-pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3fb6db0e8ff4` · [字段定义](../../DATASET.md)*
