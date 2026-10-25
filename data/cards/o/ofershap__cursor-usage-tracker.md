# ofershap/cursor-usage-tracker

⭐ 34 · TypeScript · MIT · 推送 2026-10-12 · [GitHub](https://github.com/ofershap/cursor-usage-tracker) · 个人维护

**Cursor Enterprise 的 AI 成本监控面板：异常检测与 Slack 告警**

自托管的 Next.js 仪表盘，面向使用 Cursor Enterprise 的工程管理、财务与平台团队。通过 Cursor Enterprise Admin API 每小时采集用量数据，存入 SQLite（可替换为 Postgres 等），对每个开发者的支出做四层异常检测（阈值/Z-Score/趋势/昂贵模型切换），异常转为带 MTTD/MTTI/MTTR 指标的 incident，并通过 Slack 或邮件（Resend）告警；提供周期汇总、席位利用与采用率追踪。需 Cursor Enterprise 计划与 Admin API key，支持 Docker/Render/Railway/Fly.io 部署。

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

- 四层异常检测：静态阈值、Z-Score、支出趋势、按请求成本识别昂贵模型切换
- 异常事件全生命周期追踪（MTTD/MTTI/MTTR 指标）
- Slack 告警与 Resend 邮件告警，含计划耗尽提醒与账期周期汇总
- Web 仪表盘：团队总览、模型采用/效率排行、用户下钻、阈值配置

## 适用场景

- 我在账单到达前发现团队里谁在烧高价模型的费用
- 追踪团队 Cursor 席位利用率与 AI 采用情况
- 给每个开发者设支出上限并在异常时收到 Slack 告警

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L29: I built cursor-usage-tracker to fix that. It sits on top of Cursor's Enterprise APIs and gives engineering managers
> L50: It connects to Cursor's Enterprise APIs, collects usage data, and automatically detects anomalies across three laye
> L91: ### Three-Layer Anomaly Detection

## 星数曲线

```mermaid
xychart-beta
    title "ofershap/cursor-usage-tracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e7a83d576787` · [字段定义](../../DATASET.md)*
