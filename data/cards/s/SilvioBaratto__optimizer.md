# SilvioBaratto/optimizer

⭐ 177 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/SilvioBaratto/optimizer) · 个人维护

**LLM 选基、skfolio 算权的组合优化工作区，人工审批模拟交易**

由四个 Python 包组成的 uv workspace：可组合的 skfolio/scikit-learn 优化库 portopt-core（26 个子模块、15 种优化器构建器）、定时拉取行情的 PostgreSQL 采集守护进程、共享数据库层，以及一个 LLM 驱动的基金桥（deepagents/langgraph），由 LLM 决策、优化器计算权重、模拟交易经人工审批后执行。库本体零 Docker/数据库依赖可独立安装；采集与 fund 组件需 Docker + PostgreSQL 16。安装走 uv、安装向导脚本或 pip editable。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 种优化器构建器：Mean-Risk、HRP、HERC、NCO、DR-CVaR 等
- 26 个研究子模块：VaR 回测、Kelly 工具、Black-Scholes 定价、Merton 信用模型等
- LLM 决策 + 优化器计算 + 人工审批门控的模拟交易流程
- 优化库零 Docker/DB 依赖，可单独 pip 安装

## 适用场景

- 在自己的量化代码里构建和调参组合优化 pipeline
- 定时维护一套本地行情/基本面/宏观数据库
- 用 LLM 管理模拟盘基金并在审批门下执行调仓

## 场景标签

`Agent 框架` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Portfolio optimization in one **uv workspace**: a composable skfolio /
> L6: > **fund** where an LLM chooses, the optimizer computes, and paper trades wait
> L25: |Run an LLM-driven fund manager that decides and lets the optimizer compute|the **`fund`** bridge (`portopt-fund`)|

## 星数曲线

```mermaid
xychart-beta
    title "SilvioBaratto/optimizer 星数(近 5 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-11-06", "2026-11-08", "2026-11-28"]
    y-axis "stars" 175 --> 178
    line [176, 177, 176, 177, 177]
```

2026-10-26 176 → 2026-11-28 177（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `4b96003c13ea` · [字段定义](../../DATASET.md)*
