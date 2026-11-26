# KumailQazi/krmaazha-binance-mcp

⭐ — · [GitHub]() · 个人维护

**面向加密交易者的 Binance MCP 服务器，人审后才可下单**

一个 Model Context Protocol 服务器，将任意 MCP 客户端接入 Binance 账户，暴露 26 个工具、5 个分析师提示与 8 个知识资源，覆盖行情、技术指标、新闻情绪、衍生品持仓、组合/风险分析与信号生成。采用双进程安全模型：MCP 服务器持只读密钥仅可提议订单，独立运行的 confirmer 进程持交易密钥，订单须经用户物理点击确认才执行。另含离线 USD-M 期货研究引擎（[research] extra）。支持 testnet 起步。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双进程人审机制：服务器只读提议，confirmer 持交易密钥且需物理点击才执行
- 26 个工具覆盖行情、指标、情绪、衍生品、组合风险与回测
- 8 个 kb:// 知识资源与 5 个分析师 playbook 提供方法论
- 离线 USD-M 期货研究引擎，无密钥读取公开归档数据

## 适用场景

- 让 Claude 等 AI 助手读取和分析 Binance 行情
- AI 提议现货订单，本人确认后执行
- 对策略信号与 DCA 计划做无前视偏差回测
- 研究已退市永续合约的生存偏差无关面板数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L23: `krmaazha-binance-mcp` is a Model Context Protocol server
> L59: |**MCP server** `krmaazha-binance-mcp`|your MCP client (stdio)|**read-only** (`BINANCE_READ_*`)|reads, pre-validate

## 星数曲线

```mermaid
xychart-beta
    title "KumailQazi/krmaazha-binance-mcp 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-10-23 4 → 2026-11-25 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `bb6aedbb098f` · [字段定义](../../DATASET.md)*
