# john0isaac/rag-semantic-kernel-mongodb-vcore

⭐ 38 · Bicep · MIT · 推送 2026-04-28 · [GitHub](https://github.com/john0isaac/rag-semantic-kernel-mongodb-vcore) · [官网](https://techcommunity.microsoft.com/t5/educator-developer-blog/build-rag-chat-application-using-azure-openai-and-cosmos-db-for/ba-p/4055852) · 个人维护

**RAG 示例应用：Azure OpenAI + Cosmos DB MongoDB vCore 向量检索**

微软 Azure 样板工程：用 Python + Quart 构建检索增强生成聊天 Web 应用，由 Azure OpenAI 生成嵌入与聊天补全，Azure Cosmos DB for MongoDB vCore 执行向量检索，编排层使用 Semantic Kernel。提供 Jupyter notebook 入口、本地虚拟环境运行流程，以及通过 Azure Developer CLI（azd）一键配置并部署到 Azure App Service 的路径；附带数据导入脚本 add_data.py，支持自定义 JSON 数据文件与字段映射。面向需要在 Azure 上搭建 RAG 方案的开发者，依赖 Azure 账号与预先创建的 Cosmos DB 集群及模型部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Azure OpenAI 嵌入（text-embedding-ada-002）+ MongoDB vCore 向量检索
- Semantic Kernel 编排 + Quart Web 应用
- azd 一键部署到 Azure App Service（infra/bicep 配置）
- add_data.py 支持自定义 JSON 数据与 id/text/description 字段映射

## 适用场景

- 我在 Azure 上快速搭建一个可部署的 RAG 聊天应用
- 学习 Semantic Kernel 与 MongoDB vCore 向量检索的集成方式
- 通过 azd 模板把 RAG 应用部署到自己的 Azure 订阅

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L19: A Python sample for implementing retrieval augmented generation using Azure Open AI to generate embeddings, Azure C
> L2: description: A Python sample for implementing retrieval augmented generation using Azure Open AI to generate embeddi

## 星数曲线

```mermaid
xychart-beta
    title "john0isaac/rag-semantic-kernel-mongodb-vcore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fbb7e550c0d8` · [字段定义](../../DATASET.md)*
