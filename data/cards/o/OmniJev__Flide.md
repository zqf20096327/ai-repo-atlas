# OmniJev/Flide

⭐ 582 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/OmniJev/Flide) · [官网](https://flide.org) · 组织维护 · 中文 README

**面向开发者的 Jev 决策模型快速推理引擎**

Flide 是面向 Jev 风格决策模型的推理基础设施，通过精确状态分叉（exact state forking）机制使一个状态可分叉为多个问题并在单次前向传播中各自得到答案。提供 `/v1/systemone` API 服务、`--vllm-kv` 从 vLLM 所服务 agent 的 KV 读取答案、会话缓存、批不变输出、FP8/int8 量化与多进程前端等选项。README 自述其相对 vLLM 与 SGLang 的加速倍数，并附论文、文档与邮件分诊示例。运行于 NVIDIA GPU（Linux/WSL2）或 AMD Instinct GPU（Linux）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 精确状态分叉：一个状态分叉为多个问题，各在单次前向传播中作答
- 支持 FP8 与 int8 量化及批不变输出选项
- 支持 Qwen2.5/Qwen3/Qwen3.5、Gemma 4 及数十个决策模型家族
- 提供 PyPI 包与 Docker 镜像两种分发方式

## 适用场景

- 用 Jev 决策模型对大量邮件等条目做多问题批处理打标
- 为 LLM agent 的每一步决策提供低延迟推理服务
- 在单卡 GPU 上以量化方式运行决策模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L15: Flide is fast inference infrastructure for Jev-style decision models. With exact state forking it is up to 9.5 time
> L53: Flide runs on an NVIDIA GPU under Linux or Windows WSL2, and on an AMD Instinct GPU under Linux. Install it with uv

## 星数曲线

```mermaid
xychart-beta
    title "OmniJev/Flide 星数(近 21 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 0 --> 639
    line [3, 4, 7, 8, 29, 358, 445, 475, 489, 501, 508, 525, 538, 543, 545, 550, 553, 566, 571, 577, 582]
```

2026-10-29 3 → 2026-11-28 582（+579）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `20991169475d` · [字段定义](../../DATASET.md)*
