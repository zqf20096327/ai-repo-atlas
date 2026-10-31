# zTgx/solagent

⭐ 48 · Rust · Apache-2.0 · 推送 2026-05-26 · [GitHub](https://github.com/zTgx/solagent) · 个人维护

**面向 Solana 的 Rust AI agent 工具库，链上操作封装**

以 Cargo crate 形式提供的 Solana AI agent 库：核心包含 solagent-core 与 solagent-wallet-solana 钱包组件，通过 SolanaAgentKit 与 ConfigBuilder 构建 agent。提供 12 个工具与对应插件包，覆盖 Jupiter 交易、pumpfun 发币、Pyth 取价、rugcheck 风控检查、Helius Webhook、Solayer 质押等链上操作，以及 Birdeye/Dexscreener/GoPlus/Cookie 等数据 API。面向在 Solana 上构建 agent 的 Rust 开发者，以 crates.io 分发，按需引入各插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- solagent-core 与 solagent-wallet-solana 组成核心钱包与 agent 构建能力
- 12 个工具/插件包：Jupiter、pumpfun、Pyth、rugcheck、Solayer 质押等
- Birdeye / Dexscreener / GoPlus / Cookie 等数据 API 插件
- 以独立 Cargo crate 分发，可按需组合引入

## 适用场景

- 在 Rust 项目中构建操作 Solana 链上资产的 AI agent
- 为 agent 接入 Jupiter 交易、发币、质押等链上操作
- 通过 rugcheck / GoPlus 等插件获取代币安全与行情数据

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: use solagent_core::{ConfigBuilder, SolanaAgentKit};
> L27: |gibwork|Create a task on Gibwork|solagent-rig-gibwork|Version|Crates Downloads|

## 星数曲线

```mermaid
xychart-beta
    title "zTgx/solagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7884bd4710d6` · [字段定义](../../DATASET.md)*
