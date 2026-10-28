# thangchung/coffeeshop-agent

⭐ 36 · C# · MIT · 推送 2025-11-28 · [GitHub](https://github.com/thangchung/coffeeshop-agent) · 个人维护

**.NET 多智能体咖啡店演示应用（MAF/MCP/A2A/AG-UI）**

基于 .NET 的演示型 AI Agents 应用：以咖啡店点单为场景，集成 Microsoft Agent Framework 的工作流编排（ValidatorExecutor/SplitExecutor 等节点）、对外暴露 MCP 服务（SSE 端点，可用 MCP Inspector 调试）、A2A 协议（通过 agentgateway 暴露 agent.json）与 AG-UI。身份层使用 Microsoft Entra ID，A2A 部分需设置 GEMINI_API_KEY 运行 agentgateway。README 明确声明这是演示应用，不建议用于生产或复制部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Microsoft Agent Framework 工作流编排咖啡店点单流程
- 暴露 MCP SSE 端点并可配合 MCP Inspector 调试
- 通过 agentgateway 支持 A2A 协议（.well-known/agent.json）
- 基于 .NET Aspire 运行并提供 Dashboard

## 适用场景

- 学习 .NET 技术栈下多智能体协议（MCP/A2A/AG-UI）的集成方式
- 参考 Microsoft Agent Framework 工作流编排的实现示例
- 调试 MCP 服务端点与 A2A agent 发现机制

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L2: .NET Agents technologies
> L59:   ValidatorExecutor["ValidatorExecutor (Start)"];

## 星数曲线

```mermaid
xychart-beta
    title "thangchung/coffeeshop-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `f1ed8126f657` · [字段定义](../../DATASET.md)*
