# microsoft/RetrievalAttention

⭐ 154 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/microsoft/RetrievalAttention) · [官网](https://aka.ms/RetroInfer) · 组织维护

**长上下文 LLM 推理加速系统：将 KV 缓存作为向量存储利用注意力稀疏性**

RetroInfer 是微软推出的长上下文 LLM 解码加速系统，把 KV cache 视为 GPU–CPU 协同执行环境下的向量存储：通过注意力感知向量索引 wave index 检索关键 token，用 wave buffer 协调 KV cache 放置与 GPU/CPU 间的计算传输重叠；注意力划分为 steady/retrieval/estimation 三区处理动态稀疏。提供 Python API、简单测试脚本与 RULER/LongBench/推理基准评测脚本，支持 Llama-3/Qwen2.5/DeepSeek-R1-Distill 等模型。依赖 CUDA 12.4，示例 demo 约需 35GB 显存与 70GB 内存；框架允许用户接入新的稀疏注意力方法。

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

## 能力要点

- wave index 向量索引从 KV cache 检索关键 token，利用注意力稀疏性
- wave buffer 协调 GPU–CPU 间 KV cache 放置与计算/传输重叠
- 三区注意力划分（steady/retrieval/estimation）与有精度界的注意力估计
- 提供 RULER/LongBench/推理基准评测脚本，可扩展新稀疏注意力方法

## 适用场景

- 在有限显存下加速长上下文 LLM 的推理
- 复现论文在 RULER/LongBench 上的精度与吞吐结果
- 在此基础上集成自定义稀疏注意力方法做实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: RetroInfer is a novel system that rethinks the KV cache as vector storage within a GPU–CPU co-execution setup to acc
> L142: This repository provides a flexible inference framework that allows users to easily integrate new sparsity-based a

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/RetrievalAttention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 153 --> 155
    line [154, 154]
```

2026-10-18 154 → 2026-10-30 154（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1f733e3a6ac1` · [字段定义](../../DATASET.md)*
