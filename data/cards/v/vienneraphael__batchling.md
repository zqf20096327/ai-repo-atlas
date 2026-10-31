# vienneraphael/batchling

⭐ 23 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/vienneraphael/batchling) · [官网](https://batchling.pages.dev) · 个人维护

**把异步 GenAI 调用转为半价批处理任务的 Python 插件**

Python 库加 CLI，将使用 asyncio 的 GenAI 异步函数或脚本转换为 Batch API 批处理任务，利用各提供商批处理接口通常约 50% 的成本折扣。提供 batchify 异步上下文管理器（两行代码嵌入）与 batchling CLI 两种使用方式，启动前给出成本节省明细。支持 Anthropic、Doubleword、Gemini、Groq、Mistral、OpenAI、Together、xAI 八家提供商，代码本身不改动。适合大规模离线评估、数据集分类、批量嵌入与合成数据生成等非实时负载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- batchify 上下文管理器两行代码嵌入现有异步脚本
- CLI 方式 batchling main.py:func 一条命令切换批处理模式
- 支持 8 家提供商（Anthropic/OpenAI/Gemini/Groq/Mistral/Together/xAI/Doubleword）
- 启动批处理前提供成本节省明细

## 适用场景

- 把现有 OpenAI 异步脚本改造成低成本批处理作业
- 大规模离线评测、数据集分类与批量嵌入
- 合成数据生成或批量结构化抽取等非实时负载

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: batchling is a frictionless, batteries-included plugin to convert any GenAI async function or script into half-cost
> L107: ## Supported providers
> L109: |Name|Batch API Docs URL|

## 星数曲线

```mermaid
xychart-beta
    title "vienneraphael/batchling 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f8fca70942cb` · [字段定义](../../DATASET.md)*
