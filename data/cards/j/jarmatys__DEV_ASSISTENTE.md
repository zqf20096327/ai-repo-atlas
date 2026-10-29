# jarmatys/DEV_ASSISTENTE

⭐ 45 · C# · MIT · 推送 2025-11-19 · [GitHub](https://github.com/jarmatys/DEV_ASSISTENTE) · [官网](https://assistente.dev) · 个人维护

**开发者个人知识库助手：存储笔记/代码片段并生成回答**

面向开发者的个人记忆库应用：加载并解析 *.md 笔记（知识库）与 *.cs 文件（代码库），使用 OpenAI embedding 生成向量并存入 Qdrant，基于知识库与代码库生成 prompt，通过 OpenAI API 生成回答或代码。技术栈为 C#/.NET，含 Blazor UI、内部 API 与 Worker，使用 PostgreSQL、RabbitMQ、SignalR 实现异步回答生成，并集成 Seq/Jaeger 可观测性组件。通过 Docker 与 PowerShell 脚本部署，需配置 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载解析 *.md 知识库与 *.cs 代码库
- OpenAI embedding + Qdrant 向量存储
- RabbitMQ + SignalR 异步生成回答或代码
- Blazor UI + Docker Compose 一键部署环境

## 适用场景

- 集中管理散落各处的开发笔记、书签与代码片段
- 基于自己的笔记与代码库提问并获取回答或代码
- 团队或个人搭建自托管的开发知识问答环境

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L42: - ✅ Generating prompt based on the 'knowledge base' & 'code base'
> L45: - ✅ Integration with the OpenAI API

## 星数曲线

```mermaid
xychart-beta
    title "jarmatys/DEV_ASSISTENTE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `55dc1c1cfba2` · [字段定义](../../DATASET.md)*
