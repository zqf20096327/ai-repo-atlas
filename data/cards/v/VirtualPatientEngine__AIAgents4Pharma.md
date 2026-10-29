# VirtualPatientEngine/AIAgents4Pharma

⭐ 106 · Python · MIT · 推送 2026-03-30 · [GitHub](https://github.com/VirtualPatientEngine/AIAgents4Pharma) · [官网](https://virtualpatientengine.github.io/AIAgents4Pharma/) · 组织维护

**面向药物研发的生物医药 AI Agent 工具包（5 个对话 Agent）**

Team VPE 维护的开源工具包，提供多个面向生物医药研究的对话式 Agent：Talk2BioModels 与系统生物学数学模型交互、Talk2KnowledgeGraphs 探索生物知识图谱（内置 PrimeKG 子集）、Talk2Scholars 检索并管理文献（支持 Zotero）、Talk2Cells 查询测序数据、Talk2AIAgents4Pharma 聚合调用前述 Agent。基于 LangChain/LangGraph 与 Streamlit 构建，通过 OpenAI 与 NVIDIA API 访问 LLM，T2S 与 T2KG 需部署 Milvus 向量库。提供 Docker 镜像、pip/uv 安装与源码运行三种途径，多数 Agent 处于 v1 开发中状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5 个生物医药对话 Agent：模型、知识图谱、文献、测序数据、聚合入口
- Talk2KnowledgeGraphs 内置 PrimeKG 知识图谱子集，开箱可交互
- Talk2Scholars 支持文献下载、查询与写入 Zotero 引文管理器
- Docker Hub 提供全部 Agent 镜像，支持可选 LangSmith 追踪

## 适用场景

- 用自然语言查询系统生物学数学模型
- 探索生物医学知识图谱并发现数据关联
- 检索、下载相关文献并归档到 Zotero

## 场景标签

`科研工具` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L24: Welcome to **AIAgents4Pharma** – an open-source project by Team VPE that brings together AI-driven tools to help re
> L28: - **Talk2BioModels** _(v1 released; v2 in progress)_: Engage directly with mathematical models in systems biology.

## 星数曲线

```mermaid
xychart-beta
    title "VirtualPatientEngine/AIAgents4Pharma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-29 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `662613eb173f` · [字段定义](../../DATASET.md)*
