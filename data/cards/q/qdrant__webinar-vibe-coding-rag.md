# qdrant/webinar-vibe-coding-rag

⭐ 19 · JavaScript · 推送 2026-08-08 · [GitHub](https://github.com/qdrant/webinar-vibe-coding-rag) · 组织维护

**webinar 演示项目：YouTube 视频转录的 RAG 站内搜索应用**

Qdrant 网络研讨会（Letting LLMs Write RAG Applications）的配套实践仓库，目标是配合 AI 编码工具现场构建一个 YouTube 视频站内搜索应用：后端提取视频转录文本，按 30 秒切片（10 秒重叠），用 SentenceTransformers 生成嵌入并存入 Qdrant，用户搜索后返回可点击时间戳的片段。README 同时给出 mcp-server-qdrant 的配置方法，将 DaisyUI 组件知识库存入 Qdrant 供 Claude Code 生成前端时检索。部署于 Hugging Face Spaces（Docker SDK），Apache-2.0 许可。作者明示不保证 LLM 生成的代码开箱可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YouTube 转录按 30 秒切片、10 秒重叠建索引，结果跳转到精确时间戳
- 使用 Qdrant 向量检索与 SentenceTransformers 静态检索模型
- 配置 mcp-server-qdrant 作为 Claude Code 的代码检索知识库
- 已处理的视频复用现有嵌入，不重复计算

## 适用场景

- 在长篇教学视频中按主题搜索并跳转到对应时间点
- 跟随 webinar 学习用 AI 编码工具搭建 RAG 应用
- 演示 MCP server 与 Qdrant 知识库在 vibe coding 中的用法

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L24: Retrieval Augmented Generation (RAG) is perfect for this task. By indexing a video's transcript, we provide an inte
> L44:  - When a query is submitted, backend returns the most relevant video segments

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/webinar-vibe-coding-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0e8b3e6374bd` · [字段定义](../../DATASET.md)*
