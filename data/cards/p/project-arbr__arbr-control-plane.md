# project-arbr/arbr-control-plane

⭐ 29 · JavaScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/project-arbr/arbr-control-plane) · [官网](https://projectarbr.org/) · 组织维护

**自托管 LLM 网关与治理控制平面：观测调用、推荐可审批回滚的路由优化**

面向生产环境 AI 流量团队的自托管模型优化与治理控制平面。按应用/工作流/任务归因成本、延迟与模型选择，发现高价模型可换廉价候选的机会，用代表性流量构建评测集对比候选模型，人工批准后以可回滚规则、影子评测或金丝雀方式发布，并记录请求与实际服务模型以核验节省效果。可作为 OpenAI 兼容网关独立运行，或置于 LiteLLM 之前；开发者显式固定的模型不被改写，预算可告警/降级/阻断。提供 Docker Compose 一键部署与 Node 本地运行两种方式，另发布 arbr-client（npm/PyPI）与 arbr-audit CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六步优化闭环：观测→发现机会→构建证据→评测候选→人工批准发布→核验结果，全程可回滚
- OpenAI 兼容端点可直接替换 OpenAI chat API，支持 SSE 流式透传
- 可与现有 LiteLLM 代理叠加，置于其前增加观测、路由与治理
- 模型注册表（MongoDB）驱动成本跟踪、推荐与护栏降级，未注册模型可 pass-through

## 适用场景

- 归因分析生产 LLM 流量的成本、延迟与模型使用情况
- 在人工审批下把部分工作负载切换到更廉价模型并核验实际节省
- 为现有 LiteLLM 网关增加治理、评测与预算控制层
- 审计请求日志中的高价模型滥用

## 场景标签

`模型网关` `LLM 可观测性` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L20: Arbr is a self-hosted **model optimisation and governance control plane** for teams with
> L25: Arbr can run as a standalone OpenAI-compatible gateway or in front of infrastructure you
> L26: already use, including LiteLLM. Provider connectivity is the foundation; the product is the

## 星数曲线

```mermaid
xychart-beta
    title "project-arbr/arbr-control-plane 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ba7037210fc2` · [字段定义](../../DATASET.md)*
