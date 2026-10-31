# GoogleCloudPlatform/cortex-framework

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/GoogleCloudPlatform/cortex-framework) · [官网](https://docs.cloud.google.com/cortex/docs/overview) · 组织维护

**面向企业的 Google Cloud 数据基础框架：构建分析用数据产品**

Google Cloud 维护的企业数据框架 v7：基于 BigQuery、Dataform 与 Knowledge Catalog，将 SAP ECC/S/4HANA、SAP Business Data Cloud 等来源的数据经依赖解析与编排转换为数据基础层与数据产品，支持增量加载、多 SAP 系统并行部署与命名空间隔离的扩展机制。AI 相关部分为打包在 .agents/skills/ 的 agent 技能，供 AI 编码助手通过自然语言脚手架化、验证和部署数据产品。部署依赖 Google Cloud 环境，提供 uv 命令行工具与示例 demo 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模块化部署与自动依赖解析，仅处理所需数据
- Dataform 编排的 BigQuery 无服务器增量加载执行
- 面向 agent 的数据产品构建技能（自然语言生成数据资产）
- SAP ECC 与 S/4HANA 多源系统并行支持

## 适用场景

- 在 BigQuery 上搭建 SAP 数据基础并生成分析数据产品
- 通过 AI 助手对话创建和部署数据产品
- 企业数据资产的 Knowledge Catalog 治理与元数据同步

## 场景标签

 · 领域:企业数据分析/数据工程

## 证据(README 行号)

> L3: **Cortex Framework v7** introduces a modular deployment architecture, simple data orchestration via Dataform, and AI
> L13: * **Skills for an agentic data product builder:** Accelerate development by creating new data products simply via n
> L23: * **Serverless BigQuery-native execution:** Orchestration relies entirely on Google Cloud Dataform, which natively 

## 星数曲线

```mermaid
xychart-beta
    title "GoogleCloudPlatform/cortex-framework 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7c02a48d0bee` · [字段定义](../../DATASET.md)*
