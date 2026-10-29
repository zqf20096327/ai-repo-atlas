# BradMoonUESTC/finite-monkey-engine

⭐ 360 · Python · 推送 2026-01-06 · [GitHub](https://github.com/BradMoonUESTC/finite-monkey-engine) · 个人维护

**面向区块链与系统级代码的 AI 安全审计引擎**

安全分析流水线，按 Planning → Reasoning → Validation 三阶段执行代码审计：用 Tree-sitter 做函数级解析，通过 Codex CLI 提取业务流并执行扫描，输出多漏洞 JSON，结果持久化到 PostgreSQL 并可导出报告。聚焦 Solidity/Rust/C++/Move 四种核心语言（Go 部分支持），面向智能合约、DeFi 协议与区块链基础设施项目。需配置 AI API Key（支持 OpenAI/Claude/DeepSeek 兼容服务）与 PostgreSQL 13+，通过 git clone 源码加 python 运行。v3.0 移除了 RAG/chunk/调用图等机制，改用 Codex CLI 主导执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Planning → Reasoning → Validation 三阶段审计流水线
- Tree-sitter 函数级解析 + Codex CLI 业务流提取与扫描
- 结果持久化 PostgreSQL，可导出 xlsx 报告与 Mermaid 业务流图
- 聚焦 Solidity/Rust/C++/Move 四种核心语言

## 适用场景

- 审计以太坊/Solana/Aptos/Sui 智能合约的安全漏洞
- 审查 DeFi 协议的 AMM、借贷与治理机制
- 对区块链节点与 TEE 等系统级 C/C++ 代码做安全分析

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: Security analysis pipeline for code auditing: **Planning → Reasoning → Validation**.
> L27: Finite Monkey Engine is an advanced AI-driven code security analysis platform **focused on blockchain and system-le

## 星数曲线

```mermaid
xychart-beta
    title "BradMoonUESTC/finite-monkey-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 359 --> 361
    line [360, 360]
```

2026-10-18 360 → 2026-10-29 360（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a6d2bca1d452` · [字段定义](../../DATASET.md)*
