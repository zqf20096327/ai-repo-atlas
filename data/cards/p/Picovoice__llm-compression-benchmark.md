# Picovoice/llm-compression-benchmark

⭐ 22 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/Picovoice/llm-compression-benchmark) · [官网](https://picovoice.ai/) · 组织维护

**LLM 压缩算法基准评测框架，比较 GPTQ 与 picoLLM**

Picovoice 维护的 LLM 压缩（量化）算法基准评测框架：对 GPTQ 与 picoLLM Compression 两种算法，在 Gemma-2b/7b、Llama-2-7b、Llama-3-8b、Mistral-7b-v0.1、Phi-2 六个模型上，以 MMLU、ARC（Easy/Challenge）与 C4 困惑度三项任务评测 2/3/4-bit 量化效果。提供数据预处理脚本（MMLU/ARC/C4）与 GPTQ 量化脚本；运行 picoLLM 压缩模型需提供 Picovoice Console 的 AccessKey。README 附带完整评测结果表格。

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

- 支持 GPTQ 与 picoLLM Compression 两种压缩算法的对比评测
- 三项评测任务：MMLU、ARC Easy/Challenge、C4 困惑度
- 覆盖 Gemma/Llama-2/Llama-3/Mistral/Phi-2 六个模型，2/3/4-bit
- 提供数据集预处理与 AutoGPTQ 量化脚本

## 适用场景

- 比较不同量化算法在相同目标模型大小下的精度损失
- 复现 GPTQ 与 picoLLM 的 MMLU/ARC/困惑度评测结果
- 为自己的 LLM 压缩流程生成量化与评测数据

## 场景标签

`模型评测` `模型量化` · 领域:评测与运维

## 证据(README 行号)

> L5: This repository is a minimalist and extensible framework for benchmarking LLM compression algorithms.
> L177: Below are our benchmark results comparing GPTQ against picoLLM for all models. We perform 2, 3, and 4-bit

## 星数曲线

```mermaid
xychart-beta
    title "Picovoice/llm-compression-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `238e734ef18f` · [字段定义](../../DATASET.md)*
