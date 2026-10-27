# Routstr/protocol

⭐ 42 · MIT · 推送 2026-01-05 · [GitHub](https://github.com/Routstr/protocol) · [官网](https://routstr.com) · 组织维护

**去中心化 AI 推理网络的技术规范文档集（RIPs）**

Routstr Improvement Protocols（RIPs）是模块化规范文档集合，定义去中心化 AI 推理网络的事件、行为与接口。内容覆盖 OpenAI 兼容代理与 Cashu 微支付（RIP-01）、基于 Nostr 的提供方发现（RIP-02）、客户端行为标准（RIP-03）、审计与定价（RIP-04/05）、路由算法（RIP-06）、节点管理 API（RIP-07）、多种比特币支付通道（RIP-08）、模型评测（RIP-09）、去中心化订单簿市场（RIP-10）及专用节点配置（RIP-11）。面向实现该协议的开发者，每个 RIP 以独立文件提供实施指引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个模块化规范覆盖支付、发现、路由、审计、定价等环节
- 定义 Nostr 事件类型（Kind 38421/38000）用于提供方公告与推荐
- 以 Millisats 为记账单位的定价与客户端验证标准
- 支持 Lightning/NWC/Bolt12/链上比特币等多种注资方式

## 适用场景

- 实现 Routstr 协议的节点或客户端开发者查阅接口规范
- 构建集成闪电网络微支付的 OpenAI 兼容代理
- 了解去中心化推理市场的订单簿与路由机制设计

## 场景标签

 · 领域:去中心化 AI 网络/协议规范

## 证据(README 行号)

> L5: Routstr Improvement Protocols (RIPs) are modular specification documents defining the events, behaviors, and interfa
> L11: |RIP-01|Proxy / Payments|Standard for OpenAI-compatible API Proxy with integrated Cashu micropayments.|

## 星数曲线

```mermaid
xychart-beta
    title "Routstr/protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a7e67a5a0428` · [字段定义](../../DATASET.md)*
