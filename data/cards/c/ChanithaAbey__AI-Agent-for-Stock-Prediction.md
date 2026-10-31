# ChanithaAbey/AI-Agent-for-Stock-Prediction

⭐ 22 · Python · MIT · 推送 2026-01-30 · [GitHub](https://github.com/ChanithaAbey/AI-Agent-for-Stock-Prediction) · 个人维护

**股票数据分析与买卖建议生成的 LLM 命令行工具**

Python 命令行程序：读取任意 Yahoo Finance 股票代码近一年历史数据，识别高低价时段，通过 TheNewsAPI 检索关联商业/科技新闻，再调用 Groq Cloud 提供的 Llama LLM 生成分析、Buy/Sell/Hold 建议与摘要，结果存入 .csv 并用 matplotlib 绘图。需配置 GROQ_API_KEY 与 NEWS_API_KEY，克隆源码并 pip 安装依赖后运行 main.py。README 声明仅供教育与科研用途，输出不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 获取任意 Yahoo Finance 股票代码近一年历史数据
- 高低价事件关联新闻检索（TheNewsAPI）
- Groq Cloud 的 Llama LLM 生成 Buy/Sell/Hold 建议与摘要
- 结果保存为 .csv 并用 matplotlib 绘图

## 适用场景

- 我想快速拿到某只股票一年的行情和新闻关联分析
- 做量化金融或 LLM 应用的课程作业和研究实验
- 生成带图表的股票表现分析留档

## 场景标签

`金融量化` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: An AI Agent for stock data analysis, news rerieval, and prediction; powered by Yahoo Finance, GroqCloud, Llama and T
> L10: - Provides in-depth analysis, Buy/Sell/Hold suggestion, and summarization through an LLM API (Llama LLM, provided b

## 星数曲线

```mermaid
xychart-beta
    title "ChanithaAbey/AI-Agent-for-Stock-Prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b6d8b2739549` · [字段定义](../../DATASET.md)*
