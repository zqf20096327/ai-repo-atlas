# DataChefHQ/aws-data-landing-zone

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/DataChefHQ/aws-data-landing-zone) · [官网](https://datalandingzone.com) · 组织维护

**面向 AI/数据项目的 AWS 多账户 Landing Zone CDK 构造库**

Data Landing Zone (DLZ) 是一个 AWS CDK construct，提供 TypeScript 与 Python 两种包，用于部署多账户 AWS 基础环境：集成 AWS Organizations、Control Tower、Security Hub、Config、IAM Identity Center、Lake Formation 等服务，管理 VPC 网络、SCP 策略（含 15 个可选 SCP 预设库）、预算与合规报告生成。面向承担 CCoE 职责的云工程与数据工程团队；范围限于 Landing Zone，不涉及应用开发与数据科学任务。采用 wave/stage 分层部署策略，可部署到既有或全新 AWS 组织。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TypeScript 与 Python 双语言的 CDK construct
- 内置 15 个可组合的 SCP 预设（含风险分级标注）
- 集成 Control Tower/Security Hub/Lake Formation/IAM Identity Center 等 AWS 服务
- wave/stage 分层部署策略与合规报告生成

## 适用场景

- 为数据与 AI 项目搭建多账户 AWS 基础环境
- 集中管理账户安全、网络与合规策略
- 企业内实施 CCoE 职责的自动化落地

## 场景标签

 · 领域:云基础设施/数据平台

## 证据(README 行号)

> L5: The **Data Landing Zone (DLZ)** is a CDK construct designed to accelerate AI and data-related projects. It provides 
> L6: opinionated Landing Zone, laying the foundation for a multi-account AWS strategy, so you can focus on delivering dat

## 星数曲线

```mermaid
xychart-beta
    title "DataChefHQ/aws-data-landing-zone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2e862746796c` · [字段定义](../../DATASET.md)*
