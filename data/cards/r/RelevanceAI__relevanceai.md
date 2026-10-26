# RelevanceAI/relevanceai

⭐ 285 · Python · Apache-2.0 · 推送 2026-01-15 · [GitHub](https://github.com/RelevanceAI/relevanceai) · [官网](https://sdk.relevanceai.com) · 组织维护

**Relevance AI 平台的 Python SDK，用于构建与管理 AI agent**

Relevance AI 官方 Python SDK：通过客户端接入 Relevance AI 平台（需注册账号与 secret key），支持列出、检索并调用 AI agent 与 tool，管理 knowledge sets 数据的存取，以及任务元数据查询与删除。安装方式为 pip install relevanceai，凭据可经环境变量（RAI_API_KEY/RAI_REGION/RAI_PROJECT）或直接传参配置。本体是平台客户端 SDK，模型与 agent 运行于 Relevance AI 云端。

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

- 列出/检索/调用项目中的 AI agent 与 tool
- knowledge sets 的列出与数据检索
- 任务元数据查询与已完成任务删除
- 凭据支持环境变量（python-dotenv）或直接传参两种方式

## 适用场景

- 在 Python 代码中调用我在 Relevance AI 平台创建的 agent
- 查询和管理项目里的 tool 与 knowledge set
- 跟踪和清理平台任务

## 场景标签

 · 领域:AI agent 平台/SDK

## 证据(README 行号)

> L15: # Relevance AI SDK
> L17: Welcome to the Relevance AI SDK! This guide will help you set up and start using the SDK to interact with your AI a

## 星数曲线

```mermaid
xychart-beta
    title "RelevanceAI/relevanceai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 283 --> 286
    line [284, 285, 285]
```

2026-10-18 284 → 2026-10-26 285（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `65c27a904984` · [字段定义](../../DATASET.md)*
