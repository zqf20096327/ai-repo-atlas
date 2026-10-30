# OriginTrail/dkg

⭐ 141 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/OriginTrail/dkg) · [官网](https://origintrail.io) · 组织维护

**面向多智能体的去中心化知识图谱共享记忆节点**

OriginTrail DKG V10 是一个 monorepo，包含节点软件、CLI、仪表盘 UI、协议包、适配器与工具，用于运行 DKG 节点并加入网络。它为多智能体 AI 系统提供三层可验证记忆（本地工作记忆 → 共享工作记忆 → 链上锚定的可验证记忆），知识以 RDF 三元组构成的 Knowledge Asset 形式发布，通过 Merkle 根锚定区块链以校验完整性，Context Graph 提供访问控制与 M-of-N 多签治理。提供 Hermes、OpenClaw 适配器与 MCP 接入（Cursor/Claude Code/Codex 等），支持独立节点模式。运行需要 Node.js 22+，链上发布需 gas 与 TRAC。

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

- 三层记忆架构：WM/SWM/VM，知识由私有逐步晋升为链上锚定记录
- Knowledge Asset 以 Merkle 根锚定区块链，支持内容完整性校验与生命周期审计
- Context Graph 提供访问控制与 M-of-N 链上多签治理
- Hermes/OpenClaw 适配器与 MCP 客户端接入（dkg setup 两条命令完成配置）

## 适用场景

- 让多个 AI agent 共享跨会话持久的知识图谱记忆
- 为 agent 产出的知识附加链上可验证的出处与完整性证明
- 通过 MCP 让 Cursor/Claude Code/Codex 等客户端使用 DKG 记忆

## 场景标签

`Agent 记忆` `多智能体` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L14: The Decentralized Knowledge Graph V10 is the shared, verifiable memory layer for multi-agent AI systems. Every find
> L20: Any AI agent — whether built with OpenClaw, ElizaOS, Hermes, or any custom framework — can run a DKG node and start
> L113: ### Model Context Protocol (MCP)


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6613d968310c` · [字段定义](../../DATASET.md)*
