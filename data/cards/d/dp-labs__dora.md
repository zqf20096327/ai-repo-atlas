# dp-labs/dora

⭐ 25 · WebAssembly · Apache-2.0 · 推送 2026-01-27 · [GitHub](https://github.com/dp-labs/dora) · 组织维护

**面向链上计算与验证的模块化区块链 VM 层（EVM/WASM）**

Dora 是一个模块化机器层，目标是将真实世界计算用例带上区块链，内置 ZK 验证能力。当前处于 MVP 阶段，支持 EVM 与 WASM 规范运行于单一 VM，提供多语言与工具链灵活性（含 Foundry、Hardhat、Rust 工具链示例），并支持与 zkVM 等协处理器协作。编译器基于统一中间表示（IR）层，将代码编译为面向主处理器与协处理器优化的机器码后由 VM 执行。以 Rust 实现，通过 cargo 安装 CLI 或从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 VM 同时支持 EVM 与 WASM 规范
- 内置零知识证明（ZKP）验证
- 统一 IR 层编译器，面向主处理器与协处理器优化
- 与 zkVM 等协处理器原生协作

## 适用场景

- 在链上运行 DEX、游戏等去中心化应用
- 部署需要 ZK 验证的智能合约
- 以多语言（WASM 字节码）开发链上合约

## 场景标签

 · 领域:区块链基础设施

## 证据(README 行号)

> L5: Dora is a modular machine layer designed to bring real-world computing use cases on-chain, featuring in-house ZK ver
> L33: - On-chain AI inference

## 星数曲线

```mermaid
xychart-beta
    title "dp-labs/dora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `df698db99881` · [字段定义](../../DATASET.md)*
