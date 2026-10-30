# dengls24/LLM-para

⭐ 22 · Python · 推送 2026-04-16 · [GitHub](https://github.com/dengls24/LLM-para) · [官网](https://llm-para.onrender.com) · 组织维护

**LLM 推理性能分析框架：FLOPs、访存与 Roofline 建模**

基于 Flask 的 Web 分析框架，对 Transformer 推理流水线中的 13 类以上算子进行 FLOPs 计数、访存流量与算术强度建模，扩展经典 Roofline 与 Energy Roofline，覆盖 GQA、MoE、MLA、RoPE、SwiGLU、FlashAttention 等现代架构特性。内置 24 种硬件平台参数（NVIDIA/AMD GPU、Apple Silicon、PIM、多卡集群等），支持异构多层内存建模、能耗/TCO/碳足迹分析与多目标设计空间探索（Pareto 优化）。提供 CLI、Python API 与 REST API，CSV/JSON 导出。多芯片切分与投机解码分析标注为开发中（WIP）。面向需要分析 LLM 推理瓶颈与硬件选型的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 13 类以上算子的 FLOPs 计数与访存分解（GQA/MoE/MLA/SwiGLU/FlashAttention）
- 24 种硬件平台库，含 PIM 与多卡集群，支持自定义参数
- 多目标 DSE 引擎：性能/能耗/TCO/CO₂e 的 Pareto 优化
- Flask Web 界面 + CLI + Python API + REST API，CSV/JSON 导出

## 适用场景

- 分析某个模型在特定硬件上的推理瓶颈是访存还是算力受限
- 对比不同硬件平台与量化位宽下的吞吐、能耗与 TCO
- 做 LLM 推理硬件相关的论文实验与 Pareto 设计空间探索

## 场景标签

 · 领域:LLM 推理/系统分析

## 证据(README 行号)

> L10: A comprehensive **web-based analytical framework** for analyzing **computation complexity**, **memory access patter
> L22: > **Abstract:** We present LLM-Para, a first-order analytical framework whose two principal contributions are: (1) 

## 星数曲线

```mermaid
xychart-beta
    title "dengls24/LLM-para 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f69dd008519c` · [字段定义](../../DATASET.md)*
