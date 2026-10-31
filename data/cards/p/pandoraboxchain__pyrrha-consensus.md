# pandoraboxchain/pyrrha-consensus

⭐ 25 · Solidity · MIT · 推送 2026-06-24 · [GitHub](https://github.com/pandoraboxchain/pyrrha-consensus) · [官网](http://pandoraboxchain.ai) · 组织维护

**Pandora Boxchain 共识层的以太坊智能合约集**

以 Solidity 实现的以太坊合约集合，实现 Pandora 白皮书中定义的第一层共识机制 Proof of Cognitive Work（PoCW），核心合约为 Pandora.sol，实现 Pandora Protocol Specification。当前为受限实现，首个认知网络实现代号 Pyrrha 开发中。部署在本地 Ganache、Ropsten/Rinkeby 测试网及 RSK 测试网上验证，提供 npm 脚本执行 lint、测试与覆盖率检查；已知问题为 Ropsten 区块 gas 上限导致 createWorker() 调用多数失败。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 实现白皮书 3.3 节 Proof of Cognitive Work 共识
- 核心合约 Pandora.sol，实现 Pandora Protocol Specification
- 部署在 Ganache、Ropsten、Rinkeby 与 RSK 测试网验证

## 适用场景

- 搭建 Pandora Boxchain 认知网络的第一层共识合约
- 研究 PoCW 共识机制的智能合约实现
- 在测试网上验证认知工作共识合约的部署与调用

## 场景标签

 · 领域:区块链/去中心化 AI 基础设施

## 证据(README 行号)

> L5: Core set of Ethereum contracts for Pandora Boxchain implementing the first level of consensus.
> L7: "3.3. Proof of Cognitive Work (PoCW)" in Pandora white paper

## 星数曲线

```mermaid
xychart-beta
    title "pandoraboxchain/pyrrha-consensus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c8391497b597` · [字段定义](../../DATASET.md)*
