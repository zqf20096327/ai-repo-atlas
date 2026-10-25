# John0n1/ON1Builder

⭐ 37 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/John0n1/ON1Builder) · [官网](https://github.com/John0n1/ON1Builder) · 个人维护

**面向开发者的多链 EVM MEV/套利交易框架**

Python 编写的模块化 MEV searcher 框架，用于在多个 EVM 兼容链上构建和部署套利、抢跑（front-running）、跟跑（back-running）及闪电贷交易策略。机制上支持可配置的 RPC/WebSocket 端点连接任意 EVM 链、滑点上限与 gas 价格上限等安全机制、eth_call/Anvil/Tenderly 三种模拟后端做预执行验证，以及心跳、结构化日志与 Slack/Telegram/Discord/Email 通知。通过 pip 或源码安装，配置 .env 后以 python -m on1builder 运行。README 未描述 AI/ML 功能；公共 WS 端点会禁用 txpool 扫描，非 EVM 链不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置套利、抢跑、跟跑、闪电贷策略，模块化可扩展
- 滑点上限、gas 上限、余额分级与紧急停止等安全机制
- eth_call/Anvil/Tenderly 多种预执行模拟后端
- 心跳、性能摘要与 Slack/Telegram/Discord/Email 通知通道

## 适用场景

- 在 EVM 链上构建并部署套利或 MEV 策略
- 通过模拟后端在执行前验证交易
- 对运行中的 MEV bot 做实时监控与告警

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: ON1Builder is a modular MEV searcher framework designed for building and deploying arbitrage, front-running, and ba
> L18: - **MEV Strategies**: Built-in support for common MEV strategies including arbitrage, front-running, back-running, 

## 星数曲线

```mermaid
xychart-beta
    title "John0n1/ON1Builder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `83e3c8289927` · [字段定义](../../DATASET.md)*
