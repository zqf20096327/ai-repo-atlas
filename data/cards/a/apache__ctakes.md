# apache/ctakes

⭐ 139 · Java · Apache-2.0 · 推送 2026-08-12 · [GitHub](https://github.com/apache/ctakes) · [官网](https://ctakes.apache.org) · 组织维护

**面向临床文本的 NLP 平台：从病历文本抽取医学知识与实体**

Apache cTAKES 是用自然语言处理技术从临床文本中抽取知识的模块化平台，结合规则与机器学习方法，可识别症状、操作、诊断、药物、解剖结构等概念及其属性和标准编码，支持将时间事件置于患者时间线。组件在生物医学与通用领域金标数据上训练，支持 HL7/CDA/FHIR/SNOMED-CT/RxNORM 等多种数据标准。运行需 Java 17（6.0+）或 Java 8/11（5.x），命名实体识别默认词典需 UMLS 许可证；提供预编译发行包与 Maven 源码构建两种途径，另有 Python 3 的 PBJ 桥。给医学机构研究人员、NLP/ML 开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从临床文本抽取症状、诊断、药物等概念及标准编码
- 时间事件识别并置于患者时间线
- 支持 HL7/CDA/FHIR/SNOMED-CT/RxNORM 等数据标准
- 提供预编译安装包与 Maven 源码构建两种方式

## 适用场景

- 从放射报告、临床笔记、出院小结中抽取医学实体与编码
- 构建患者时间线以分析临床事件
- 处理健康相关叙述文本（如社交媒体健康内容）

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: The Apache™ clinical Text Analysis and Knowledge Extraction System (cTAKES™) focuses on extracting knowledge
> L8: cTAKES is engineered in a modular fashion and employs leading-edge rule-based and machine learning methods.

## 星数曲线

```mermaid
xychart-beta
    title "apache/ctakes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-22 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d52e9ea9d43a` · [字段定义](../../DATASET.md)*
