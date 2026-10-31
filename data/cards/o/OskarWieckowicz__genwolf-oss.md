# OskarWieckowicz/genwolf-oss

⭐ 13 · TypeScript · MIT · 推送 2026-02-20 · [GitHub](https://github.com/OskarWieckowicz/genwolf-oss) · [官网](https://www.genwolf.ai) · 组织维护

**监测品牌在 AI 生成回答中出现情况的开源分析平台**

开源 AI 监测平台：用户定义提示词，系统向所选 AI 引擎（OpenAI/Gemini/Perplexity）发起运行，Python worker 从回答中提取提及与引用检测并做品牌/域名富化，结果写入 Postgres 并映射到 Brand Registry，Next.js 仪表盘聚合可见度、引用、声量份额与趋势指标。以 Docker Compose 全栈部署（web、worker、RabbitMQ、Postgres），本地启动需至少一个引擎 API key。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对多个 AI 引擎执行提示词运行并提取品牌提及与引用
- Python worker 做 LLM 处理、品牌检测与富化
- 仪表盘聚合可见度、引用、声量份额、趋势指标
- Docker Compose 一键部署全栈（web/worker/RabbitMQ/Postgres）

## 适用场景

- 追踪我的品牌在 ChatGPT 等 AI 回答中被提及的情况
- 分析不同 AI 引擎中品牌的声量份额与趋势
- 自托管部署做内容策略的数据决策

## 场景标签

 · 领域:AI 监测/分析

## 证据(README 行号)

> L7: Genwolf is an open-source AI monitoring platform that tracks how brands appear inside AI-generated answers. It provi
> L14: 2. Genwolf triggers runs against selected AI engines.
> L17: 5. Dashboard aggregates metrics (visibility, citations, share of voice, trends).

## 星数曲线

```mermaid
xychart-beta
    title "OskarWieckowicz/genwolf-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7b13490e47cc` · [字段定义](../../DATASET.md)*
