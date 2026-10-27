# SAP-samples/btp-a2a-dispute-resolution

⭐ 27 · Python · Apache-2.0 · 推送 2026-06-15 · [GitHub](https://github.com/SAP-samples/btp-a2a-dispute-resolution) · 组织维护

**演示多组织 AI 代理经 A2A 协作解决客户纠纷的示例**

SAP 示例仓库，演示跨组织（SAP/Google/Microsoft）领域代理通过 A2A 协议与 ORD 发现机制协作处理发票纠纷：Joule 作为编排入口，从 Agent Catalog 选取代理、生成任务计划，由纠纷解决、仓储洞察、纠纷邮件等代理分别读取 S/4HANA 数据、分析物流、起草客户邮件。仓库含 ORD 聚合器、A2A 路由器及部署在 BTP/GCP/Azure 的代理代码。自声明为实验性研究/概念验证用途，需 SAP BTP、Cloud Foundry、BAF 订阅及云平台访问权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- A2A 协议代理间通信，ORD 聚合跨目录 Agent Card 实现动态发现
- ord-aggregator 与 a2a-router 提供代理发现与请求路由
- 代理分别部署于 SAP BTP、GCP（Vertex AI/Cloud Run）、Azure（AI Foundry）
- 含分步部署与本地运行教程及演示视频

## 适用场景

- 参考跨组织多代理协作架构搭建 A2A 场景
- 学习 ORD 聚合与 A2A 路由的实现方式
- 在 BTP/GCP/Azure 上复现纠纷处理端到端示例

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: > **Experimental**: The current source code and architecture are experimental, intended for research and proof-of-co
> L7: This repository demonstrates an end-to-end scenario where multiple organizations collaborate through domain-specific
> L50: 1. Provision A2A Agents

## 星数曲线

```mermaid
xychart-beta
    title "SAP-samples/btp-a2a-dispute-resolution 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ed030fb96444` · [字段定义](../../DATASET.md)*
