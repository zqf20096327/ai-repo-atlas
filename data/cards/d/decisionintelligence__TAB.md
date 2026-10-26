# decisionintelligence/TAB

⭐ 146 · Jupyter Notebook · 推送 2025-11-26 · [GitHub](https://github.com/decisionintelligence/TAB) · [官网](https://arxiv.org/pdf/2506.18046) · 组织维护 · 中文 README

**面向研究者的时间序列异常检测评测基准库**

TAB 是一个开源 Python/PyTorch 库，为时间序列异常检测研究者提供端到端评测：在同一管线和多种评测策略、指标下比较各类异常检测模型与基线算法，覆盖统计学习、深度学习、预训练与 LLM 类模型（UniTS、Timer、TimesFM 等，checkpoint 可从 Google Drive/Huggingface 获取）。提供预处理数据集、实验脚本（单变量/多变量检测）与中文英文文档，论文已被 PVLDB 2025 接收，开发获华为云支持。全程在 Python 3.8 下测试，通过 pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端评测管线，多种评测策略与指标
- 支持统计、深度学习、预训练与 LLM 类模型统一对比
- 提供预处理数据集、checkpoint 与可复现实验脚本
- 配套开源时间序列异常检测榜单（2025.10）

## 适用场景

- 我要在统一基准下评测自己的异常检测模型
- 复现论文中的基线实验结果
- 分析时间序列数据集的趋势、季节性等特征

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L16: TAB is an open-source library designed for time series anomaly detection researchers.
> L18: We provide a clean codebase for end-to-end evaluation of time series anomaly detection models, comparing their perf

## 星数曲线

```mermaid
xychart-beta
    title "decisionintelligence/TAB 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 144 --> 147
    line [145, 146, 146]
```

2026-10-18 145 → 2026-10-26 146（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c38a46f7434f` · [字段定义](../../DATASET.md)*
