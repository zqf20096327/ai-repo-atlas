# SolidLao/SQLBarber

⭐ 16 · Python · 推送 2026-04-07 · [GitHub](https://github.com/SolidLao/SQLBarber) · 个人维护

**LLM 驱动的定制化 SQL 负载生成系统，用于数据库基准测试**

SIGMOD 2026 论文的配套系统：面向数据库研究者与开发者，生成定制化且贴近真实分布的 SQL 负载。用户提供自然语言模板规格与目标代价分布（如基数、执行代价），流程为 LLM 生成 SQL 模板、profiling 评估模板代价覆盖、迭代精炼与剪枝，再用自适应贝叶斯优化搜索谓词取值，使实例化查询匹配目标代价分布。已在 PostgreSQL v14.9（Docker 容器）上测试，依赖 TPC-H/IMDB 数据库与 BenchBase（需 JDK），通过脚本复现实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 生成 SQL 模板 + 贝叶斯优化谓词搜索，输出匹配目标代价分布的负载
- 支持从 Snowset/Redset 等高层负载统计构造可执行基准
- 输出含模板、workload.json、统计摘要与代价分布可视化
- 提供复现全部实验的脚本

## 适用场景

- 为评估 DBMS 特性或查询优化器构造定制 SQL 基准
- 将公开负载统计转化为可执行的真实基准
- 为学习型 DBMS 组件生成大规模多样化训练查询

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L18: **SQLBarber** is a system based on Large Language Models (LLMs) to generate customized and realistic SQL workloads.
> L20: - 📌 ① SQLBarber employs an LLM-powered SQL Template Generator to create customized SQL templates based on user-defi

## 星数曲线

```mermaid
xychart-beta
    title "SolidLao/SQLBarber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `0f44c1aff4c1` · [字段定义](../../DATASET.md)*
