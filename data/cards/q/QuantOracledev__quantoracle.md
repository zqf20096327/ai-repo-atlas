# QuantOracledev/quantoracle

⭐ 13 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/QuantOracledev/quantoracle) · [官网](https://quantoracle.dev) · 个人维护

**面向金融 agent 的 63 个确定性量化计算 API 服务**

以 HTTP API / CLI / MCP 形式提供的量化计算服务：覆盖期权定价、衍生品、风险、组合、统计、加密货币/DeFi、宏观/外汇与货币时间价值共 63 个纯计算器，外加 10 个组合工作流（回测、对冲建议、风险分析等）。计算无数据依赖、输入输出确定，公式经教科书（Hull/Wilmott 等）数值校验并附 120 个精度基准。免费层每日 1,000 次调用无需注册，超出后经 x402 按次付费；另有拉取实时行情的 Live 层与 24/7 持仓监控 Watch 层（付费）。供 AI agent 通过系统提示词、OpenAPI/MCP 等方式接入。

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

- 63 个纯计算器 + 10 个组合工作流，零数据依赖、结果确定可缓存
- 免费层 1,000 次/IP/天，无需 API key，超出经 x402 微支付（Base/Solana）
- 提供 CLI（npm/npx）、MCP 端点、OpenAPI/AI Plugin 发现 URL 与 LangChain cookbook
- 120 个精度基准，公式对照 Hull/Wilmott/Bailey & Lopez de Prado 校验

## 适用场景

- 让金融 agent 调用确定性 API 做期权定价与风险计算
- 终端里快速运行 Black-Scholes、Kelly 等计算（CLI/npx）
- 通过 MCP 端点把量化计算接入 agent 框架
- 注册加密货币永续仓位获得清算距离与资金费率翻转告警

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L2:  The quantitative computation API for autonomous financial agents
> L78: Drop this into your agent's system prompt:
> L93: |**MCP endpoint**|`npx quantoracle-mcp`|

## 星数曲线

```mermaid
xychart-beta
    title "QuantOracledev/quantoracle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `95e236f31aa5` · [字段定义](../../DATASET.md)*
