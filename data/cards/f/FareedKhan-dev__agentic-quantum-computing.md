# FareedKhan-dev/agentic-quantum-computing

⭐ 24 · Python · MIT · 推送 2026-06-18 · [GitHub](https://github.com/FareedKhan-dev/agentic-quantum-computing) · [官网](https://medium.com/@fareedkhandev/building-an-agentic-quantum-computing-system-97997172583d) · 个人维护

**本地量子核异常检测引擎：PennyLane+LangGraph 代理+本地 Qwen3-14B**

端到端管道，整合三部分：PennyLane 量子核异常检测器（CPU 模拟或本地 CUDA GPU 后端）、LangGraph 多代理（规划、执行、评估、写报告）、本地运行的 Qwen3-14B 驱动引擎并解释结果。在 KDD 网络入侵、LHC 物理、信用卡欺诈三域做基准，与经典基线对比 ROC-AUC，并做纠缠开/关消融。README 明确声明模拟量子核为受限经典模型，不做量子霸权声明；CPU 即可完整运行复现，GPU 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PennyLane 量子核（lightning.qubit/default.qubit/lightning.gpu）异常检测，与经典基线同 Z 对比
- LangGraph 代理通过 @tool 调用引擎，自动评估并生成报告
- Qwen3-14B 本地 GPU 运行，无外部 API，可用 vLLM/Ollama 兼容服务
- 三域基准（KDD/LHC/信用卡欺诈）+ 纠缠消融扫描脚本

## 适用场景

- 在笔记本 CPU 上复现量子 vs 经典异常检测基准
- 用本地 LLM 代理编排并解释量子管道运行结果
- 跨网络安全、粒子物理、金融欺诈领域测试量子核方法

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: 1. **Quantum machine learning.** A PennyLane quantum kernel anomaly detector that runs on CPU (`lightning.qubit` / `
> L9: The same engine detects anomalies across three very different domains, network intrusion (KDD), particle physics (th
> L49:    ->  Scorer (quantum One-Class SVM or quantum k-means)  ->  anomaly scores

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/agentic-quantum-computing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a6bffc2c1dfd` · [字段定义](../../DATASET.md)*
