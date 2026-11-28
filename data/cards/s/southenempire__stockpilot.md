# southenempire/stockpilot

⭐ 10 · TypeScript · MIT · 推送 2026-11-02 · [GitHub](https://github.com/southenempire/stockpilot) · [官网](https://www.stockpilotsol.xyz) · 组织维护

**Solana 上的 24/7 自动化代币化股票配置终端与移动客户端**

以 Anchor 程序为核心的 Solana 非托管 PDA 金库系统：代币化美股篮子采用两层结构，第一层为 USDC 现金储备，第二层为策略篮子；客户端检测漂移后经 Jupiter 路由原子化再平衡，充值含 0.15% 协议费，5 分钟冷却锁。提供 Next.js 终端、Seeker 安卓客户端与 8 项不变量测试。本地运行需 Node.js、pnpm/npm，配置 Helius RPC 环境变量；合约开发需 Rust 与 Solana CLI。

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

- 两层 PDA 金库：USDC 现金储备与策略篮子分离
- 漂移触发再平衡，经 Jupiter v6 原子路由执行
- Privy 嵌入式钱包（Email/Google）与 Phantom/Solflare 支持
- 8 项不变量测试套件与 Devnet 已验证交易签名

## 适用场景

- 在 Solana Devnet 沙箱中模拟代币化股票组合与再平衡
- 一键将现金储备部署为代币化美股篮子
- 在 Solana Seeker 手机上通过 Seed Vault 管理非托管金库

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L23: StockPilot is an autonomous, non-custodial stock robo-advisor running natively on Solana.
> L47: 2. **Layer 2: Active Strategy Baskets** — Tokenized US equity allocations (`xNVDA`, `xAAPL`, `xMSFT`, `xTSLA`) with
> L29: * **Deterministic 2-Layer PDA Vault Architecture:** Separates idle liquidity (Layer 1: 0-risk Vault Cash Reserve in


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `561b8db01094` · [字段定义](../../DATASET.md)*
