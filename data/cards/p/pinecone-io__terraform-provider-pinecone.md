# pinecone-io/terraform-provider-pinecone

⭐ 32 · Go · MPL-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/pinecone-io/terraform-provider-pinecone) · 组织维护

**Pinecone 官方 Terraform Provider：以 IaC 管理向量库资源**

Pinecone 官方维护的 Terraform Provider 插件，用 Go 编写，允许通过 Terraform 声明式管理 Pinecone 的索引、集合、项目、API Key、服务账户、用户、邀请与角色绑定。支持两种认证方式：常规操作（索引/集合）使用 API Key，管理操作（API Key/项目管理）需 Client ID 与 Secret。索引支持 schema 风格（文档索引、集成嵌入、向量索引）与旧版 spec 风格，后者计划弃用；另支持 Serverless/BYOC 部署、读写容量配置与索引导入。需 Terraform >= v1.4.6、Go >= 1.26 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 管理索引、集合、项目、API Key、用户与角色绑定等 Pinecone 资源
- schema 与 spec 两种索引描述风格，含集成嵌入（Pinecone 托管模型）与全文检索字段
- 支持 Serverless 与 BYOC（自带云）部署及可配置读写容量
- API Key 角色体系（Project/ControlPlane/DataPlane 的 Editor/Viewer）

## 适用场景

- 用 Terraform 声明式创建和管理 Pinecone 向量/文档索引
- 为不同环境自动化创建与授权 Pinecone API Key
- 将已有 Pinecone 索引导入 Terraform 统一管理
- 通过 CMEK、Pod 上限等项目配置满足合规要求

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L12: The Terraform Provider for Pinecone allows Terraform to manage Pinecone resources: indexes, collections, projects, 
> L21: - Terraform >= v1.4.6

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/terraform-provider-pinecone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d0f73b1fc446` · [字段定义](../../DATASET.md)*
