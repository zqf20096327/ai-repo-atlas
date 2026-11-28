# Ndarrr07/pro-llm-api-hub

⭐ 13 · HTML · 推送 2026-11-27 · [GitHub](https://github.com/Ndarrr07/pro-llm-api-hub) · 个人维护

**给研究者的免费 LLM API 结构化数据集：可溯源、可复验**

以 JSON 扁平表形式收录各家大模型 API 条目，每条记录按固定 schema 记录名称、模型类别（文本/语音/嵌入/图像等）、免费额度、注册条件、OpenAI 兼容标志、速率限制与数据驻留等字段，并保留来源文档引用与核验日期。无法从官方文档确认的字段标记 unverified 而非推断；按行级核验日期区分 confirmed/provisional/unconfirmed 三级置信度。数据集以 CC BY 4.0 发布，附引用格式说明。提供 PowerShell 脚本入口，要求 Windows 与 PowerShell 5.1+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 固定 schema 的 JSON 数据集，覆盖免费额度、注册条件、速率限制、OpenAI 兼容标志等字段
- 每条记录带来源文档引用与 UTC 核验日期，无法确认的字段标 unverified
- 行级三级置信度（confirmed/provisional/unconfirmed）与保留 superseded 值的变更历史
- CC BY 4.0 许可发布，附学术引用格式

## 适用场景

- 为研究对比各 LLM API 的免费额度与使用条款
- 筛选无信用卡/无手机验证要求的免费模型接口
- 在自己的分析流水线中引用带溯源的 API 条目数据

## 场景标签

`精选清单` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # Pro LLM API Hub: Structured Multi LLM API Reference — Dataset
> L7: This dataset documents the Pro LLM API Hub, a structured compilation of large language model APIs assembled to suppo
> L18: The dataset is organized as a flat table of level records, serialized as JSON, with one row per API offering. Each 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `f76b2049e341` · [字段定义](../../DATASET.md)*
