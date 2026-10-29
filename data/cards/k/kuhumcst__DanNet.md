# kuhumcst/DanNet

⭐ 29 · Clojure · MIT · 推送 2026-10-28 · [GitHub](https://github.com/kuhumcst/DanNet) · [官网](https://wordnet.dk) · 组织维护

**丹麦语 WordNet 词汇语义网络数据集与 RDF 知识图谱应用**

DanNet 是丹麦语的 WordNet，以 RDF 为原生表示，涵盖数据库层、应用层与序列化格式。数据可通过 wordnet.dk 浏览、从 releases 页面下载，或经 SPARQL（Apache Jena 后端）查询。提供 RDF(Turtle)、CSV(CSVW)、WN-LMF、DMLex 多种导出格式及 COR/DDS 等伴生数据集。系统由 Clojure/ClojureScript 编写，部署为 Docker Compose 三服务（Web 应用、Python MCP server、Caddy 反代），可经 MCP（https://wordnet.dk/mcp）接入 Claude 等 AI 工具查询语义关系。自建运行需 Java 与 Clojure CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式数据集：RDF/CSV(CSVW)/WN-LMF/DMLex
- 基于 Ontolex-lemon 与 GWA 标准的可 SPARQL 查询知识图谱
- 提供 MCP server URL（https://wordnet.dk/mcp）供 Claude 等 LLM 工具接入
- OWL/RDFS 推理生成隐含三元组，SHACL 验证数据质量

## 适用场景

- 语言学研究或 NLP 应用中获取丹麦语词汇语义资源
- 通过 Claude 等 AI 工具直接查询丹麦语语义关系
- 将 RDF 数据装入 Jena 等图数据库做 SPARQL 查询
- 用 Python wn 库加载 WN-LMF 格式进行词网分析

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L3: DanNet is a WordNet for the Danish language. DanNet uses RDF as its native representation at both the database level
> L86: DanNet can be connected to AI tools like Claude via MCP (Model Context Protocol).

## 星数曲线

```mermaid
xychart-beta
    title "kuhumcst/DanNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4214d3358cc3` · [字段定义](../../DATASET.md)*
