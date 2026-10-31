# axem-solutions/shaide

⭐ 42 · Go · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/axem-solutions/shaide) · [官网](https://www.axem.dev/) · 组织维护

**面向企业的自托管分布式多模型 LLM 推理平台**

部署在用户自有 Kubernetes 集群上的自托管 AI 平台：以 vLLM 为推理引擎、llm-d 做多实例编排，并行服务生成式与嵌入模型，支持多副本独立扩缩与多模型路由，暴露 OpenAI 兼容 API。各层均为 Pulumi 基础设施即代码，通过交互式终端安装器单命令安装，内部 OCI 注册表镜像所有镜像与模型权重，支持完全离线的气隙部署。面向数据不得离开自有基础设施的受监管行业、国防、公共部门等组织。仓库自述处于早期访问阶段，接口与模块布局可能在版本间变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- vLLM + llm-d 的分布式多模型推理，各模型独立扩缩
- Pulumi 基础设施即代码，全平台可版本化复现
- 交互式安装器单命令安装，支持气隙离线部署
- OpenAI 兼容 API，现有 SDK 与 agent 框架仅需改 base URL

## 适用场景

- 在自有 Kubernetes 集群上并行服务多个 LLM 与嵌入模型
- 受监管行业或气隙环境内部署不离境的 AI 基础设施
- 为多个并发 agent 提供统一的多模型路由端点

## 场景标签

`推理引擎` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L23: shaide is a self-hosted AI platform that serves AI models at scale on your
> L53: - **Distributed multi-model serving.** vLLM as the inference engine,

## 星数曲线

```mermaid
xychart-beta
    title "axem-solutions/shaide 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2facf19c9cde` · [字段定义](../../DATASET.md)*
