# Oz-Networks/fxn-protocol-sdk

⭐ 22 · TypeScript · 推送 2026-09-16 · [GitHub](https://github.com/Oz-Networks/fxn-protocol-sdk) · [官网](https://fxn.world) · 组织维护

**基于 Solana 的 AI agent 间 P2P 通信与资源共享 SDK**

TypeScript SDK，封装 FXN 协议在 Solana 链上的合约调用，供 AI agent 之间建立点对点通信、资源共享与代理发现。核心机制：通过 mintRegistrationNFT 注册数据提供者令牌、createSubscription 创建能力订阅（含时长与接收地址）、renew/cancel 订阅时提交 0-100 质量评分、getAgentSubscribers 查询集群内互联 agent 并以此作为身份认证基础。安装来自 GitHub 仓库，需 AnchorProvider 与 .env 中的 Devnet 合约配置；链上发现面板尚未上线（coming soon）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 注册数据提供者令牌与订阅式访问控制
- 订阅续期/终止时提交 0-100 质量评分
- 查询互联 agent 列表，用于集群（swarm）成员发现与认证
- 基于 AnchorProvider 的 Solana 合约封装，含错误码与 PDA 工具方法

## 适用场景

- 让自己的 agent 向其他 agent 提供数据或服务并管理订阅
- 订阅他人的 agent 能力并按质量评分续约/终止
- 构建自主 agent 集群并查询集群内互联成员

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: An SDK to access FXN Protocol, enabling secure peer-to-peer communication and resource sharing between AI agents on 
> L11: - Peer-to-Peer Agent Communication

## 星数曲线

```mermaid
xychart-beta
    title "Oz-Networks/fxn-protocol-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d9d606917b00` · [字段定义](../../DATASET.md)*
