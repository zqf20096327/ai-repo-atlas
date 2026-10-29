# VarunGumma/IndicTransToolkit

⭐ 39 · Cython · MIT · 推送 2026-04-30 · [GitHub](https://github.com/VarunGumma/IndicTransToolkit) · [官网](https://openreview.net/forum?id=vfT4YuzAYA) · 个人维护

**IndicTrans2 系列翻译模型的工具包：预处理/后处理与评测**

为 Rotary-IndicTrans2 与 IndicTrans2 系列模型提供模块化、可扩展的工具包，兼容对应 HuggingFace 模型。核心组件 IndicProcessor 负责批量的预处理与后处理（以 Cython 实现），并支持 num_return_sequences 多候选输出处理；IndicEvaluator 提供 BLEU 与 ChrF2++ 打分的评测实现。要求 Python 3.10+ 与 Linux/MacOS 环境，暂不支持 Windows。作者自述为 bleeding-edge 模块，可能存在 import 问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- IndicProcessor 批量预处理/后处理（Cython 实现）
- IndicEvaluator 输出 BLEU 与 ChrF2++ 分数
- 兼容 HuggingFace 发布的 IndicTrans2 模型

## 适用场景

- 在训练与推理流程中处理 IndicTrans2 模型的输入输出
- 对印度语言机器翻译结果做 BLEU/ChrF2++ 评测
- 基于源码扩展 IndicTrans2 相关功能

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L4: - The goal of this repository is to provide a simple, modular, and extendable toolkit for Rotary-IndicTrans2 and Ind
> L43: - `IndicEvaluator` is a python implementation of compute_metrics.sh.

## 星数曲线

```mermaid
xychart-beta
    title "VarunGumma/IndicTransToolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-29 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `df4d8e4894e8` · [字段定义](../../DATASET.md)*
