# BingoWon/apple-rag-mcp

⭐ 121 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/BingoWon/apple-rag-mcp) · [官网](https://apple-rag.com) · 组织维护 · 中文 README

**面向 AI agent 的 Apple 文档/WWDC 检索 MCP 服务**

通过 MCP 协议向 AI agent 提供 Apple 开发者文档与 WWDC 视频转录的检索服务：混合关键词与语义检索，Jev 决策模型对候选来源按查询的 API、平台与版本要求打分排序，API 失败时由备用重排序器接管。以托管服务为主（免费额度 30 次工具调用/周，Pro 付费 $1/周 5 万次/周），源码公开可自托管，但自托管需自行运维数据库、语料与模型 API 凭证。支持 Cursor 一键安装及其他 MCP 客户端手动配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 关键词+语义混合检索，Jev 相关性排序并含备用重排序器
- 覆盖 iOS/macOS/watchOS/tvOS/visionOS 文档与 WWDC26 转录
- 托管服务含嵌入与排序模型调用，源码 MIT 公开可自托管
- 免认证即可免费使用，MCP Token 提升配额

## 适用场景

- 在 Cursor/Claude Code 等 agent 中直接查询 Apple 开发者文档
- 让编程 agent 在编码时获取 WWDC 会话转录作为上下文
- 为 Apple 平台开发项目提供最新版本文档检索

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L15: Hybrid retrieval combines keyword and semantic search to find Apple sources. Jev then ranks the merged candidates f
> L30: - **Ready-to-query sources:** Official developer documentation and video transcripts, available through one connect
> L64: - **MCP Type:** `Streamable HTTP`

## 星数曲线

```mermaid
xychart-beta
    title "BingoWon/apple-rag-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 119 --> 122
    line [120, 121, 121]
```

2026-10-18 120 → 2026-10-26 121（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f1f4f551548e` · [字段定义](../../DATASET.md)*
