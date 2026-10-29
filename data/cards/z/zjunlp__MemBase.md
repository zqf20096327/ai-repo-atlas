# zjunlp/MemBase

⭐ 51 · Python · MIT · 推送 2026-09-03 · [GitHub](https://github.com/zjunlp/MemBase) · 组织维护

**长期对话记忆层的统一评测基准框架**

面向长期对话记忆任务的记忆层评测框架：以记忆构建、记忆检索、问答评测三阶段流水线，统一评测 A-MEM、Mem0、MemOS 等 8 种记忆层与 LongMemEval、LoCoMo 等 4 个数据集。提供断点续跑、monkey-patch 式非侵入 token 消耗统计、执行图追踪与模块化扩展接口（实现 MemBaseLayer/MemBaseDataset 即可接入新方法）。默认输出 token 级 F1、BLEU 与 LLM-as-a-Judge 指标。各记忆层基线依赖可能冲突，建议各自建独立虚拟环境安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段统一流水线评测 8 种记忆层 × 4 个数据集
- 非侵入式 LLM API token 消耗统计（monkey-patch）
- 记忆构建-检索-使用的执行图追踪（部分基线支持）
- 实现 MemBaseLayer/MemBaseDataset 接口即可扩展新方法与数据集

## 适用场景

- 在同一流水线下对比不同记忆层基线的性能
- 统计各记忆方法的 token 消耗成本
- 追踪记忆增强 agent 的记忆生命周期做失败归因

## 场景标签

`Agent 记忆` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: A comprehensive evaluation framework for benchmarking various memory layers on long-term conversational memory tasks
> L86: Using the retrieved memories as context, a question-answering model generates answers for each question. The evalua

## 星数曲线

```mermaid
xychart-beta
    title "zjunlp/MemBase 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-29 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0528fb31cc1e` · [字段定义](../../DATASET.md)*
