# LeonMarzollDev/local-llm-rtx-spark

⭐ 3 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/LeonMarzollDev/local-llm-rtx-spark) · 个人维护

**在 RTX Spark N1X 上用 vLLM 本地运行大模型的脚本与基准集**

面向 NVIDIA RTX Spark N1X（GB10/DGX Spark 同芯片家族）笔记本的本地大模型运行项目：提供 scripts/llm 等脚本，以 Docker + vLLM 启停 Qwen3.8 系列模型（flash/27b-fast/27b-agent 预设），内置统一内存分配、CDI 设备挂载、CPU 核绑定、缓存清理等启动修复；附带 GNOME 顶栏指示器、性能/质量基准脚本（速度、prefill、大海捞针、HumanEval/BFCL/GSM8K）与编码 harness 对比文档。需 Docker 29+、NVIDIA Container Toolkit、本地模型文件与 Python 3 (GTK)。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键启停 vLLM 模型的脚本（flash/27b-fast/27b-agent/27b 预设，内置启动修复）
- 统一内存（CPU/GPU 共享）下 96 GB 模型可靠启动的 7 项修复
- GNOME 顶栏指示器：加载倒计时与实时生成/预填充速度（读取 vLLM /metrics）
- 基准文档：速度、上下文（至 1M）、质量与 Qwen Code/OpenCode/Claude Code 对比

## 适用场景

- 在 128 GB 统一内存的 N1X/DGX Spark 设备上本地运行 27B 级模型
- 为编码 agent（OpenCode/Claude Code/Qwen Code）提供本地 OpenAI 兼容 API
- 复测本地大模型的速度、内存与质量基准

## 场景标签

`推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L48: |scripts/llm|start / stop one model at a time (presets `flash`, `27b-fast`, `27b-agent`, `27b`), all fixes above bu
> L57: Requirements: Docker (29+) with the NVIDIA Container Toolkit (1.20+, which generates the CDI spec at boot via

## 星数曲线

```mermaid
xychart-beta
    title "LeonMarzollDev/local-llm-rtx-spark 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a3e72ed374a3` · [字段定义](../../DATASET.md)*
