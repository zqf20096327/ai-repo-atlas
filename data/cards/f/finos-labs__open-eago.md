# finos-labs/open-eago

⭐ 22 · Python · Apache-2.0 · 推送 2026-09-08 · [GitHub](https://github.com/finos-labs/open-eago) · [官网](https://openeago.finos.org/) · 组织维护

**受监管企业多智能体系统的治理与合规控制平面规范**

由 FINOS Labs 发布的开放规范（v0.1，Citi 作者），定位为 A2A/MCP/AGNTCY-OASF/SPIFFE 之上的治理与合规叠加层：规范定义六个阶段（合约管理、规划协商、验证合规、执行韧性、上下文状态、通信交付），覆盖 GDPR/DORA/EU AI Act 等辖区感知策略执行、人在环审批门、跨境数据许可、四维复合风险评分与审计锚定。线级传输委托给 A2A 与 MCP，支持 LangChain、LangGraph 及自定义 agent。当前为规范文档，未见可安装实现。

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

- 六阶段治理规范，覆盖策略执行、HITL 审批、跨境数据许可与审计锚定
- 四维复合风险评分（财务/运营/合规/安全）含硬停阈值
- 委托 A2A 传输与 MCP 工具调用，作为叠加层而非平行协议栈
- 声明框架无关，支持 LangChain/LangGraph/自定义 agent/遗留系统封装

## 适用场景

- 受监管行业（金融等）为多智能体系统补充合规控制平面
- 在多 agent 工作流中强制高风险任务的人工审批与审计留痕
- 跨辖区部署 agent 时执行数据驻留与主权校验

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Enterprise Agent Governance & Orchestration (OpenEAGO)** is an open specification for the **governance and compli
> L19: OpenEAGO is not a parallel protocol stack. It is a **profile and governance overlay** that runs on top of A2A trans

## 星数曲线

```mermaid
xychart-beta
    title "finos-labs/open-eago 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0f6b3633af1e` · [字段定义](../../DATASET.md)*
