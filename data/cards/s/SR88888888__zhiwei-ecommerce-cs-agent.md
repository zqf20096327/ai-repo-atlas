# SR88888888/zhiwei-ecommerce-cs-agent

⭐ 18 · Python · MIT · 推送 2026-08-08 · [GitHub](https://github.com/SR88888888/zhiwei-ecommerce-cs-agent) · 个人维护 · 中文 README

**电商客服 Agent 系统：意图分流+工具调用+RAG 处理订单物流售后咨询**

面向电商客服高频咨询场景的 Agent 系统，采用 FastAPI 后端与 React 前端。通过规则优先、LLM（DeepSeek-V4-Flash）兜底的意图识别与槽位填充分流请求：订单/物流/售后走 Function Calling 受控工具调用，知识类问题走 RAG（pgvector 向量检索+BM25+RRF 融合+BGE-Reranker 精排）。支持 PDF 手册经 MinerU 解析入库、三层会话记忆、敏感字段脱敏与 100 条自动化评测。Docker Compose 启动 PostgreSQL，前后端分别以 uvicorn 和 npm 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 意图分流+Function Calling 工具调用处理订单/物流/售后
- 父子块 RAG：MinerU 解析+pgvector 向量检索+BM25+RRF+BGE 精排
- 三层会话记忆与业务槽位持久化，重启后可恢复多轮任务
- 内置 100 条自动化评测，前端看板展示指标与逐条记录

## 适用场景

- 电商客服自动处理订单物流查询与售后收集
- 基于产品手册的商品知识问答
- 对客服 Agent 做自动化评测与结果审计

## 场景标签

`聊天机器人` `RAG` `模型评测` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: 面向电商客服高频咨询、订单物流和售后处理场景，搭建 Agent 智能客服系统。系统通过意图分流、受控 ReAct、Function Calling 和 RAG 知识库检索，完成订单物流查询、售后信息收集、商品手册问答和自动化评测，解
> L36:     R -->|订单或物流| T[Function Calling 工具调用]
> L79: 5. 将高相关上下文交给 LLM，生成自然语言回答。

## 星数曲线

```mermaid
xychart-beta
    title "SR88888888/zhiwei-ecommerce-cs-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `94fd7795c965` · [字段定义](../../DATASET.md)*
