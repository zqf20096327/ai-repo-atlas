# AnkitNayak-dev/llmBench

⭐ 49 · Python · MIT · 推送 2026-03-15 · [GitHub](https://github.com/AnkitNayak-dev/llmBench) · 个人维护

**本地 LLM 运行时基准测试与硬件深度分析套件**

面向本地 LLM 部署的评测工具：提供两种模式——硬件深度审计（CPU 缓存层级、内存类型/频率、GPU PCIe/VRAM/功耗温度等参数检测，并按 VRAM/RAM 配置给出模型推荐）与推理压力测试（TTFT、吞吐、能耗 J/T、VRAM 占用等指标）。支持对 Ollama 与 llama.cpp 服务器进行基准测试，并通过并行爬取 arena.ai 六个子排行榜（ELO 分数），用参数感知估计将本地性能映射到全球排行。要求 Python 3.10+、NVIDIA GPU、Windows 10/11 优化，从源码克隆运行。

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

- 对 Ollama / llama.cpp 服务器做 TTFT、吞吐、能耗（J/T）、VRAM 等推理指标测试
- CPU 缓存/内存/GPU 接口/温度功耗的硬件深度审计
- 并行爬取 arena.ai 六个子排行榜并合并为本地全球基线
- 按 VRAM/RAM 配置输出模型推荐（Ollama 与 GGUF/llama.cpp）

## 适用场景

- 我想测本地 Ollama 或 llama.cpp 服务的真实推理性能
- 部署前审计机器硬件瓶颈，确认能跑什么规模的模型
- 把本地成绩与 LMSYS Arena 全球排行做对照

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: llmBench is a high-depth benchmarking tool designed to measure the raw performance of local LLM runtimes (Ollama, ll
> L31: ### Mode 2: LLM Performance & Global Index

## 星数曲线

```mermaid
xychart-beta
    title "AnkitNayak-dev/llmBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-28 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `476928254087` · [字段定义](../../DATASET.md)*
