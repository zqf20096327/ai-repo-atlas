# eclipse-inception/inception

⭐ 733 · Java · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/eclipse-inception/inception) · [官网](https://eclipse-inception.github.io) · 组织维护

**面向标注者的多层文本语义标注平台，带知识库与机器建议**

INCEpTION 是一个多层文本语义标注平台：支持在自定义本体上标注实体、关系、共指、句法、框架等层级，可加载 RDF/OWL/OBO/SKOS/Turtle 或查询远程 SPARQL 端点，内置 Wikidata、SNOMED CT、Gene Ontology 等知识库配置。推荐器随标注过程训练，主动学习挑选模型最不确定的用例询问标注者，未接受的建议不落库。支持多人标注一致性度量与金标准整理，提供 REST API 与外部推荐器接口，可导入纯文本/PDF/HTML/TEI，导出 UIMA CAS XMI/JSON 或 CoNLL-U。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 推荐器随标注过程训练，主动学习选择不确定用例
- 支持 RDF/OWL/OBO/SKOS/Turtle 本体与远程 SPARQL 查询
- 多层标注（实体/关系/共指/句法/框架）在浏览器内定义
- REST API、webhook 与外部推荐器接口

## 适用场景

- 按自定义本体构建标注语料库
- 多人协作标注并计算一致性、整理金标准
- 接入自有模型为标注过程提供建议

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5:  Multi-layer text annotation with knowledge-base entity linking and machine-assisted suggestions.
> L28: - **Get suggestions that improve while you work.** Recommenders train on what you have annotated so
> L89: INCEpTION is provided as open source under the Apache License v2.0.

## 星数曲线

```mermaid
xychart-beta
    title "eclipse-inception/inception 星数(近 8 点)"
    x-axis ["2026-10-30", "2026-11-01", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-16", "2026-11-20", "2026-11-22"]
    y-axis "stars" 727 --> 735
    line [728, 729, 730, 731, 732, 734, 733, 733]
```

2026-10-30 728 → 2026-11-22 733（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `54ed73a0c852` · [字段定义](../../DATASET.md)*
