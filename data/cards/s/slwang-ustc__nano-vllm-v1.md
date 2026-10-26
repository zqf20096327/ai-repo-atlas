# slwang-ustc/nano-vllm-v1

⭐ 102 · Python · MIT · 推送 2026-01-26 · [GitHub](https://github.com/slwang-ustc/nano-vllm-v1) · 个人维护

**从零实现的轻量 vLLM 复刻，复现 v1 调度与 Chunked Prefill**

以 Nano-vLLM 为基础重新设计核心架构的轻量推理引擎，用约 1,200 行 Python 代码复现 vLLM v1 的请求调度策略，并实现 Chunked Prefill、Paged Attention、Prefix Caching、Tensor Parallelism、Torch Compilation 等优化。API 接口与 vLLM 对齐（LLM.generate 有少量差异），提供离线推理示例 example.py 与在线基准 serving_bench.py。面向阅读推理引擎源码并做实验的开发者。

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

- 约 1,200 行 Python 实现 vLLM v1 调度策略的完整复现
- 支持 Paged Attention / Prefix Caching / Chunked Prefill / Tensor Parallelism / Torch Compilation
- API 镜像 vLLM 接口，提供离线与在线用法示例

## 适用场景

- 学习或讲授 LLM 推理引擎的调度与优化机制
- 在可读的小型代码库上实验调度策略与 Chunked Prefill
- 复现 vLLM v1 风格的离线/在线推理基准

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A lightweight vLLM implementation built from scratch. While built upon the foundation of Nano-vLLM, this project sig
> L13: See `example.py` (offline) and `serving_bench.py` (online) for usage. The API mirrors vLLM's interface with minor d

## 星数曲线

```mermaid
xychart-beta
    title "slwang-ustc/nano-vllm-v1 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 100 --> 103
    line [101, 102, 102]
```

2026-10-18 101 → 2026-10-26 102（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fdb000ac62c4` · [字段定义](../../DATASET.md)*
