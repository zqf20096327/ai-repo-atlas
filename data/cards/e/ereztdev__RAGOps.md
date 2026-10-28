# ereztdev/RAGOps

⭐ 24 · Python · NOASSERTION · 推送 2026-03-10 · [GitHub](https://github.com/ereztdev/RAGOps) · 个人维护

**面向航空地面设备维护的本地 RAG 排障问答系统**

针对航空地面支持设备（GSE）维护团队的检索增强生成管线：解析 OEM 维护手册 PDF（Docling 结构感知或 pypdf 兜底），本地建立版本化索引，通过 BGE 语义检索加 BM25 关键词经 RRF 融合回答排障问题，回答附页码与来源引用；文档不支持时显式拒答。全流程本地部署（Ollama 运行 Llama 3.1、本地 BGE 嵌入），无云 API。限制：需 NVIDIA GPU，基准测试 80%（12/15）仍在迭代中。提供 Docker Compose 与 CLI 两种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- BGE+BM25 混合检索与 RRF 融合，无近似最近邻与随机检索层
- 文档不支持时显式拒答，回答附 chunk 引用与页码溯源
- 全本地运行：Llama 3.1 via Ollama、本地 BGE 嵌入、无出站网络需求
- 索引需通过检索评估（空检索/置信度/命中数检查）后方可激活，索引版本不可变

## 适用场景

- 机坪技师快速从上百页 OEM 手册中查到排障步骤与规格值
- 受监管运营方（政府/军事）在不出网环境下搭建私有文档问答
- 机队内部文档（改线图、维护计划、事件报告）的带引用问答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L7: RAGOps is a Retrieval Augmented Generation pipeline built for GSE maintenance teams. It ingests OEM technical manual
> L9: No cloud dependency. No API keys. No data leaves your infrastructure.
> L41: RAGOps converts OEM maintenance manuals into a private troubleshooting system.

## 星数曲线

```mermaid
xychart-beta
    title "ereztdev/RAGOps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `cea839b48629` · [字段定义](../../DATASET.md)*
