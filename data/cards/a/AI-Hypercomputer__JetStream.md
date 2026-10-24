# AI-Hypercomputer/JetStream

⭐ 470 · Python · Apache-2.0 · 推送 2026-01-05 · [GitHub](https://github.com/AI-Hypercomputer/JetStream) · 组织维护

**XLA 设备（TPU）上吞吐与内存优化的 LLM 推理引擎**

Google 开源的 LLM 推理引擎，面向 XLA 设备（首发 TPU，GPU 在规划中），优化吞吐量与内存使用。提供 Jax（MaxText）与 PyTorch 两种参考引擎实现，文档覆盖 v5e Cloud TPU VM 在线推理、GKE 上部署 Gemma、基准测试与性能分析等。可用 make install-deps 安装依赖并本地运行 mock server 与单元测试。README 顶部声明：核心功能已迁移至 tpu-inference 仓库，本仓库将于 2026 年 2 月 1 日归档为只读。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 XLA 设备（TPU）的吞吐与内存优化推理
- 提供 Jax 与 PyTorch 两种参考引擎实现
- 文档覆盖 Cloud TPU / GKE 部署、基准测试与性能分析

## 适用场景

- 在 TPU 上部署 LLM 在线推理服务
- 基准测试与调优 TPU 上的 LLM 服务
- GKE 集群中用 TPU 服务 Gemma 类模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: # JetStream is a throughput and memory optimized engine for LLM inference on XLA devices.
> L13: JetStream is a throughput and memory optimized engine for LLM inference on XLA devices, starting with TPUs (and GPU

## 星数曲线

```mermaid
xychart-beta
    title "AI-Hypercomputer/JetStream 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 469 --> 471
    line [470, 470]
```

2026-10-18 470 → 2026-10-24 470（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `792a4c0a43e7` · [字段定义](../../DATASET.md)*
