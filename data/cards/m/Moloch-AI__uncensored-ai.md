# Moloch-AI/uncensored-ai

⭐ 18 · Python · MIT · 推送 2026-11-13 · [GitHub](https://github.com/Moloch-AI/uncensored-ai) · [官网](https://molochai.dev/uncensored-ai?utm_source=github&utm_medium=oss&utm_campaign=uncensored-ai) · 组织维护

**低拒绝（uncensored）语言模型的开发者参考指南与模型比较工具**

面向开发者的参考文档仓库：解释拒绝行为的来源与降低方式（abliteration、微调、提示词），并排对比自托管运行时与 MolochAI 托管 OpenAI 兼容 API 的内存、运维、数据控制与成本差异。覆盖 MolochAI 五个 refusal-reduced 模型的卡片事实、Quickstart（curl/Python/Node）、错误排查表与 FAQ；仓库自带 compare_models.py 脚本，可向任意 OpenAI 兼容端点批量发送提示并输出 Markdown/CSV 对比表。指南内容除 MolochAI 特有部分外适用于任何 OpenAI 兼容端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对比自托管（llama.cpp/Ollama/LM Studio/vLLM）与托管 API 的部署决策表
- compare_models.py 将提示批量发送到多个模型并输出延迟/token/摘要对比表
- 覆盖 401/429/524 等每个 HTTP 状态与参数被忽略等问题的排查表
- Python/TypeScript/CLI SDK 从 GitHub 安装，提供类型化错误处理

## 适用场景

- 在自托管与托管 API 之间做部署选型评估
- 了解 abliteration 等降低拒绝行为的方法及其代价
- 用自有提示批量对比多个 OpenAI 兼容模型的表现
- 排查调用 OpenAI 兼容 API 时的错误

## 场景标签

`模型评测` `精选清单` · 领域:评测与运维

## 证据(README 行号)

> L6: A developer's reference for uncensored (less-restricted) language models: what they are, how they get that way, how 
> L10: "Uncensored" is what people search for; "refusal-reduced" is what it means. This guide explains the concepts withou
> L136: `tools/compare_models.py` sends each prompt in a text or JSONL file to several models on any OpenAI-compatible end

## 星数曲线

```mermaid
xychart-beta
    title "Moloch-AI/uncensored-ai 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-19", "2026-11-26"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-11-18 17 → 2026-11-26 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `530f826ac586` · [字段定义](../../DATASET.md)*
