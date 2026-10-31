# iblai/financial-services-agents

⭐ 15 · MIT · 推送 2026-06-08 · [GitHub](https://github.com/iblai/financial-services-agents) · [官网](https://ibl.ai/solutions/financial-services) · 组织维护

**面向金融服务公司的 OpenClaw/NemoClaw 多智能体配置包**

ibl.ai 发布的即插即用 agent 配置：一个 Advisory Assistant 编排器加 12 个覆盖合规监控、风险评估、KYC/AML、欺诈调查、监管报送等领域的专家子智能体，通过 git clone 复制到 OpenClaw 沙箱后即可导入。推理依赖 Anthropic API 凭证（需替换占位 key），并内置 11 个第三方平台技能（Bloomberg、FactSet、BlackRock Aladdin、Salesforce 等）供 agent 运行时调用。所有 agent 配置为辅助持牌人员，不独立向客户提供投资建议，并记录审计日志与人工升级规则。MIT 许可。

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

- 1 个编排器 + 12 个金融领域专家子智能体的完整配置
- 11 个第三方平台工具技能（Bloomberg/FactSet/Aladdin/Salesforce 等）
- 零转换导入 NemoClaw 主机，附配置哈希重算与网关重载步骤
- 内置审计日志记录与人工升级规则（CCO/BSA Officer/CISO）

## 适用场景

- 在 OpenClaw/NemoClaw 上快速部署金融服务多智能体团队
- 让合规与风控人员通过对话获取监管监控、KYC/AML 筛查等辅助
- 作为金融机构 agent 架构的参考配置模板

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Drop-in OpenClaw / NemoClaw agent configuration for the ibl.ai **Financial Services** solution segment — one Advisor
> L12: This directory is a complete, drop-in OpenClaw configuration for the **Financial Services** solution segment. It co
> L16: The **Advisory Assistant** (`financial-services-assistant`) is the default entry point. It greets staff, interprets

## 星数曲线

```mermaid
xychart-beta
    title "iblai/financial-services-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `411d400837f7` · [字段定义](../../DATASET.md)*
