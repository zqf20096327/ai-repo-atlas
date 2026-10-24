# langchain-ai/helm

⭐ 97 · Shell · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/langchain-ai/helm) · 组织维护

**Kubernetes 上部署 LangChain 应用的 Helm chart 仓库**

由 LangChain Inc. 维护的官方 Helm chart 仓库，提供将 LangChain 应用部署到 Kubernetes 所需的 chart。使用方式：通过 helm repo add 命令将本仓库添加到 Helm 客户端，再安装 chart 完成部署。仓库附有安全策略（SECURITY.md）说明扫描器处理指引与 CVE 报告流程。内容面向已在 Kubernetes 环境中使用 Helm 的运维或开发人员。

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

- 提供部署 LangChain 应用到 Kubernetes 的 Helm chart
- helm repo add 一条命令接入 Helm 客户端
- 附安全策略与 CVE 报告指引

## 适用场景

- 在 Kubernetes 集群中部署 LangChain 应用
- 通过 Helm 标准化交付 LangChain 服务

## 场景标签

 · 领域:LLM 基础设施/部署

## 证据(README 行号)

> L3: This repository contains Helm charts for deploying Langchain applications on Kubernetes.
> L10: helm repo add langchain https://langchain-ai.github.io/helm/

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/helm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-24 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a9b64e9cdbea` · [字段定义](../../DATASET.md)*
