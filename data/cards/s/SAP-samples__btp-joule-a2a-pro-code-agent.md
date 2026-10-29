# SAP-samples/btp-joule-a2a-pro-code-agent

⭐ 22 · TypeScript · Apache-2.0 · 推送 2026-05-20 · [GitHub](https://github.com/SAP-samples/btp-joule-a2a-pro-code-agent) · 组织维护

**SAP BTP 上 A2A 协议 Pro-Code Agent 端到端参考实现**

SAP 团队提供的企业级参考实现，演示在 SAP BTP 上用 TypeScript + CAP + LangGraph 构建的 A2A 协议合规 Pro-Code Agent，通过 SAP Cloud SDK for AI 接入 Generative AI Hub 模型，并将 Joule 作为 A2A 客户端集成。附带 WebSocket/Webhook 异步推送与 React 状态展示、Terraform 全套基础设施代码，以及用 SAP-RPT-1 模型做报价评分与预测（付款延迟、转化概率）的销售询价优化示例用例。含 Human-in-the-Loop 与自定义扩展示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- A2A 协议合规的 Pro-Code Agent（TypeScript + CAP + LangGraph）
- Joule 作为 A2A 客户端的出站集成（agent-request）
- Terraform 端到端开通 BTP 子账户、Cloud Foundry、AI Core、HANA 等
- RPT-1 作为工具用于报价评分与预测（转化概率/付款延迟）

## 适用场景

- 参考其架构在 SAP BTP 上构建企业级 AI Agent
- 实现 Joule 与自建 Agent 间的 A2A 委派集成
- 学习 Agent 的 Webhook 异步通知与 Human-in-the-Loop 模式

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: This repository serves as a **reference implementation** for building enterprise-grade, "Pro-Code" Agents on the SAP
> L29: |**Pro-Code AI Agent Implementation**|✅ **Done**|Built using **LangGraph** (TypeScript) on **CAP**, integrated with

## 星数曲线

```mermaid
xychart-beta
    title "SAP-samples/btp-joule-a2a-pro-code-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d6f588d38873` · [字段定义](../../DATASET.md)*
