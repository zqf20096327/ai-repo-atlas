# youngseongshin/thesis-investment-os

⭐ 14 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/youngseongshin/thesis-investment-os) · 个人维护 · 中文 README

**投资 agent 的问责框架：论点卡、预测账本与反馈闭环**

面向投资者与构建者的开源框架，将碎片化市场信息转化为论点卡、决策卡、预测账本与前向收益反馈，形成可事后审计的判断链路。核心循环为：登记预测→不修改论点等待→过程分与结果分分开评级。量化筛选器连接候选队列与滚动 walk-forward 窗口评估。本地优先架构（SQLite+markdown vault），快速入门无需 API key 与付费数据源，捆绑样本 CSV 支持完全离线运行。非自动交易机器人，不承诺 alpha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- thesis/evidence/action/prediction/feedback 分离的判断对象模型
- 过程分与结果分分离的预测账本与滚动前向收益反馈
- 完全离线快速入门（捆绑样本 CSV）与 --live 无密钥 Yahoo/Stooq 模式
- 本地优先知识架构：SQLite + markdown vault + 静态 dashboard

## 适用场景

- 让股票筛选器信号在论点原生持有期内接受前向收益评估
- 为投资决策留下预登记、可审计的预测记录与失效条件
- 本地离线跑通从筛选器到论点卡到反馈闭环的完整流程

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: **Thesis OS is an accountability layer for investment agents.** It is a runnable open-source core that turns fragme
> L52: Bring your own data sources, investing philosophy, watchlists, broker adapters, private notes, and agent prompts. T

## 星数曲线

```mermaid
xychart-beta
    title "youngseongshin/thesis-investment-os 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a688f4922f60` · [字段定义](../../DATASET.md)*
