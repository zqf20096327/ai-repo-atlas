# chainstacklabs/pumpfun-cli

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/chainstacklabs/pumpfun-cli) · 组织维护

**pump.fun 代币发行与交易的命令行工具**

Chainstack 团队开源的独立 CLI，用于在 Solana 上的 pump.fun 发币、买卖代币、查询代币信息与钱包管理。设计为无状态，面向人类、脚本与 LLM agent 三类使用者，另有配套的 agent 交易 skill。命令分为发现类（浏览/搜索代币，零配置）与交易类（买卖/launch/迁移，需 Solana RPC）。私钥以 AES-256-GCM + scrypt 加密存储。安装需 uv 与 Python 3.12+，支持 macOS/Linux/Windows(WSL)。

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

- 无状态 CLI，面向人类、脚本与 LLM agent 使用
- 代币发现命令零配置即可使用
- 本地钱包管理，私钥 AES-256-GCM + scrypt 加密
- 配套 Claude Code agent 技能与 hooks（自动 lint、密钥防护）

## 适用场景

- 通过命令行浏览与搜索 pump.fun 上的新代币
- 脚本化执行代币的买卖、发行与迁移操作
- 让 LLM agent 调用 CLI 执行 pump.fun 交易

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: Built from experience developing pumpfun-bot, distilled into a stateless CLI designed for humans, scripts, and LLM a
> L7: > Check out also our skill for trading on pump.fun with OpenClaw and other agents.

## 星数曲线

```mermaid
xychart-beta
    title "chainstacklabs/pumpfun-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `06bdac2cca1c` · [字段定义](../../DATASET.md)*
