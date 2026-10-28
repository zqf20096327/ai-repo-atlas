# liuyanqun0815/langgraph_fly_base

⭐ 43 · Python · Apache-2.0 · 推送 2026-09-20 · [GitHub](https://github.com/liuyanqun0815/langgraph_fly_base) · 个人维护 · 中文 README

**基于 LangGraph 的智能贷款销售客服工作流应用**

面向贷款销售场景的客服 Web 应用：以 LangGraph 1.x 编排问题分类、闲聊、知识库 RAG 问答与多轮信息收集（金额/期限/用途/资质 4 项），确认后进入双库并行产品推荐（推荐库 + 默认 KB，TopN 合并去重）并引导客户留资转化。向量检索采用 Milvus 稠密向量 + SPLADE 稀疏混合检索，支持 Word/PDF/Excel 上传分块与分区键过滤；会话经 SQLite Checkpoint 持久化，接口以 FastAPI + SSE 流式提供。LLM 走 DashScope OpenAI 兼容模式（qwen-plus），智谱可回退。提供 Docker Compose 一键启动与本地 Python 两种运行方式，信息收集阶段启用 Presidio 脱敏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 1.x 工作流：分类→信息收集(4项)→确认→双库并行推荐→客户转化
- Milvus 稠密向量 + SPLADE 稀疏混合检索，分区键隔离文档
- Word/PDF/Excel 上传分块入库，SSE 流式对话，SQLite Checkpoint 会话持久化
- 信息收集阶段 Presidio 脱敏；LLM 兼容通义千问（DashScope）与智谱回退

## 适用场景

- 搭建贷款产品咨询与销售的智能客服
- 上传贷款产品文档构建知识库做 RAG 问答
- 收集客户贷款需求后做个性化产品推荐与留资转化

## 场景标签

`聊天机器人` `RAG` `推荐系统` · 领域:对话与助手

## 证据(README 行号)

> L3: 基于 **LangGraph 1.x** 的智能贷款销售客服工作流：多轮对话、知识库 RAG、双库并行产品推荐、信息确认与客户转化。
> L31: 问题修复 → 问题分类 ─┬→ 闲聊经理
> L59: |`POST /api/chat/stream`|SSE 流式对话|

## 星数曲线

```mermaid
xychart-beta
    title "liuyanqun0815/langgraph_fly_base 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-28 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d45b0602fde4` · [字段定义](../../DATASET.md)*
