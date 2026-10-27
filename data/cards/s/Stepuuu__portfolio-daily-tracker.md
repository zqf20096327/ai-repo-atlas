# Stepuuu/portfolio-daily-tracker

⭐ 47 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Stepuuu/portfolio-daily-tracker) · 个人维护 · 中文 README

**自托管投资组合记录与 Agent 股票研究工作台**

面向个人投资者的自托管工具：多市场（A股/港股/美股）多币种组合追踪、带确认机制的交易账本、CSV 导入与回滚；提供策略回测引擎与手动/Agent 自动股票研究，Agent 在次数与时间预算内规划实验并产出可复现记录。支持 GPT/Claude/DeepSeek 对话，可通过 API 或 Codex/Claude Code 官方登录接入。消息推送依赖 OpenClaw 可选启用；本地 JSON/CSV 存储，导出不自动脱敏。不含期权回测或实盘下单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 需确认的交易账本：费用、碎股、变更预览、CSV 去重导入与备份
- 策略回测：时序分割、标签边界清除、成本与可复现记录
- Agent 自动研究：预算内规划实验、冻结候选并评估最终测试结果
- CLI/HTTP/MCP/Python 注册的扩展接口与持久化任务（取消/重试/调度）

## 适用场景

- 记录每日持仓与交易并自动生成风险指标日报
- 用合成数据学习动量、均值回归等股票日线研究方法
- 让 Agent 在预算内自动跑实验并复盘验证证据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: **Self-hosted portfolio journaling and agent-driven stock research**
> L35: |🤖|AI chat with GPT / Claude / DeepSeek|AI 对话助手|
> L104: Portfolio tracking, the dashboard and stock research run without OpenClaw.

## 星数曲线

```mermaid
xychart-beta
    title "Stepuuu/portfolio-daily-tracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-27 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `895d474e8ffc` · [字段定义](../../DATASET.md)*
