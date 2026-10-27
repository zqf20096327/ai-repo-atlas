# anthropics/scone-bench

⭐ 61 · Python · Apache-2.0 · 推送 2026-05-19 · [GitHub](https://github.com/anthropics/scone-bench) · 组织维护

**评测 LLM agent 发现并利用智能合约漏洞的基准（417 任务）**

面向智能合约安全的 LLM agent 基准：417 个任务取自 DeFiHackLabs 等公开历史 DeFi 事件（重入、预言机操纵、访问控制、算术错误等），每个任务在本地 anvil 分叉节点上呈现一个真实 EVM 合约，要求 agent 找出缺陷并编写 Solidity FlawVerifier 合约，其 executeOnOpportunity() 需提取 ≥0.1 原生代币利润。评分前重启 anvil 进程防止作弊。通过 Docker 容器与 MCP/stdio 协议运行，需归档节点 RPC、Etherscan 与模型提供商 API key。README 声明不再维护、不接受贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 417 个任务取自公开历史 DeFi 安全事件
- MCP 服务器暴露 setup_problem/grade_problem，可接入任意 MCP 兼容客户端
- 评分前重启 anvil 进程，仅链上真实可获利的利用可通过
- 提供训练截止期后的 12 事件子集用于评价新模型

## 适用场景

- 评测 LLM agent 在智能合约漏洞发现与利用上的能力
- 用截止期后子集对训练数据之后的事件做盲测
- 通过 MCP 协议手动检查单个任务或接入自研 agent 循环

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: > **Benchmark.** Not maintained and not accepting contributions.
> L5: A benchmark for evaluating LLM agents on **smart-contract vulnerability discovery and exploitation**. Each of the 41

## 星数曲线

```mermaid
xychart-beta
    title "anthropics/scone-bench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-27 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c3ca707acd67` · [字段定义](../../DATASET.md)*
