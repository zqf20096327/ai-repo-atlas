# chenxuniu/TokenPowerBench

⭐ 18 · Python · 推送 2026-09-14 · [GitHub](https://github.com/chenxuniu/TokenPowerBench) · 组织维护

**测量 LLM 推理功耗/能耗/吞吐的基准测试库**

面向单 NVIDIA GPU 节点的 Python 基准测试库，测量 LLM 推理的 GPU 功率、能耗、吞吐与 TTFT/prefill/decode 时序：通过 NVML 读 GPU、Intel RAPL 读 CPU/DRAM、IPMI 读整机功率；基于首个输出 token 事件分离 prefill 与 decode 窗口；不可用的测量记为 null 并保存原因。推理路径针对 vLLM 0.10.x，支持 Python API 与 CLI，另提供 Ray/SLURM 多节点编排（未纳入已验证范围）。随 AAAI 2026 论文发布，供科研复现使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NVML/RAPL/IPMI 三层功耗测量，不可用项记 null 并附原因
- 基于首 token 事件的 TTFT/prefill 与 decode 窗口分离
- 保存完整实验产物（提示词、配置、原始传感器读数）供复现
- 支持单节点 vLLM 已验证路径与 Ray/SLURM 多节点编排

## 适用场景

- 对比不同推理引擎/部署配置的能耗与吞吐
- 复现论文中的功耗基准实验
- 在 GH200 等节点上记录功耗测量能力与硬件限制

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3: A Python library for measuring LLM inference power, energy, throughput, and
> L20: - Measure selected GPUs through NVML, CPU/DRAM through Intel RAPL, and whole-node power through IPMI.
> L167: The v1.0 validated inference path is single-node vLLM. The

## 星数曲线

```mermaid
xychart-beta
    title "chenxuniu/TokenPowerBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `12def5357228` · [字段定义](../../DATASET.md)*
