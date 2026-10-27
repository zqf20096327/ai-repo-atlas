# pinecone-io/contextual-webinar-rag

⭐ 23 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/pinecone-io/contextual-webinar-rag) · 组织维护

**基于 Claude/Pinecone/AWS 的网络研讨会视频 RAG 问答应用**

Pinecone 官方的 Contextual Video RAG 示例实现：将用户放入 data/videos 的 .mp4 视频经预处理、Claude 上下文增强嵌入后 upsert 到 Pinecone，再通过 Streamlit 本地 Web 应用进行问答。提供 Makefile 驱动的完整流水线（建环境、装依赖、预处理、enrich、upsert、setup 一键执行），另有 Sagemaker Notebook 分支。运行需自备 AWS Bedrock（含 Claude）访问权限与 Pinecone API Key，并先完成 AWS 认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude contextual embedding 步骤生成上下文化向量后写入 Pinecone
- Makefile 驱动的八步流水线，make setup 可一键完成全部数据处理
- Streamlit 本地 Web 应用交互问答，另有 Sagemaker Notebook 分支

## 适用场景

- 对 YouTube 视频、Zoom 研讨会、会议录像建 RAG 问答机器人
- 学习 contextual retrieval 在视频数据上的实现方式

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L4: Ever wanted to ask questions over your video data, such as Youtube, Zoom webinars, recorded meetings, etc? This appl
> L15: You'll also need access to AWS Bedrock, Pinecone (via an API Key), and Claude specifically via Bedrock.

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/contextual-webinar-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b69125eeff76` · [字段定义](../../DATASET.md)*
