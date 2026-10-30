# ISON-format/isongraph

⭐ 18 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/ISON-format/isongraph) · [官网](https://graph.ison.dev) · 组织维护

**面向 LLM 上下文的多语言属性图库：省 token 的图序列化**

提供 Python/TypeScript/Rust/C++/C# 多语言实现的属性图库，核心是以紧凑表格格式（ISON）将图数据序列化进 LLM 上下文窗口，基准测试报告其 token 用量低于 JSON/GraphML/RDF 等 10 种格式。功能覆盖节点与边 CRUD、多跳遍历、路径查找、图分析、类 Cypher 模式查询、ISONQL 声明式查询语言、ISONGraphantic 模式校验及跨语言位一致的 SVG 可视化。语义搜索（向量嵌入）为规划中、对应包未发布；图为简单图，不支持平行边。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 紧凑表格序列化格式，官方基准报告比格式化 JSON 省 68.6% token
- 节点/边 CRUD、多跳遍历、路径查找、连通性与环检测等图操作
- ISONQL：SQL 风格图查询语言，支持 Python/TypeScript/Rust/C++
- 五种语言实现发布于 PyPI/npm/crates.io，C# 库零依赖

## 适用场景

- 把知识图谱塞进 LLM 上下文窗口做图推理问答
- 多跳关系查询与遍历任务的数据层
- 需要模式校验（约束、无环、基数等）的图数据管理

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L12: ISONGraph is a **multi-language property graph library** designed specifically for LLM and AI applications. It is t
> L30: ISONGraph uses a compact tabular format that LLMs understand naturally:

## 星数曲线

```mermaid
xychart-beta
    title "ISON-format/isongraph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `356ebdf04719` · [字段定义](../../DATASET.md)*
