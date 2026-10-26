# tradecatlabs-projects/tradecat-public

⭐ 959 · Makefile · MIT · 推送 2026-10-25 · [GitHub](https://github.com/tradecatlabs-projects/tradecat-public) · [官网](https://x.com/tradecat_ai) · 组织维护 · 中文 README

**供 Agent 框架驱动的 Binance 合约纸面交易系统（public-readonly）**

面向 Hermes、Codex、Claude Code 等 Agent 框架的自主交易 loop 的公开层实现：以公开在线表格 signal_flow/anomaly_panel 为信号源，Agent 用仓库内 Binance public-readonly skill/API 快照补全行情上下文并生成交易 thesis，TradeCat 负责 schema 审计、paper/watch 执行、账本、风控拒绝与可复现审计。安全边界明确：只读行情、不读取 Binance key、不签名、不真实下单；缺少 Agent 明确 sizing/杠杆/止损时 fail-closed。提供 Docker Compose 本地隔离容器与 Web 只读监控页，不提供实盘 executor。

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

- 在线表格信号 + Agent thesis + 本地 paper/watch 执行的完整链路
- JSON Schema 约束全部 I/O，SQLite audit journal 可复现审计
- 缺少 Agent sizing/exits 时 fail-closed，不自动填交易参数
- 只读边界：不读密钥、不签名、不下单，实盘 executor 属未来私有仓库

## 适用场景

- 让 Claude Code/Hermes 等 Agent 基于表格信号做合约纸面交易回测
- 以 public-readonly 数据研究 Binance 行情并沉淀交易 thesis
- 本地跑带审计账本与风控拒绝的 paper loop 并用 Web 页监控

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: TradeCat Public 的目标形态是一个可被 Hermes、Codex、Claude Code、OpenClaw 等 Agent 框架驱动的自主交易 loop：先通过公开在线表格信号感知市场异动，后续可扩展其他信号源；再由
> L16: 当前公开仓库实现的是这个目标形态中的 public-readonly + paper/watch 层：公开在线表格只作为信号源；Agent/Hermes 根据仓库内自包含的 Binance skill/API 快照和公开只读工具补
> L27: - 执行本地 paper/watch，不读取 Binance key，不签名，不访问账户/订单私有端点，不真实下单。

## 星数曲线

```mermaid
xychart-beta
    title "tradecatlabs-projects/tradecat-public 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-26"]
    y-axis "stars" 958 --> 960
    line [959, 959]
```

2026-10-22 959 → 2026-10-26 959（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d435f7c70dfa` · [字段定义](../../DATASET.md)*
