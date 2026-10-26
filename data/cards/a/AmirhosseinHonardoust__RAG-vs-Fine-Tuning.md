# AmirhosseinHonardoust/RAG-vs-Fine-Tuning

⭐ 26 · MIT · 推送 2025-10-31 · [GitHub](https://github.com/AmirhosseinHonardoust/RAG-vs-Fine-Tuning) · 个人维护

**面向开发者的 RAG 与微调选型教程：原理、对比与决策框架**

一份以 README 形式组织的教程文档：解释 RAG 与微调两种 LLM 适配技术的工作原理（含分步流程与简化代码示例），从知识来源、延迟、维护成本、隐私等维度给出对比表格，并提供决策树、真实场景选型表（客服机器人/法律助手/摘要器等）、混合方案说明与实操建议（重叠分块、LoRA/QLoRA 等）。给需要在项目中决定采用哪种方案的 LLM 开发者阅读；本仓库不含可运行的软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 与微调的工作原理分步说明与简化 Python 示例
- 多维对比表（成本/维护/隐私/可扩展性）与决策树
- 真实场景选型表与混合方案（Hybrid）流程
- 实操建议：重叠分块、LoRA/QLoRA、检索与生成质量验证

## 适用场景

- 我在为 LLM 项目决定用 RAG 还是微调时查阅此指南
- 我需要向团队解释两种技术的成本与维护差异
- 我需要参考客服机器人、法律助手等场景的选型结论

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: In today’s rapidly evolving AI landscape, two techniques dominate how developers adapt large language models (LLMs) 
> L6: This guide explores each method in detail, how they work, when to use them, their pros and cons, and how combining b

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/RAG-vs-Fine-Tuning 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-26 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7f26b302d58d` · [字段定义](../../DATASET.md)*
