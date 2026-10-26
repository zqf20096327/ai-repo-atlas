# The-OpenROAD-Project/ORAssistant

⭐ 48 · Python · GPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/The-OpenROAD-Project/ORAssistant) · 组织维护

**面向 OpenROAD 用户的 RAG 文档问答聊天助手**

OpenROAD 项目官方的聊天助手：对 OpenROAD、OpenROAD-flow-scripts、OpenSTA、Yosys、Klayout 文档做分块与嵌入（FAISS），通过 langgraph 路由 LLM 调用将查询分发到 7 类检索器工具，混合检索后经交叉编码器重排生成回答，用于安装排障与文档查询。架构分后端、Streamlit 前端与人工评测三组件，可 Docker 部署或本地运行（uv 依赖管理），支持 HF/Google GenAI/VertexAI 三种嵌入来源，对话数据用 PostgreSQL 持久化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档分块嵌入 FAISS，混合检索＋交叉编码器重排
- langgraph 路由至 7 类检索器工具，LLM tool-calling 调用
- 后端/前端/评测三组件可分机部署
- 提供 Docker 部署与 uv 本地安装两条路径

## 适用场景

- 查询 OpenROAD/ORFS 工具用法与安装排障
- 汇总 OpenROAD 文档与在线资源给出答案
- RAG 系统的人工评测研究

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L9: The OpenROAD chat assistant aims to provide easy and quick access to information regarding tools, responses to quest
> L173: OpenROAD documentation, OpenROAD-flow-scripts documentation, manpages and OpenSTA documentation is chunked and emb
> L196: The `langgraph` framework has been used to make effective use of the multiple retriever tools. Upon receiving a qu

## 星数曲线

```mermaid
xychart-beta
    title "The-OpenROAD-Project/ORAssistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `36e9c956d359` · [字段定义](../../DATASET.md)*
