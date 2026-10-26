# muratmula/ai-robinhood-chain

⭐ 134 · TypeScript · MIT · 推送 2026-09-14 · [GitHub](https://github.com/muratmula/ai-robinhood-chain) · 个人维护

**面向 Robinhood Chain L2 的多 agent 加密货币筛选与交易信号机器人**

Node.js/TypeScript 构建的自主多 agent 加密情报与交易系统，专用于 Robinhood Chain（EVM L2，链 ID 4663）。五个专项筛选 agent 24/7 运行（meme、LP、NFT、alpha、ETH 巨鲸），信号需通过 3 层 Swarm 共识（≥80% 置信度）与安全审计后才以卡片形式投递；执行与筛选分离，默认 DRY_RUN。通过 Discord 命令中心（22 个斜杠命令）、Terminal TUI 与 Telegram 桥接操作，提供 PM2 守护进程部署、自更新、CLI 诊断与交互式配置向导。README 声明为实验性研究工具并附金融风险免责声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5 个专项筛选 agent 24/7 运行，覆盖 meme/LP/NFT/alpha/ETH 巨鲸场景
- 3 层 Swarm 共识引擎，信号需 ≥80% 置信度且安全门 fail-closed
- Discord 命令中心 22 个斜杠命令 + Terminal TUI + Telegram 桥接三端操作
- PM2 24/7 部署、opencatz update 自更新、doctor 诊断等运维 CLI

## 适用场景

- 在 Robinhood Chain 上接收经共识门控的代币/NFT/LP 交易信号卡片
- 通过 Discord 对话或 TUI 管理筛选 agent、钱包与持仓风控
- 用自然语言自定义筛选策略并自动编译为策略模块

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Autonomous Multi-Agent Crypto Intelligence & Trading Ecosystem** — built exclusively for **Robinhood Chain (EVM L
> L41: |🐾 **OpenCatz Core** — Intelligence|Screening & Reasoning|**3-Layer Swarm Consensus Engine** (Quant & Liquidity, Ca
> L63: |6|💬 **Natural-Language Command Room**|Chat with OpenCatz in `#opencatz-control-room` — swap/send intents, audits, 

## 星数曲线

```mermaid
xychart-beta
    title "muratmula/ai-robinhood-chain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-26 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6ef1e1a21ab4` · [字段定义](../../DATASET.md)*
