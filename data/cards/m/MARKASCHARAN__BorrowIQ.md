# MARKASCHARAN/BorrowIQ

⭐ 15 · TypeScript · 推送 2026-03-09 · [GitHub](https://github.com/MARKASCHARAN/BorrowIQ) · [官网](https://borrowiq.vercel.app) · 个人维护

**给 DeFi 借贷用户的链上信用评分与动态定价协议**

构建在 Creditcoin 网络上的 DeFi 借贷协议，用 AI 链上信用引擎替代超额抵押：Python/FastAPI 后端分析钱包链上历史（交易数、钱包年龄、余额）生成信用评分，据此动态确定利率与额度；还款成功后 LoanManager 合约自动提升链上信用分；AI 后端为新钱包代付测试网 Gas。架构由 React 前端、链下 Python AI Oracle 与四个 Solidity 合约（已部署于 CC3 测试网）组成，本地运行需 MetaMask 或 Wagmi 支持的钱包切换到测试网。项目自述为 hackathon 作品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于钱包链上行为生成信用评分，动态定价利率与额度
- 还款后 LoanManager 合约自动提升链上信用分
- Account Abstraction 方式为新钱包代付测试网 Gas
- 四个合约已部署于 Creditcoin CC3 测试网并给出地址

## 适用场景

- 在 Creditcoin 测试网以信用评分获得无需超额抵押的借贷
- 通过按时还款逐步积累链上信用并解锁更低利率
- 开发者参考其信用评分合约与 AI Oracle 架构

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L15: **BorrowIQ** is a next-generation DeFi lending protocol built on the **Creditcoin Network** that replaces capital-i
> L21: 1. **🧠 AI Credit Scoring:** Our Python/FastAPI backend analyzes a wallet's on-chain history (transaction counts, wa
> L28: BorrowIQ utilizes a 4-layer architecture coordinating the user's wallet, the React frontend, the off-chain Python A


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `2ff2cacc274d` · [字段定义](../../DATASET.md)*
