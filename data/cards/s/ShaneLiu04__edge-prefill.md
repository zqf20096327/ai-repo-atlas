# ShaneLiu04/edge-prefill

⭐ 5 · C++ · 推送 2026-11-03 · [GitHub](https://github.com/ShaneLiu04/edge-prefill) · [官网](https://gitee.com/liu-xingyan04/edge-prefill) · 个人维护 · 中文 README

**端侧长上下文 LLM 的稀疏 Prefill 加速引擎**

基于固定 llama.cpp commit 的 C++17 项目，对本地长 prompt 推理的 prefill 阶段做稀疏化：按块准入、FFN 跳过、attention top-k、图内页门控等机制控制进入 KV cache 的 token 量，并配合 KV 快照、会话复用与批解码流水线。每个基准数字配质量指标同表报告，稀疏路径默认有损，budget=1.0 时与 dense 数值等价。面向在端侧 CPU/GPU 上运行本地 LLM 的开发者，Linux/WSL2 下 CMake 构建使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层稀疏 prefill：块准入、FFN skip、attention top-k、图内 query 门控
- 内容寻址 KV 快照与跨会话前缀复用（warm TTFT 为 cold 的 0.027-0.046x）
- GPU 稀疏 prefill 与 CPU 批 decode 的双上下文流水线模式
- 每个加速数字与质量指标同表报告，无 mock 计时

## 适用场景

- 端侧设备上运行 32K-64K 长 prompt 的本地 LLM 推理加速
- 降低本地 LLM 服务的首 token 延迟（TTFT）
- 需要 prefill 优化与质量指标成对验证的推理实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L12:  面向端侧长上下文大模型的分层稀疏 Prefill 引擎
> L24: Real-GGUF, prefill-stage acceleration for edge-class CPUs/GPUs, built directly
> L50: serving. EdgePrefill plans and executes a sparse prefill:

## 星数曲线

```mermaid
xychart-beta
    title "ShaneLiu04/edge-prefill 星数(近 3 点)"
    x-axis ["2026-10-31", "2026-11-08", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-31 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `b83593e3f9d9` · [字段定义](../../DATASET.md)*
