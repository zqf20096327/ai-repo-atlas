# lianyinging/flowgame

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/lianyinging/flowgame) · [官网](http://flowgame.mgdeep.com) · 个人维护 · 中文 README

**面向业务自定义的 AI 工作流编排框架，Vue 3 一行接入**

在 Tinyflow 画布引擎之上扩展的 AI 工作流编辑框架：前端通过 @flowgame/vue 的 FlowEditor 嵌入任意 Vue 3 项目，@flowgame/core 注册 Start API、模型调用（LLM API）、知识库检索+（Qdrant RAG）、网页搜索/抓取、图像生成、记忆读写、HTML 模板等自定义节点；流程试运行、Redis 持久化、向量检索由独立 Python 后端（FastAPI + Redis + Qdrant）执行，前后端分离。支持 npm 接入、Monorepo 本地开发与 Docker 一键部署（前端+API+Redis+Qdrant）。未启动后端时画布可编辑但接口功能不可用。

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

- 基于 Tinyflow 画布扩展自定义 AI 节点（模型调用/知识库检索/网页搜索抓取/记忆读写/图像生成）
- FlowEditor 一行接入 Vue 3 项目，内置流程列表/知识库/AgentTeam/会话机器人
- FastAPI + Redis + Qdrant 独立后端驱动真实执行与数据持久化
- Docker 一键部署完整环境（前端 + API + Redis + Qdrant）

## 适用场景

- 在 Vue 3 项目中嵌入可视化的 AI 工作流编辑器
- 业务侧自定义包含 LLM 调用与 RAG 检索的工作流并以 API 对外暴露
- 搭建带知识库向量检索与会话机器人的对话/图生图应用

## 场景标签

`工作流自动化` `RAG` · 领域:效率与自动化

## 证据(README 行号)

> L15: - **FlowGame** 在 Tinyflow 画布引擎之上，面向 **AI 工作流** 做了深度扩展：保留 Tinyflow 的拖拽编排体验，并**新增一批自定义节点**，同时配套 **Python 后端** 完成真实执行与
> L26: |**模型调用（LLM API）**|配置 API Key、接口地址与模型名，调用大模型|
> L38: - **Python 后端驱动执行**：flowgame_python 负责解析工作流、调用 LLM/HTTP/网页搜索与抓取、读写 Redis 与 Qdrant，支持同步与流式试运行。

## 星数曲线

```mermaid
xychart-beta
    title "lianyinging/flowgame 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `64280d050def` · [字段定义](../../DATASET.md)*
