# henrietteharmse/uml2semantics

⭐ 20 · Scala · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/henrietteharmse/uml2semantics) · 个人维护

**将 UML 类图转换为 OWL 2 本体的 Java 命令行工具**

读取 TSV 文件或 UML 工具导出的 XMI 文件中的类图信息（类、属性、关联、泛化集），生成 OWL 2 本体（RDF 文件），供后续对本体进行推理以发现不一致或非预期结果。面向从事概念建模与知识图谱工作的开发者与数据建模人员。支持 TSV 与 XMI 混合输入并用 overrides 选项控制优先级、可用 CURIE 覆盖将类与属性映射到已有链接数据（如 schema.org）。项目自述处于非常早期阶段，目前不支持枚举（XMI 路径）等特性，需 Java 11+ 运行环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- TSV/XMI 两种输入格式，可混合并用 --overrides 控制优先级
- 通过 CURIE/TSV 覆盖将类映射到已有链接数据（如 schema.org）
- 提供 --no-global-disjointness 处理多继承场景

## 适用场景

- 把概念层的 UML 类图转成 OWL 2 本体用于逻辑一致性检查
- 将既有 UML 模型与 schema.org 等链接数据词汇对齐
- 从 Enterprise Architect 导出的 XMI 批量生成本体文件

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L1: `uml2semantics` is an application that allows you to convert a UML class diagram to an OWL 2 ontology. Translating a
> L2: class diagram to an OWL 2 ontology allows one to reason over the ontology and thereby discover possible

## 星数曲线

```mermaid
xychart-beta
    title "henrietteharmse/uml2semantics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `34f0dac041ca` · [字段定义](../../DATASET.md)*
