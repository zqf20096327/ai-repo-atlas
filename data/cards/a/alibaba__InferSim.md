# alibaba/InferSim

⭐ 103 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/alibaba/InferSim) · 组织维护 · 中文 README

**面向 LLM 推理的性能模拟器：按 FLOPs/带宽/MFU 预估 TTFT/TPOT/TGS**

纯 Python、无第三方依赖的 LLM 推理性能模拟器，基于计算量 FLOPs、GPU 算力 FLOPS、显存带宽与实测 MFU 估算 TTFT、TPOT 与吞吐 TGS，并针对多 GPU 多节点部署按数据量与带宽估算通信延迟。适用场景为模型-系统协同设计与推理性能瓶颈分析（compute-bound / IO-bound）。支持 MHA/GQA/MLA 注意力、MoE GroupedGEMM、DP Attention 与 EP MoE、DeepEP 大 EP 等特性模拟；模拟精度依赖 kernel 基准数据。由阿里妈妈 AI Infra 团队维护，通过 python3 main.py --config-path 运行。

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

- 基于 FLOPs/FLOPS/带宽/MFU 估算 TTFT、TPOT 与 TGS
- 多 GPU 多节点部署的通信延迟估算
- 支持 MHA/GQA/MLA、MoE GroupedGEMM、DP Attn/EP MoE、DeepEP 低时延模式
- 纯 Python 实现，无第三方依赖

## 适用场景

- 给定模型超参预测推理性能，做模型-系统协同设计
- 量化推理瓶颈是 compute-bound 还是 IO-bound 以指导优化
- 对比不同 GPU（H20/H800/H200/GB200/PRO5000）部署下的预估吞吐

## 场景标签

 · 领域:LLM 基础设施/性能仿真

## 证据(README 行号)

> L3: InferSim is a lightweight simulator for LLM inference, written in pure Python without any 3rd-party dependencies. It
> L5: The main use cases of InferSim include:

## 星数曲线

```mermaid
xychart-beta
    title "alibaba/InferSim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-31 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ff357cc3bce0` · [字段定义](../../DATASET.md)*
