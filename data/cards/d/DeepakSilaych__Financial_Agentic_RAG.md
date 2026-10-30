# DeepakSilaych/Financial_Agentic_RAG

⭐ 16 · Python · 推送 2026-07-26 · [GitHub](https://github.com/DeepakSilaych/Financial_Agentic_RAG) · [官网](https://finsight.deepaksilaych.me) · 组织维护

**面向 10-K 财报的 Agentic RAG 金融文档问答平台**

端到端的 agentic RAG 系统，针对 10-K 年报等长篇金融 PDF 提供读取、检索与问答：结合向量检索、元数据过滤与相关性评分，agentic 层负责问题分解、逐子查询检索、答案生成与幻觉评估，并可拉取网页证据。仓库含 FastAPI 后端与 Vite+React 前端，支持两种模式：demo 模式无需 API key（AI 端点返回固定提示，其余功能可用）；full 模式接入外部 LLM 与 embedding 提供商运行 LangGraph 完整流水线。曾获 Inter IIT Tech Meet 13.0 第一名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 问题分解→子查询检索→相关性评分→生成→幻觉评估的 LangGraph agentic 流水线
- demo 模式无 API key 可运行，产品功能（spaces/上传/聊天 UI/websocket）保持可用
- FastAPI 后端 + Vite+React 前端的完整应用形态
- 支持按公司、财年等元数据约束的检索

## 适用场景

- 我对 10-K 年报等金融 PDF 做有出处的问答与检索
- 我需要一套可本地部署演示的金融文档智能平台
- 我想实验不同的 RAG 编排策略与答案评估标准

## 场景标签

`文档问答` `RAG` `金融量化` · 领域:知识与检索

## 证据(README 行号)

> L11: FinSight is an end-to-end, agentic Retrieval-Augmented Generation (RAG) system designed specifically for financial 
> L13: This repo is intentionally organized to support two operating modes. In “full mode,” the LangGraph pipeline runs wi
> L85: The research pipeline is built around LangGraph workflows that combine retrieval, reasoning, grading, and safety ch

## 星数曲线

```mermaid
xychart-beta
    title "DeepakSilaych/Financial_Agentic_RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `95ef230be3fa` · [字段定义](../../DATASET.md)*
