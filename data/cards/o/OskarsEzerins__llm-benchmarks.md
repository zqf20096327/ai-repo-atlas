# OskarsEzerins/llm-benchmarks

⭐ 78 · Ruby · MIT · 推送 2026-09-29 · [GitHub](https://github.com/OskarsEzerins/llm-benchmarks) · [官网](https://benchmarks.oskarsezerins.site/) · 个人维护

**面向 Ruby 代码生成的 LLM 基准测试套件与结果网站**

用 Ruby 编写的 LLM 基准测试工具：让模型完成 CSV 大规模处理、图最短路径、LRU 缓存、游程编码等性能类任务，以及日历系统调试、停车场逻辑修复等程序修复类任务，运行模型生成代码并聚合结果到交互式结果网站展示排名与指标。CLI 通过 RubyLLM/OpenRouter 读取模型能力信息，支持自动生成 thinking 变体。要求 Ruby 3.4+，通过 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 性能与程序修复两类基准（CSV 处理、图算法、LRU 缓存、逻辑修复等）
- CLI 从 RubyLLM/OpenRouter 读取模型能力并自动生成 thinking 变体
- bin/aggregate_results 将结构化元数据自动带入结果网站

## 适用场景

- 测试不同 LLM 生成 Ruby 代码的能力并对比结果
- 为新模型跑全套基准并提交 PR 收录
- 在交互式网站查看各模型排名与指标

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L80: **Performance Benchmarks** ⚡️
> L94: ### 🔬 `assert_equal(ai_promises, reality)`

## 星数曲线

```mermaid
xychart-beta
    title "OskarsEzerins/llm-benchmarks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e9261ee1a228` · [字段定义](../../DATASET.md)*
