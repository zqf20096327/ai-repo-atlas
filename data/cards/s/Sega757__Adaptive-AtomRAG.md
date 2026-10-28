# Sega757/Adaptive-AtomRAG

⭐ 85 · Python · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/Sega757/Adaptive-AtomRAG) · 个人维护

**GraphRAG 的查询路由网关：按查询复杂度分流降本提速**

面向 Atom-Entity Graph（AEG）RAG 架构的条件路由网关：内置 TF-IDF + SVM 分类器（分类耗时 <1ms），将简单查询绕过深度图遍历以避免上下文污染，并对质量、延迟、token 成本执行成本感知的效用最大化调度（CA-RAG）。基于 FastAPI 构建异步端点，支持 Prometheus 指标与 Kubernetes 部署。README 给出与朴素 RAG 和无条件 AtomRAG 的基准对比（P95 延迟 -47.1%、token 成本 -48.5%、路由 Macro F1 0.928）。通过 git clone 源码安装运行。

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

- TF-IDF + SVM 分类器实现 <1ms 查询路由
- CA-RAG 效用函数平衡质量、延迟与 token 成本
- 简单事实查询绕过深度图遍历，防止上下文污染
- FastAPI 异步端点，支持 Prometheus 与 Kubernetes 部署

## 适用场景

- GraphRAG 系统中按查询复杂度自动选择轻量或深度执行路径
- 降低 RAG 服务的 P95 延迟与 token 开销
- 在生产环境以 Kubernetes 部署带指标监控的 RAG 网关

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: **Sub-millisecond query routing & cost-aware execution for GraphRAG architectures.**
> L5: Adaptive-AtomRAG is a highly optimized conditional routing gateway designed to resolve the latency and cost bottlene
> L9: * **Sub-millisecond Routing:** Classification takes `< 1 ms`, preventing unnecessary LLM planning overhead.

## 星数曲线

```mermaid
xychart-beta
    title "Sega757/Adaptive-AtomRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-28 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `416e9de9072c` · [字段定义](../../DATASET.md)*
