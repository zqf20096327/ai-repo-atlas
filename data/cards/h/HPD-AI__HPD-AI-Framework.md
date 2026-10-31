# HPD-AI/HPD-AI-Framework

⭐ 14 · C# · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/HPD-AI/HPD-AI-Framework) · 组织维护

**面向 .NET 的生产级 AI 应用构建框架族（agent/RAG/工作流等 12 个包）**

一组 C#/.NET 框架包，覆盖 AI 应用构建所需的多类基础设施：HPD-Agent 用于构建可调用模型、工具、子代理与流式事件的 agent；HPD-RAG 提供可替换组件的检索系统；HPD-Graph 运行带检查点/恢复的类型化工作流图；另有 ML 管道、实时媒体、沙箱运行时、应用数据、API 网关、认证、账本与终端 UI 等包。面向 .NET 开发者，各包文档与产品层在独立仓库。多个包标注 Coming Soon，整体 pre-1.0，API 契约可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- HPD-Agent：模型对话、工具调用、子代理委派、流式事件与会话管理
- HPD-RAG：摄取/存储/搜索/重排/评估各环节可独立替换或移除
- HPD-Graph：类型化工作流图，支持并行层、检查点恢复与人工等待
- 覆盖沙箱执行环境、认证、API 网关、双录账本等周边能力

## 适用场景

- 用 .NET 构建可调工具和子代理的生产级 AI agent
- 搭建组件可替换的 RAG 检索系统
- 运行带检查点/恢复的有状态工作流图

## 场景标签

`RAG` `工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A set of C# (.NET) frameworks for building production AI applications, autonomous agents, sandboxed compute environm
> L11: Use HPD-Agent to build production agents that can talk to models, call tools, stream events, manage sessions, hand 
> L17: Use HPD-RAG to build retrieval systems where ingestion, storage, search, reranking, formatting, and evaluation can 

## 星数曲线

```mermaid
xychart-beta
    title "HPD-AI/HPD-AI-Framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d2a2548de45e` · [字段定义](../../DATASET.md)*
