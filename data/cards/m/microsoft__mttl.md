# microsoft/mttl

⭐ 116 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/microsoft/mttl) · 组织维护

**微软的模块化 LLM 研究代码库：LoRA 库构建、路由与合并**

MTTL 是微软发布的研究代码库，围绕 LLM 的模型复用、模型重组与参数高效微调（PEFT），聚焦少样本与零样本学习场景。它是多篇 ArXiv 论文（Arrow+MBC、MHR、Polytropon）的配套代码，提供 LoRA 专家库的构建、训练与评测，以及 Arrow、PhatGOOSE 等适配器路由与合并方法。官方声明仅供研究使用，未在生产环境测试，评测以英文 NLP 任务为主（基于 Phi-2、Mistral 等模型），多语言场景性能未知。

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

- LoRA 专家库的构建、训练与评测代码
- 支持 Arrow、PhatGOOSE 等多种适配器路由与合并方法
- 配套多篇 ArXiv 论文（Arrow+MBC / MHR / Polytropon）

## 适用场景

- 复现模块化 LLM 与 LoRA 路由相关论文实验
- 研究少样本/零样本场景下的适配器复用与重组
- 在自建 LoRA 库上实验不同路由策略

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: MTTL is a repository focusing on building LLMs that focus on model reusability, model recombination, and parameter-e
> L15: :point_right: Navigate here for a quick tutorial on how to use MTTL to route and merge adapters with Arrow or PhatG

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/mttl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-26 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `cd452af15101` · [字段定义](../../DATASET.md)*
