# Azure-Samples/Cosmic-Food-RAG-app

⭐ 67 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Azure-Samples/Cosmic-Food-RAG-app) · [官网](https://techcommunity.microsoft.com/blog/educatordeveloperblog/build-ai-rag-apps-with-langchain-azure-documentdb-and-microsoft-foundry-step-by-/4513775?wt.mc_id=studentamb_71460) · 组织维护

**Azure OpenAI + DocumentDB 的餐饮点餐 RAG 演示应用**

微软 Azure Samples 出品的演示应用：用户以对话方式请求定制餐食（如“高蛋白菜品”），系统基于 Azure DocumentDB（MongoDB 兼容）中的菜品数据做向量检索推荐，用户可进一步定制并发送订单与配送信息，用户偏好存储于 DocumentDB 供后续订单记忆。检索链路由 LangChain 构建，面向 ISV 展示可迁移的方案架构。支持 GitHub Codespaces、本地 uv/npm 构建与 azd 一键部署到 Azure App Service，需自备 Azure OpenAI 与 DocumentDB 资源。

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

- 对话式菜品推荐，基于 DocumentDB 向量检索
- 用户偏好持久化，支持后续订单记忆
- 提供 azd 一键部署到 Azure App Service 与本地开发流程
- 通过 Jupyter notebook 生成 .env 并完成数据加载

## 适用场景

- 参考 Azure 上的 RAG 推荐应用参考架构并快速部署
- 餐饮点餐场景的原型验证与定制演示
- ISV 基于该方案适配其他餐饮连锁系统

## 场景标签

`RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L2: description: A Demo application for a streamlined ordering system tailored for various food categories. It allows us
> L20:  A Demo application for a streamlined ordering system tailored for various food categories. It allows users to requ

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/Cosmic-Food-RAG-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-31 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a3c59297beb5` · [字段定义](../../DATASET.md)*
