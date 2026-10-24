# genieincodebottle/rag-app-on-aws

⭐ 62 · Python · MIT · 推送 2026-09-07 · [GitHub](https://github.com/genieincodebottle/rag-app-on-aws) · [官网](https://aimlcompanion.ai/) · 个人维护

**用 Terraform 在 AWS 上一键部署全栈 RAG 文档问答应用**

提供完整 Terraform IaC 代码，在 AWS 上部署 RAG 应用后端：API Gateway、Lambda（上传/文档处理/查询/认证/建库）、S3、DynamoDB、带 pgvector 扩展的 PostgreSQL RDS 存储 embeddings。生成与嵌入使用 Google 免费层 Gemini Pro 与 Gemini Embedding 模型，认证由 AWS Cognito 与 JWT 负责，另含基于 SerpAPI 的远程 MCP 网页搜索服务和带登录/上传/查询/评估面板的 Streamlit 前端，支持 dev/staging/prod 多环境与 GitHub Actions CI/CD。面向熟悉 AWS 的开发者与学习者，实验成本估算约 $3（无免费层时，主要为 RDS 与 NAT Gateway）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Terraform 模块化部署 API Gateway、Lambda、S3、DynamoDB 与 pgvector RDS
- 集成 Gemini Pro 生成与 Gemini Embedding 嵌入（Google 免费层）
- Cognito + JWT 认证保护 /upload 与 /query 端点
- 内置 RAG 评估（faithfulness、relevancy、context precision）与远程 MCP 网页搜索

## 适用场景

- 在自有 AWS 账号上部署可登录的文档问答应用
- 学习 RAG 系统在云上的完整网络与组件拓扑
- 以多环境 IaC 方式管理 dev/staging/prod 部署

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: Terraform-based **Infrastructure as Code (IaC)** to deploy a complete AWS backend for a Retrieval-Augmented Generat
> L24: This repository contains the complete Terraform codebase for provisioning and managing the AWS infrastructure that 
> L104:  - Generates a final answer using the Gemini Pro model with the retrieved context.

## 星数曲线

```mermaid
xychart-beta
    title "genieincodebottle/rag-app-on-aws 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `da88507010c2` · [字段定义](../../DATASET.md)*
