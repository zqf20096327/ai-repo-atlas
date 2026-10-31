# magent4aci/openJiSi

⭐ 15 · Python · MIT · 推送 2026-06-03 · [GitHub](https://github.com/magent4aci/openJiSi) · 组织维护 · 中文 README

**将多个开源 LLM 组成集合系统的路由与聚合框架（ICML 2026 论文官方代码）**

论文 Beyond Gemini-3-Pro 的官方实现：把异构开源 LLM 池视为集体系统，推理时检索语义相近的支持集问题、估计各模型表现，再决定路由到单一专家模型或聚合多个专家回答。三大机制为查询-回答混合路由、基于支持集的聚合器选择、路由-聚合自适应切换，无需训练路由器。面向学术研究，也可用于搭建多 LLM 系统。提供 runner、配置层、数据适配器与评测工具，数据集发布在 Hugging Face（aisfuture/jisi_data），推理需 OpenAI 兼容的 embeddings 端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 查询-回答混合路由：结合查询相似度与回答侧证据估计模型能力
- 支持集驱动的聚合器选择与路由/聚合自适应切换
- 免训练：依赖支持集检索与分数估计，不训练单一路由器
- 发布含预计算嵌入缓存的数据集与 9 个基准的问题库

## 适用场景

- 复现论文中的多 LLM 路由与聚合实验
- 把多个开源 LLM 组成按问题分派专家的问答系统
- 在 AIME/GPQA/LiveCodeBench 等基准上评测路由决策

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L49: This is the official code repository for the paper *Beyond Gemini-3-Pro: Revisiting LLM Routing and Aggregation at 
> L51: The core design is minimalism and effective: instead of relying on one monolithic model, JiSi turns a pool of heter
> L61: JiSi contains three main mechanisms:

## 星数曲线

```mermaid
xychart-beta
    title "magent4aci/openJiSi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `041bc7fa27f1` · [字段定义](../../DATASET.md)*
