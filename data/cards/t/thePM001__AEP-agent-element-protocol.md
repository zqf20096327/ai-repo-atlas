# thePM001/AEP-agent-element-protocol

⭐ 12 · Rust · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/thePM001/AEP-agent-element-protocol) · [官网](https://aep.newlisbon.agency) · 个人维护

**为 AI agent 提供确定性零信任输出治理与动作审批的协议库**

AEP v2.9 是一个参考协议实现：在 agent 的工具调用、API 请求、工作流、基础设施变更等输出生效前，由本地 Base Node 内核验证——提案密封为签名胶囊，经 15 项检查墙单次判定，默认拒绝，仅放行合规动作；配套加密传输通道、gVisor 命令沙箱、哈希链审计账本、内容扫描器（密钥/个人数据/注入检测）、模型调用网关与 TLA+ 形式化模型。通过 UCB 桥接入 LangGraph、AutoGen、CrewAI、MCP 等外部系统。面向构建 agent 系统的开发者，Docker 部署或 Rust 源码构建。

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

- 本地 Base Node 内核在动作生效前做确定性验证，默认拒绝
- 15 项检查墙单次判定，结果与检查顺序无关
- Rust CAW 在 gVisor 沙箱中运行 agent 主机命令
- 哈希链审计账本带 Merkle 证明，TLA+ 形式化模型

## 适用场景

- 给 agent 系统加一层动作审批与审计
- 约束 agent 在受限领域内不执行违规输出
- 扫描 agent 提案中的密钥与个人数据泄漏

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L22: AEP (Agent Element Protocol) is an advanced deterministic mechanism for total control of AI output. An agent does n
> L141: **What it is:** The Universal Connect Bridge (UCB) is the airlock for systems outside AEP, for example LangGraph, 
> L50: AEP 2.9 is a reference protocol library: a set of working components a builder attaches to a system. The Base Node 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `9d02ff8744ca` · [字段定义](../../DATASET.md)*
