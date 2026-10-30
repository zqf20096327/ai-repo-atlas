# g-clouds/ANS

⭐ 28 · JavaScript · Apache-2.0 · 推送 2025-12-29 · [GitHub](https://github.com/g-clouds/ANS) · [官网](http://g-clouds.github.io/ANS/) · 组织维护

**AI agent 发现与信任验证的开放规范与配套基础设施**

Agent Network System（ANS）是一套开放规范及配套实现，为 AI agent 生态提供类似 DNS 的发现服务与多级信任验证（Basic/Standard/Blockchain），定位为 A2A、ACP、MCP 等通信协议之下的基础层。架构混合集中式发现服务与去中心化信任层，采用零信任模型、支持 DIDs/gRPC/AIBOM 与后量子密码（NIST ML-DSA）。提供 JS/Java/Python SDK、anslookup CLI、CopilotKit 适配器，后端可经 Terraform 部署到 GCP（Cloud Run + Docker）。注意：当前 SDK 兼容 v0.1.1，规范仍在演进中。

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

- 类 DNS 的 agent 全局发现与多级信任验证（Basic/Standard/Blockchain）
- 提供 npm/Maven/PyPI 三语言 SDK 与 anslookup CLI
- CopilotKit 适配器与示例工程，协议无关设计
- Terraform 一键部署到 GCP（Cloud Run + Docker 镜像）

## 适用场景

- 让不同协议的 AI agent 在互联前互相发现并验证身份
- 为 A2A/ACP/MCP 通信补充发现与信任层
- 用 anslookup CLI 查询注册的 agent 及其能力与信任等级

## 场景标签

 · 领域:AI agent 基础设施

## 证据(README 行号)

> L7: An open specification for a foundational hybrid architecture enabling secure discovery, multi-level trust, and confi
> L9: The Agent Network System (ANS) addresses a fundamental need as AI agents proliferate: a reliable and secure way for 
> L158: ANS is designed as a foundational layer that enhances and supports a diverse range of agent communication and inte

## 星数曲线

```mermaid
xychart-beta
    title "g-clouds/ANS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f036ea53a9b4` · [字段定义](../../DATASET.md)*
