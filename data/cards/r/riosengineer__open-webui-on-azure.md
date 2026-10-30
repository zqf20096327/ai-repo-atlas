# riosengineer/open-webui-on-azure

⭐ 67 · Bicep · 推送 2026-01-10 · [GitHub](https://github.com/riosengineer/open-webui-on-azure) · [官网](https://rios.engineer/open-webui-on-azure-part-1-architecture-deployment/) · 个人维护

**在 Azure 上生产化部署 Open WebUI 的参考架构与快速启动代码**

提供一套 Bicep 基础设施即代码与部署流程，将 Open WebUI 部署到 Azure Container Apps，集成 Entra ID OAuth/OIDC 认证、Azure API Management 作为 AI 网关（含 token 限额与用量指标）、Microsoft Foundry 多模型后端（GPT/Grok/Mistral/Llama/DeepSeek）、Application Gateway SSL 终结与私有端点的 PostgreSQL 持久化。面向拥有 Azure 订阅 Owner 权限的 DevOps/平台工程师，需自有域名与 SSL 证书，分三步部署 hub/app/重部署并手工导入 OpenAPI 规范到 APIM。全程用 Managed Identity，不存储密钥（Azure File SMB 挂载除外）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bicep + Azure Verified Modules 全套基础设施即代码
- APIM 作为 AI 网关：token 跟踪、限额、用量指标、Entra OAuth 策略校验
- Entra ID OIDC 登录与 Managed Identity 免密钥设计
- 内部 ingress 与私有端点的默认安全网络拓扑

## 适用场景

- 在企业 Azure 环境中快速搭建带统一认证的 Open WebUI
- 通过 APIM 对内部 LLM 用量做限额与计量
- 参考生产级 Azure AI 网关架构（hub-spoke 网络、私有端点）

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Deploy Open WebUI on Azure Container Apps with Entra ID authentication, Azure API Management (AI API Gateway), Micro
> L15: ✅ **API Management with AI in Azure** with token tracking, limits, usage metrics, custom analytics, Entra OAuth pol

## 星数曲线

```mermaid
xychart-beta
    title "riosengineer/open-webui-on-azure 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-30 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c15e421d5877` · [字段定义](../../DATASET.md)*
