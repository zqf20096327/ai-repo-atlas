# SilvioBaratto/optimizer

⭐ 177 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/SilvioBaratto/optimizer) · 个人维护

**给量化研究者的组合优化 uv 工作区，含 LLM 基金代理与模拟交易**

由四个 Python 包组成的 uv workspace：纯 Python 的 skfolio/scikit-learn 组合优化库 portopt-core（26 个子模块、15 种优化器构建器、VaR/回测/期权/信用模型等研究工具）、定时抓取行情的 ingestion 守护进程（PostgreSQL 存储）、共享数据库层，以及 portopt-fund 桥接——由 LLM 选择策略、优化器计算权重、模拟交易经人工审批门执行。优化库无需 Docker/数据库即可用；守护进程与 fund 需 Docker + PostgreSQL 16 及聊天模型端点。面向量化开发与研究者。

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

- sklearn/skfolio 风格的可组合优化原语：15 种优化器构建器与 26 个子模块
- 内置风险（VaR/回测）、衍生品、信用、统计套利等 8 个研究工具
- LLM 驱动的基金代理：LLM 决策、优化器计算、模拟交易等待人工审批
- 库可零 Docker/数据库安装运行，CLI 提供安装向导与生命周期管理

## 适用场景

- 在自己的代码里构建和调优组合优化 pipeline
- 定时维护 PostgreSQL 中的行情/基本面/宏观数据
- 用 LLM 代理生成模拟交易组合并人工审批
- 回测动量/均线策略并计算 VaR、有效前沿等风险指标

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: > daemon** that keeps PostgreSQL fresh, a shared **database layer**, and an agentic
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
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c7f0f3947a1b` · [字段定义](../../DATASET.md)*
