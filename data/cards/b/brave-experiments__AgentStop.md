# brave-experiments/AgentStop

⭐ 18 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/brave-experiments/AgentStop) · [官网](https://brave.com/blog/agentstop/) · 组织维护

**本地 AI agent 提前终止的节能研究代码与数据集**

ACM CAIS '26 论文 'AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices' 的配套代码与数据。提供在 Apple Silicon 与 NVIDIA Jetson 设备上对本地 LLM agent（FRAMES 问答、SWE-Bench 编码任务）进行功耗/温度/风扇转速剖析的脚本，训练用于提前终止 agent 的分类器，并附论文剖析数据与复现 notebook。后端为 llama.cpp（经 llama-swap 切换模型），早期工作使用 Ollama 拉取 Qwen3 模型，答案评估使用 Claude Haiku API。复现完整实验耗时可达数天。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Apple Silicon / NVIDIA Jetson 功耗、温度、风扇转速剖析流程
- 训练 AgentStop 提前终止分类器
- 附论文原始剖析数据与复现 notebook（reproduce_paper_results.ipynb）
- 覆盖 FRAMES 问答与 SWE-Bench Verified 编码两类任务

## 适用场景

- 复现论文中的功耗剖析与提前终止结果
- 在本地设备上测量 LLM agent 的能耗
- 基于提供的 trace 数据训练终止分类器

## 场景标签

 · 领域:AI 系统/能效研究

## 证据(README 行号)

> L3: This repo contains the code and data for our paper "AgentStop: Terminating Local AI Agents Early to Save Energy in C
> L134: ### Profiling
> L162: Begin with running the notebook `notebooks/process_profiling_results.ipynb`, changing the config parameters as nee

## 星数曲线

```mermaid
xychart-beta
    title "brave-experiments/AgentStop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `9d480a31559e` · [字段定义](../../DATASET.md)*
