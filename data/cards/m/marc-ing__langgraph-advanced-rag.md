# marc-ing/langgraph-advanced-rag

⭐ 18 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/marc-ing/langgraph-advanced-rag) · 个人维护 · 中文 README

**面向终端用户的 HR 政策问答 RAG 应用，含范围拒答**

由 Notebook 教学案例整理的 HR 员工手册问答系统：上传 Markdown 手册，按 H1/H2 切分后经 OpenAI 兼容接口生成向量并存入本地 FAISS；用 LangGraph StateGraph 编排提取、LLM 范围分类、Top-3 检索、Prompt 组装、生成与拒答节点，条件边区分 HR/非 HR 分支，支持 50 条历史多轮追问并返回节点轨迹。提供 FastAPI REST API、Swagger、响应式 Web UI 与不调真实 API 的自动化测试。限制：仅处理 Markdown，无混合检索、Reranker 与查询改写，需一个同时兼容 Embedding 与 Chat Completions 的服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph StateGraph 条件路由：HR 分支检索生成、非 HR 分支拒答
- FAISS 本地持久化索引，临时目录构建后原子替换
- 前端可配置 API Key/Base URL/双模型，Key 不落盘
- 返回引用文件、章节标题与逐节点执行轨迹

## 适用场景

- 上传员工手册搭建 HR 政策问答
- 观察并讲解 LangGraph 状态图与条件边的执行路径
- 学习 RAG 流程的工程化实现（FastAPI 后端 + Web UI + 测试）

## 场景标签

`文档问答` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L9: 一个使用 **LangGraph 状态图、FAISS 和条件边**实现的智能 HR 政策问答项目。应用把 HR RAG 流程拆成提取问题、范围分类、文档检索、Prompt 组装、答案生成和拒答节点，让状态变化、执行顺序与分支路径都可
> L29: > 由 LangGraph 编排、带分类护栏和条件路由的向量 RAG 工作流。
> L110: |`answer_generate`|调用 LLM 生成受上下文约束的回答|`answer`|

## 星数曲线

```mermaid
xychart-beta
    title "marc-ing/langgraph-advanced-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `2405d0894090` · [字段定义](../../DATASET.md)*
