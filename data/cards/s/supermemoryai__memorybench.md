# supermemoryai/memorybench

⭐ 331 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/supermemoryai/memorybench) · [官网](https://supermemory.ai/docs/memorybench/overview) · 组织维护

**可插拔评测框架：横向评测记忆/上下文系统与 RAG 表现**

supermemoryai 维护的评测基准框架，面向评估对话记忆与 RAG 系统的开发者：将基准数据集（LoCoMo、LongMemEval、ConvoMem）灌入待测 provider（Supermemory、Mem0、Zep），经 ingest→index→search→answer→evaluate 六阶段流水线产出准确率、延迟与 token 消耗，并汇总为 MemScore 三元组。支持 judge 模型可替换（GPT-4o、Claude、Gemini）、多 provider 并排对比、阶段级断点续跑与实时 Web UI。基于 Bun/TypeScript 运行，需配置各 provider API key。

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

- 六阶段流水线（ingest→index→search→answer→evaluate→report）阶段级断点续跑
- MemScore 复合指标：accuracy% / latencyMs / contextTokens 三元组
- 多 provider 同一基准并排对比，judge 模型可替换
- CLI 全套命令与实时 Web UI 查看运行与失败详情

## 适用场景

- 对比 Supermemory、Mem0、Zep 等记忆系统在同一基准上的表现
- 为自己的记忆/RAG 系统接入自定义基准做评测
- 分析问答失败案例与延迟、token 成本权衡

## 场景标签

`模型评测` `RAG` · 领域:评测与运维

## 证据(README 行号)

> L3: A pluggable benchmarking framework for evaluating memory and context systems.
> L12: - 🆚 Multi‑provider comparison: run the same benchmark across providers side‑by‑side
> L45: |`run`|Full pipeline: ingest → index → search → answer → evaluate → report|

## 星数曲线

```mermaid
xychart-beta
    title "supermemoryai/memorybench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 329 --> 332
    line [330, 331, 331]
```

2026-10-18 330 → 2026-10-26 331（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `414f6da8f846` · [字段定义](../../DATASET.md)*
