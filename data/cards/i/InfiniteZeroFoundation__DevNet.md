# InfiniteZeroFoundation/DevNet

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/InfiniteZeroFoundation/DevNet) · [官网](https://github.com/InfiniteZeroFoundation)

**在数据所在地联邦训练共享 AI 模型的开放协议**

InfiniteZero 是一个开放协议：参与者在本地设备上用联邦学习训练模型，只共享模型更新而非原始数据，训练轮次由以太坊上的智能合约协调、校验并发放奖励。本仓库为其 DevNet，包含 Solidity 合约（质押/罚没/奖励/公平发行）、dincli 命令行工具、参考 MNIST 模型服务与文档。DevNet 1.0 已在 Optimism Sepolia 测试网运行（测试 ETH），DevNet 2.0 尚未部署；目前仅 MNIST 图像模型完成端到端测试，差分隐私选项默认关闭且尚无正式隐私保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 联邦学习只共享模型更新，原始数据留在本地设备
- 以太坊智能合约协调训练轮次、校验工作并发放奖励
- 含 Solidity 合约、dincli CLI、参考模型服务与文档
- MNIST 模型已端到端测试；可选差分隐私设置（默认关闭）

## 适用场景

- 在 Optimism Sepolia 测试网上运行验证节点或加入训练轮次
- 在网络上训练自己的模型
- 为社区或组织评估该协议的适用性
- 参与协议代码、文档或研究的贡献

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L23: InfiniteZero is an open protocol for training shared AI models on data where it lives. Participants train models on
> L25: This repository is the **DevNet**: the smart contracts, the `dincli` command-line tool, the reference model service

## 星数曲线

```mermaid
xychart-beta
    title "InfiniteZeroFoundation/DevNet 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-28 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `94e8e9e8c056` · [字段定义](../../DATASET.md)*
