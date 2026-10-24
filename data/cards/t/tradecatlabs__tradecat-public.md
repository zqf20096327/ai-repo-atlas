# tradecatlabs/tradecat-public

⭐ — · [GitHub]() · 组织维护 · 中文 README

**面向 Agent 的加密货币自主纸面交易运行时**

TradeCat Public 是供 Agent/Hermes 使用的自主纸面交易运行时：从公开在线表格读取信号，Agent 依据仓库内自包含的 Binance public/read-only skill/API 快照补齐行情上下文与交易 thesis，系统负责 schema 审计、信号对齐、paper/watch 执行、账本、风控拒绝与可复现审计。安全边界严格：不读取 Binance key、不签名、不下真实单；缺少 Agent 明确 sizing/止损等参数时 fail-closed。旧 TUI 与安装器已退役，本地 CLI 渠道暂不可用，指引跳转 web 端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以公开在线表格为信号源的 Agent 纸面交易执行与账本
- Binance public/read-only skill/API 快照供 Agent 研究行情
- JSON Schema 约束各 I/O，输出 SQLite 审计日志与多类报告
- 缺 Agent sizing/leverage/止损时 fail-closed，禁止真实下单

## 适用场景

- 让 AI Agent 基于在线表格信号做可审计的纸面交易回放
- 研究 Agent 交易决策的完整上下文与 thesis 记录
- 在无实盘风险的前提下迭代 paper 风控策略

## 场景标签

`金融量化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: TradeCat Public 是一个面向 Agent/Hermes 的自主纸面交易运行时。公开在线表格只作为信号源；Agent/Hermes 根据仓库内自包含的 Binance skill/API 快照和公开只读工具补齐行情上下
> L16: 本仓库的核心目标是：Agent 交易员同步在线表格作为信号源的自主纸面交易系统。旧的本地交互式 TUI、安装器、watchdog、缓存浏览器和 `project/` 根目录已经退役。

## 星数曲线

```mermaid
xychart-beta
    title "tradecatlabs/tradecat-public 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 958 --> 960
    line [959, 959]
```

2026-10-18 959 → 2026-10-21 959（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `1fdbc23f8bd9` · [字段定义](../../DATASET.md)*
