# Anton2025-11-06/DRAGON-AI

⭐ 212 · Vue · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/Anton2025-11-06/DRAGON-AI) · 个人维护 · 中文 README

**给企业用的可私有部署多租户 AI 中台**

面向需要自托管 AI 能力的企业团队，把模型网关、知识库 RAG、知识图谱、工作流编排、ReAct 智能体沙箱与 RBAC 权限体系整合进同一工作区。后端为 Python/FastAPI 微服务（六服务 + 四条 arq 流水线），前端 Vue 3；依赖 MySQL、Redis、Nacos、Elasticsearch、Neo4j。README 明确标注开发进度：核心服务已可用，datasets/train/inference 等训练推理模块仅预留空包骨架，k8s 清单尚未编写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容模型网关，接入 12 类能力 × 3 家供应商（OpenAI 兼容/通义千问/智谱）
- 可视化工作流画布，21 类节点，支持人工审批、记忆与函数调用
- RAG 三类知识库：BM25 + dense kNN 混合检索、Neo4j 图谱增强、RAGAS 评测
- AgentScope ReAct 智能体配每用户持久化云沙箱与产物在线预览

## 适用场景

- 企业内部搭建私有化的多模型接入与对话平台
- 构建带审批流的可视化 AI 工作流
- 自托管企业知识库问答与图谱检索
- 给智能体配独立沙箱执行任务并交付产物

## 场景标签

`模型网关` `工作流自动化` `RAG` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L1: # 🐉 DRAGON-AI — 可私有部署的多租户 AI 中台
> L3: > 把 **模型网关、知识库 RAG、知识图谱、工作流编排、深度探索智能体（Harness）与企业级 RBAC** 收进同一个工作区，数据、模型与权限都由你自己掌握。
> L16: |模型网关与模型广场|统一接入、分发、治理多供应商模型|OpenAI 兼容入口、12 类能力 × 3 供应商、申请审批、API Key|

## 星数曲线

```mermaid
xychart-beta
    title "Anton2025-11-06/DRAGON-AI 星数(近 3 点)"
    x-axis ["2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 208 --> 213
    line [209, 212, 212]
```

2026-11-21 209 → 2026-11-23 212（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `4bc843970aad` · [字段定义](../../DATASET.md)*
