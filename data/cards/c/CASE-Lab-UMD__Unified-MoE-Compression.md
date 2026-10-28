# CASE-Lab-UMD/Unified-MoE-Compression

⭐ 92 · Python · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/CASE-Lab-UMD/Unified-MoE-Compression) · [官网](https://openreview.net/forum?id=HTpMOl6xSI) · 组织维护

**MoE 大模型压缩研究框架：论文官方实现，统一剪枝/量化/结构裁剪**

TMLR 2025 论文的官方实现，来自马里兰大学 CASE Lab 等机构。提供统一压缩流水线，分两个维度：Expert Slimming（专家内幅度剪枝、Wanda、SparseGPT、AWQ/GPTQ 4-bit 量化）与 Expert Trimming（Expert Drop / Layer Drop / Block Drop 结构性裁剪），并支持混合方案与轻量后微调。覆盖 Mixtral-8x7B 与 DeepSeek-MoE-16B 两类架构，提供压缩、微调、FLOPs/延迟/困惑度及 LM-Eval 基准评测的脚本。微调脚本按 8×A100 80GB 分布式训练配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一实现剪枝、4-bit 量化（AWQ/GPTQ）与结构裁剪（Expert/Layer/Block Drop）
- 支持 Mixtral-8x7B 与细粒度共享专家的 DeepSeek-MoE-16B
- 提供经实证的 Pareto 压缩组合方案与轻量后微调恢复脚本
- 配套 FLOPs/延迟、困惑度与 LM-Eval Harness 标准基准评测

## 适用场景

- 对 MoE 大模型做剪枝、量化与结构裁剪以压缩显存占用
- 复现论文中各压缩技术在 MMLU/GSM8K 等基准上的结果
- 研究不同压缩手段组合的效率-精度权衡

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L31: > This is the official implementation of the paper **Towards Efficient Mixture of Experts: A Holistic Study of Comp
> L44: This project provides a unified compression pipeline investigating two complementary dimensions:

## 星数曲线

```mermaid
xychart-beta
    title "CASE-Lab-UMD/Unified-MoE-Compression 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-28 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `36e535ab5c0b` · [字段定义](../../DATASET.md)*
