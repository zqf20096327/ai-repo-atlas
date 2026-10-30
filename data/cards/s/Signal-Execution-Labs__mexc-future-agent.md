# Signal-Execution-Labs/mexc-future-agent

⭐ 87 · Shell · MIT · 推送 2026-09-14 · [GitHub](https://github.com/Signal-Execution-Labs/mexc-future-agent) · 组织维护

**MEXC USDT 永续合约规则化交易机器人（Node CLI）**

TypeScript Node 命令行程序，面向 MEXC USDT 本位永续合约（contract.mexc.com）做规则化自动交易。内置两种策略：9/21 SMA 均线交叉（RSI 过滤）与网格；提供 dry-run 模拟模式、名义风险上限（RISK_MAX_POSITION_USDT 等）与杠杆配置。通过 Open API 密钥或网页会话 cookie 认证，需 Node.js 20+ 与足额 USDT 保证金。仓库描述称兼容 Claude Code 与 OpenAI Codex 作为 agent 工具使用，README 正文未展开该部分。

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

- 内置 ma-cross（9/21 SMA + RSI 过滤）与 grid 两种策略
- dry-run 干跑模式与名义风险上限参数
- 支持 Open API 凭证或网页会话 key/cookie 两种认证
- 长运行策略循环（npm run bot）

## 适用场景

- 在 MEXC USDT 永续合约上运行均线交叉或网格策略
- 用 dry-run 模式先行验证策略行为
- 在 Claude Code / OpenAI Codex agent 中调用 MEXC 交易能力

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: TypeScript Node CLI for rule-based automation on MEXC USDT-margined perpetual contracts (`contract.mexc.com`). Ships
> L22: |`npm run bot`|Long-running strategy loop (`BOT_DRY_RUN=true` recommended first).|

## 星数曲线

```mermaid
xychart-beta
    title "Signal-Execution-Labs/mexc-future-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-30 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `2641ae84fdd2` · [字段定义](../../DATASET.md)*
