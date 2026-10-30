# InditexTech/kumoss

⭐ 94 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/InditexTech/kumoss) · [官网](https://inditextech.github.io/kumoss) · 组织维护

**面向平台工程师：自然语言生成合规 Terraform/OpenTofu PR 的 agentic IaC 工具**

开发者用一句话描述基础设施需求，Kumoss 的 agent 读取现有 IaC 仓库与实际部署状态，生成 Terraform/OpenTofu 兼容 HCL 并反复运行 plan 直到通过，同时把云上漂移回写进代码，最终产出含影响与成本估算的报告并开启 pull request。高危或不合规变更会锁定会话等待管理员审批。支持 AWS/Azure/GCP/OCI/K8s/vSphere 多云，模型通过 LiteLLM 接入（含自托管），身份、IaC 执行器与通知为可替换的 sidecar 服务。本地可 Docker Compose 单机运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言请求 → 生成并验证通过的 Terraform/OpenTofu plan
- 以实际部署为事实源，漂移检测与回写进同一 PR
- 合规 agent 审查，高危/不合规变更需管理员审批
- 模型自选（任意 LiteLLM 支持模型，含自托管），多云支持

## 适用场景

- 开发者自助创建、变更基础设施而无需 HCL 专业知识
- day-2 运维：更新、漂移修复、导入控制台创建的资源
- 在组织治理规则下生成带成本估算与审计记录的 IaC 变更

## 场景标签

`代码生成` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L27: Kumoss turns **natural-language requests into reviewed, compliant Infrastructure as Code (IaC)**. Platform engineer
> L67: |**Model**|—|Any LiteLLM-supported model, including self-hosted ones, with web search included;|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ace3e96d2f23` · [字段定义](../../DATASET.md)*
