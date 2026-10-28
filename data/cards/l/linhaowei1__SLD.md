# linhaowei1/SLD

⭐ 37 · Python · 推送 2026-01-30 · [GitHub](https://github.com/linhaowei1/SLD) · [官网](https://linhaowei1.github.io/scaling_law_discovery) · 组织维护

**用 LLM 进化式 agent 自主发现 LLM 缩放定律的基准与工具**

ICLR 2026 论文官方仓库，包含 SLDAgent（基于进化搜索的 AI agent，通过 OpenEvolve 框架协同优化缩放定律的符号公式与参数拟合算法）与 SLDBench（首个缩放定律发现基准，含 8 个任务，数据来自 5,000 余项 LLM 训练实验，托管于 Hugging Face）。评测以 R²、NMSE、NMAE 为主指标衡量外推精度；任何 OpenAI 兼容 API 端点均可接入。面向科研用户，Python 3.13+，通过 uv 或 pip 从源码安装。

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

- SLDAgent 通过进化搜索联合优化公式形式与拟合算法
- SLDBench 含 8 类缩放定律发现任务与 train/test 数据划分
- 支持任意 OpenAI 兼容 LLM 端点（--primary-model 指定模型）
- 已接入 Terminal-Bench Harbor 可评测通用代码 agent

## 适用场景

- 运行进化式 agent 自动发现 LLM 缩放定律
- 在 8 个缩放定律任务上评测不同 LLM 或代码 agent 的外推能力
- 向基准贡献新的缩放定律发现任务

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L17: **SLDAgent** is an evolution-based AI agent that autonomously discovers scaling laws for large language models. Thi
> L37: - **SLDBench**: A comprehensive benchmark containing 8 diverse scaling law discovery tasks
> L53: **SLDBench** is the first comprehensive benchmark for scaling law discovery, curated from over 5,000 LLM training e

## 星数曲线

```mermaid
xychart-beta
    title "linhaowei1/SLD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8e8895fa28fb` · [字段定义](../../DATASET.md)*
