# ArsMedicaTech/arsmedicatech

⭐ 22 · Python · NOASSERTION · 推送 2026-08-11 · [GitHub](https://github.com/ArsMedicaTech/arsmedicatech) · 个人维护

**面向医疗工作流的一体化临床平台（含 LLM/EMR 集成）**

Flask + React + SurrealDB 构建的临床综合平台，目标是连接医疗人员、患者与研究者。已完成图谱/键值/关系/文档/地理空间/全文等多种数据模型 schema、模块化前端仪表盘，以及 Flask、React、Nginx、OSCAR EMR、SurrealDB 的全容器化部署；LLM 层包含工具调用路由、决策树确定性逻辑、NCBI/clinicaltrials.gov 等外部 API 与基于 SurrealDB 的向量存储 RAG 设计，RAG 与微调仍在路线图未勾选状态。项目自述处于早期阶段，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SurrealDB 多模型数据库承载症状/诊断/用药临床知识图谱与 ICD 编码
- Docker 化全栈（Flask、React、Nginx、OSCAR EMR、SurrealDB）
- LLM 工具调用架构：Prompt Router、决策树确定性推理、外部医学 API
- MCP 服务器（Model Context Protocol）与 OSCAR EMR 集成

## 适用场景

- 搭建支持 OSCAR EMR 互操作的临床诊疗平台原型
- 在临床数据图谱之上试验 LLM 辅助决策与 RAG 检索
- 作为临床信息学的开发者实验与贡献项目

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: **ArsMedicaTech** is an integrated clinical platform designed to support a wide range of use cases across modern hea
> L34: |AI/ML Integration|OpenAI-compatible LLMs (planned: RAG, fine-tuning, prompt engineering)|
> L76: * [ ] Add **prompt engineering** support (e.g., Latitude.so) AMT-025.
> L77: * [ ] Implement **Retrieval-Augmented Generation (RAG)** with SurrealDB vector store AMT-024.
> L78: * [ ] Add support for **LLM fine-tuning** AMT-023.

## 星数曲线

```mermaid
xychart-beta
    title "ArsMedicaTech/arsmedicatech 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `c748b4c40846` · [字段定义](../../DATASET.md)*
