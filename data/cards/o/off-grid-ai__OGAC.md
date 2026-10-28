# off-grid-ai/OGAC

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/off-grid-ai/OGAC) · [官网](https://onprem-console.getoffgridai.co) · 组织维护

**企业自托管 AI 治理平台：统一模型网关与合规流水线**

由 Wednesday Solutions 开发的源码可用（source-available）企业 AI 控制平面，部署在自有服务器上。核心组件：统一受治理的模型网关（本地优先，云端路由可选并先做 PII 脱敏）、可组合流水线（绑定模型、评测、黄金集、策略、护栏、漂移）、非技术人员用自然语言在沙箱中构建应用与 agent、人工审批收件箱。治理覆盖确定性拦截、ML 护栏、LLM-as-judge 三层检查，输出签名、带引用、可导出的审计记录，映射 ISO 42001/NIST AI RMF/EU AI Act。多数引擎可经环境变量替换为开源组件（Qdrant、Ragas、LLM Guard 等）。README 同时列出多项未完成项与路线图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一治理网关：路由、护栏、观测、阻断每个模型调用
- 自然语言构建受治理应用/agent，含人工审批与沙箱测试
- 三层护栏（确定性/ML/LLM-as-judge）与签名审计、监管导出
- 引擎可经单个环境变量替换（Qdrant/pgvector/Ragas/LLM Guard/Langfuse 等）

## 适用场景

- 企业在自有基础设施上统一管控各模型的访问、成本与合规
- 非技术业务团队在预设策略内构建 KYC、核保、理赔等应用
- 为监管审计输出签名、带引用、可回溯的运行记录

## 场景标签

`模型网关` `LLM 可观测性` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L90: One governed door to every model: route, guardrail, observe, and kill every call from one place
> L117: - **Gateway.** One governed door to every model. Local by default. Cloud routing is opt-in and masks
> L142: **The governance spine is Off Grid AI's own code, always on.** It is not borrowed from a library.

## 星数曲线

```mermaid
xychart-beta
    title "off-grid-ai/OGAC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `daa8160077db` · [字段定义](../../DATASET.md)*
