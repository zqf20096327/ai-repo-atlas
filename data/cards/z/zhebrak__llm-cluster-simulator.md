# zhebrak/llm-cluster-simulator

⭐ 38 · TypeScript · MIT · 推送 2026-04-01 · [GitHub](https://github.com/zhebrak/llm-cluster-simulator) · [官网](https://simulator.zhebrak.io/) · 个人维护

**浏览器内模拟分布式 LLM 训练/推理的算力规划模拟器**

基于第一性原理物理模型的分析型模拟器，在浏览器端（无后端）估算任意模型–集群–并行策略组合下的 MFU、显存、吞吐与成本，支持 70+ 模型、25 种 GPU、DDP/ZeRO/FSDP/TP/PP/CP/SP/EP 全并行栈，含自动寻优并行布局的优化器。物理模型已对照 LLaMA 3.1 405B、DeepSeek V3 等公开训练数据校准；明确不建模融合内核、vLLM/TensorRT 服务框架、RLHF 后训练与 TPU。另含 60 个结构化学习任务的 Learn Mode 与叙事式 Space RPG 教学模式。面向需要做集群预算与并行策略权衡评估的开发者与研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 客户端纯浏览器计算，无需真实 GPU 即可估算 MFU/显存/吞吐/成本
- 覆盖 70+ 模型、25 种 GPU 与全并行策略栈（含专家并行、上下文并行）
- 自动优化器自动搜索最快并行布局
- 物理模型对照 5 个公开训练运行校准（误差约 1-2 个 MFU 百分点）

## 适用场景

- 训练前评估需要多少 H100 及对应成本
- 比较不同张量/流水线/专家并行布局的 MFU 与吞吐
- 推断推理场景下 TTFT/TPOT 与显存可行性（如 2×4090 INT4 能否跑 70B）
- 通过结构化任务学习并行策略权衡

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: Analytical simulator for distributed LLM training and inference. Estimates MFU, memory, throughput, and cost for any
> L13: Planning distributed training and inference sizing today means either booking cluster time to run experiments or re

## 星数曲线

```mermaid
xychart-beta
    title "zhebrak/llm-cluster-simulator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-27 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `808b9d713e67` · [字段定义](../../DATASET.md)*
