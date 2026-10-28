# kmeanskaran/stock-agent-ops

⭐ 306 · Python · 推送 2026-02-13 · [GitHub](https://github.com/kmeanskaran/stock-agent-ops) · 个人维护

**生成每周股票报告的端到端 MLOps 流水线（LSTM+多Agent）**

自动化股票价格预测与金融报告生成的完整流水线：PyTorch LSTM 父子迁移学习架构（S&P 500 基座模型微调到个股）、LangGraph 协调 4 个 Agent（分析师/市场专家/报告生成/审校）产出报告；配套 Feast 特征库、MLflow/DagsHub 实验注册、FastAPI+Redis 实时服务、Qdrant 语义缓存（24 小时内相似请求直接返回缓存）、Prometheus/Grafana/Evidently 监控漂移。LLM 引擎为 Ollama（gpt-oss:20b-cloud 与 nomic-embed-text），通过 run_docker.sh 或 Docker Compose 一键启动，Streamlit 提供前端。需自行配置 DagsHub 与 FinnHub API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LSTM 父子迁移学习：S&P 500 基座微调个股（NVDA/AAPL/GOOG 等）
- LangGraph 协调 4 个专职 Agent 生成金融报告
- Qdrant 语义缓存：相似查询 24 小时内直接返回缓存报告
- Auto-Healing：API 检测缺失模型自动触发训练

## 适用场景

- 我想每周自动生成个股分析报告而不用手写脚本
- 想参考一个含特征库/注册表/监控的 MLOps 全流程参考实现
- 学习迁移学习 LSTM 在股价预测中的父子架构用法

## 场景标签

`金融量化` `MLOps` `微调` · 领域:学习与行业

## 证据(README 行号)

> L34: - **🧠 Transfer Learning**: Uses a Parent-Child architecture (S&P 500 base model) to predict individual stock prices
> L35: - **🤖 Agentic AI**: A multi-agent system (LangGraph) that acts as a financial analyst, market expert, and editor to

## 星数曲线

```mermaid
xychart-beta
    title "kmeanskaran/stock-agent-ops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 303 --> 306
    line [304, 305, 305]
```

2026-10-18 304 → 2026-10-28 305（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `42f72a1d2c81` · [字段定义](../../DATASET.md)*
