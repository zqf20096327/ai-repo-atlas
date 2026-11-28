# langchain-ai/langchain-azure-js

⭐ 10 · JavaScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/langchain-ai/langchain-azure-js) · 组织维护

**为 LangChain.js 提供微软 Azure AI 服务集成的仓库**

该仓库为 LangChain.js 与 LangGraph.js 提供 Azure AI 服务的集成包。README 明确声明项目处于早期开发阶段，当前 langchain-azure-ai 包仅包含集成脚手架，尚不提供可用于生产的 Azure 集成，公开 API 在首个发布前可能变更。集成遵循 LangChain.js 回调、流式、工具调用等契约，支持 API-key 与 Microsoft Entra ID 认证。面向使用 pnpm 工作区的开发者，要求 Node.js 18+，通过 pnpm 安装、构建并运行 lint/test 检查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 LangChain.js 兼容的 Azure AI 服务集成包 langchain-azure-ai
- 遵循 LangChain.js 回调、流式、工具调用、序列化、追踪契约
- 支持 API-key 与 Microsoft Entra ID 两种认证方式
- 使用官方 Azure SDK 客户端

## 适用场景

- 在 LangChain.js 应用中接入微软 Azure AI 服务
- 在 LangGraph.js 编排中使用 Azure 模型组件
- 参与 Azure 集成包的早期开发与贡献

## 场景标签

 · 领域:LLM 基础设施/模型接入

## 证据(README 行号)

> L6: Azure AI integrations for LangChain.js and LangGraph.js.
> L9: > This repository is in an early development stage. The current `langchain-azure-ai` package contains integration sc
> L13: This repository provides LangChain-compatible integrations for Microsoft Azure AI services. Integrations should com

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langchain-azure-js 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `9901627765f5` · [字段定义](../../DATASET.md)*
