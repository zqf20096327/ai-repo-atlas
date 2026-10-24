# openfabric-systems/simllm

⭐ 51 · Python · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/openfabric-systems/simllm) · [官网](https://openfabric-simllm-codex.yifenwan.chatgpt.site) · 组织维护

**面向 LLM 部署的包级网络仿真器：购硬件前预测 TTFT/TPOT**

SimLLM 在购置或预留硬件前预测大规模 LLM 部署的推理性能指标（TTFT、TPOT、goodput、SLO 达成率）。其机制是让真实的 vLLM/SGLang 前端调度器不经修改地运行，将模型执行替换为校准的 compute-cost 模型，并通过 htsim 的包级离散事件网络后端（Clos fabric）仿真集合通信流量，支持开环与闭环两种耦合模式。面向分布式 AI 系统与网络研究者/工程师，由 OpenFabric 发起并获 ETH Zurich、CSCS、Stanford、NERSC 支持。安装需 git clone 源码并用 C++17 工具链（GCC/Clang/MSVC）编译 HTSIM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 真实 vLLM/SGLang 调度器 + 仿真 GPU 执行器与包级 htsim 网络（ATLAHS）
- vLLM 经 --distributed-executor-backend 接入，SGLang 经插件框架接入，无需 fork
- 开环（GOAL trace）与闭环（虚拟时钟反馈调度）两种耦合模式
- examples/ 下多项研究附 expectations.md、RESULTS.md 与证据溯源

## 适用场景

- 购买或预留集群硬件前评估 LLM serving 性能与 SLO 达成
- 研究 incast、拥塞控制等网络效应对 TTFT/TPOT 分布的影响
- 对比 DCQCN 与显式速率端点在大规模 incast 下的表现
- 分析请求时间在计算、内存与网络间的分解

## 场景标签

 · 领域:分布式 AI 系统/网络仿真

## 证据(README 行号)

> L13: SimLLM predicts the serving performance (TTFT, TPOT, goodput, SLO
> L21: captures. SimLLM couples the **real frontend scheduler** of your serving
> L42: - **No forks.** vLLM plugs in through its existing

## 星数曲线

```mermaid
xychart-beta
    title "openfabric-systems/simllm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-24 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `79e660921135` · [字段定义](../../DATASET.md)*
