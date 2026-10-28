# StreamIntelligenceLab/Kolibrie

⭐ 62 · Rust · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/StreamIntelligenceLab/Kolibrie) · [官网](https://streamintelligencelab.github.io/Kolibrie-website/) · 组织维护

**Rust 实现的 SPARQL/RDF 数据库与流推理引擎，供知识图谱应用**

由 KU Leuven Stream Intelligence Lab 开发的 Rust 库：提供 RDF 数据的解析（RDF/XML、Turtle、N3、N-Triples）、存储与 SPARQL 查询执行，支持命名图、UNION、六种 Update 形式、聚合与嵌套查询，并集成基于 Volcano 模型的代价优化器、Rayon 并行与 SIMD 加速。含 Datalog 风格 Reasoner（前向/后向链推理）、时间戳三元组的滑动窗口流处理，以及通过 PyO3 与 Python ML 框架的集成。面向需要语义数据处理的研究与开发者，以 Rust 库形式使用，另带 HTTP WebUI 与 Docker 部署。SPARQL 1.1 Update 的 WITH/USING/LOAD 等形式不在本版本支持范围。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SPARQL 查询与六种 Update 形式，含命名图/UNION/聚合/嵌套查询
- Volcano 代价优化器 + Rayon 并行 + SIMD 加速
- Reasoner 支持 ABox/TBox 与前向链、后向链规则推理
- 时间戳三元组滑动窗口流处理与 PyO3 Python ML 集成

## 适用场景

- 构建并查询大规模 RDF 知识图谱，执行 SPARQL 语义查询
- 对连续数据流做带滑动窗口的时序三元组分析
- 在规则推理基础上做符号-数据融合（神经符号）流推理研究
- 通过 WebUI 或 Docker 部署语义数据服务

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L17: **Kolibrie** is developed within the Stream Intelligence Lab at KU Leuven, under the supervision of Prof. Pieter Bo
> L30: - **Machine Learning Integration**: Seamlessly integrates with Python ML frameworks through PyO3 bindings.
> L396: The **Reasoner** component allows you to build and manage semantic networks with instance-level (ABox) information

## 星数曲线

```mermaid
xychart-beta
    title "StreamIntelligenceLab/Kolibrie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-28 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `804370aa74f1` · [字段定义](../../DATASET.md)*
