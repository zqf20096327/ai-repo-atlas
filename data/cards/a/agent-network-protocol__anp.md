# agent-network-protocol/anp

⭐ 354 · Rust · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/agent-network-protocol/anp) · [官网](https://agent-network-protocol.com/) · 组织维护 · 中文 README

**Agent Network Protocol (ANP) 多语言 SDK，实现智能体互联互信与通信**

ANP 协议的多语言 SDK 与参考实现仓库，覆盖身份、发现、调用、验证与加密通信：DID WBA 去中心化身份与 HTTP 消息签名认证、Agent Description 与 OpenRPC/JSON-RPC 接口发布、W3C Data Integrity 证明、WNS 人类可读句柄解析、端到端加密（直连 P5 与群组 MLS P6）及 AP2 支付协议。Python 提供快速构建智能体的 OpenANP，另含 Go/Rust/Dart/TypeScript/Java SDK，Java 仅可从本地 Maven 构建使用。

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

- DID WBA 身份、签名认证与验证工具
- OpenANP 从 Python 类型提示生成可发现的 OpenRPC/JSON-RPC 接口
- W3C Data Integrity 证明与 WNS 句柄解析绑定
- 直连与群组（MLS）端到端加密构件及跨语言互操作测试向量

## 适用场景

- 快速构建可被其他智能体发现和调用的 ANP 智能体
- 为 HTTP 服务添加 DID WBA 认证
- 跨语言实现智能体间的身份验证、接口发现与加密通信

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: AgentConnect is the multi-language SDK and reference implementation for the Agent Network Protocol (ANP). It helps a
> L23: - **Python agent SDK**: OpenANP for quickly building and calling ANP agents, plus authentication, proof, WNS, AP2, 
> L180: |anp/|Python package: OpenANP, authentication, proof, WNS, AP2, crawler, E2EE, and meta-protocol modules.|

## 星数曲线

```mermaid
xychart-beta
    title "agent-network-protocol/anp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 352 --> 354
    line [353, 353]
```

2026-10-18 353 → 2026-10-24 353（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f8bb4f544e89` · [字段定义](../../DATASET.md)*
