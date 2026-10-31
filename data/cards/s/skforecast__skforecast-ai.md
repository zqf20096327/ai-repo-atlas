# skforecast/skforecast-ai

⭐ 52 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/skforecast/skforecast-ai) · [官网](https://ai.skforecast.org) · 组织维护

**面向分析师/开发者的确定性时间序列预测助手**

基于 skforecast 库构建的 Python 预测助手：对时间序列做数据剖析，按可读的确定性规则选择预测器、滞后项、窗口特征、区间与交叉验证策略，返回预测结果及可独立运行的 skforecast 脚本；同一输入总是产生同一结果。LLM 层为可选安装，仅用于解释决策、按提示精炼计划或生成回测策略，输出经 Pydantic 校验且不改变结果，支持 pydantic-ai 列出的多家提供商与 Ollama 本地模型。另提供 CLI 与面向 Claude Code、Cursor 等编码代理的 MCP 服务器。需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性规则引擎：剖析→计划→脚本→预测，同输入同结果
- 返回可独立用 skforecast 运行的生成脚本
- 可选 LLM 层仅解释/精炼，输出经 Pydantic 校验，不发送数据集
- 提供 CLI 与 MCP server，供 Claude Code/Cursor 等代理作为工具调用

## 适用场景

- 给一条时间序列，自动完成建模、验证并产出可复现的预测脚本
- 在编码代理里用自然语言完成预测与回测
- 用 ask() 让 LLM 解释预测结果与评估指标

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: **The forecasting assistant that shows its work.** Give skforecast-ai a time series: it profiles the data, chooses 
> L92: - **Data profiling**: frequency, missing values, exogenous and categorical variables, and the significant lags from
> L108: - **Any provider** through pydantic-ai: OpenAI, Anthropic, Google, Groq, AWS Bedrock, Ollama for local models, or 

## 星数曲线

```mermaid
xychart-beta
    title "skforecast/skforecast-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-31 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `42e5253e1862` · [字段定义](../../DATASET.md)*
