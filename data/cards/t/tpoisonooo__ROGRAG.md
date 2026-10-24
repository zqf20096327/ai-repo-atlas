# tpoisonooo/ROGRAG

⭐ 201 · Python · BSD-3-Clause · 推送 2025-12-12 · [GitHub](https://github.com/tpoisonooo/ROGRAG) · 个人维护 · 中文 README

**鲁棒优化的 GraphRAG 框架，两阶段检索提升 LLM 领域问答精度**

ACL 2025 demo track 论文配套框架：通过双层检索与逻辑形式两阶段机制增强 LLM 在专业领域话题上的表现，支持增量数据库构建、模糊匹配与结构化推理。README 报告在 SeedBench 上较主-stream 方法有提升，并给出四组 QA 对比数据。由 HuixiangDou 改进而来，API 与 v1 兼容（Wechat/Lark/Web 可接入），提供 Docker（CMD/Swagger/Gradio）与源码两种运行方式，2025 年 11 月起支持多数据库。受许可限制，代码与测试结论公开但测试数据不提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段（dual-level + logic form）检索机制
- 增量数据库构建与模糊匹配、结构化推理
- 多数据库支持，Gradio UI 与 Swagger Server API
- API 与 HuixiangDou v1 兼容（Wechat/Lark/Web）

## 适用场景

- 在专业领域知识库上构建高精度 RAG 问答服务
- 通过 Swagger API 或 Gradio 界面部署领域问答
- 以增量方式维护领域知识图谱数据库

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L9: ROGRAG enhances LLM performance on specialized topics using a robust GraphRAG approach. It features a two-stage (dua
> L18:  - Two-stage retrieval for robustness
> L38: - 1. Run from Docker (CMD / Swagger Server API / Gradio)

## 星数曲线

```mermaid
xychart-beta
    title "tpoisonooo/ROGRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 200 --> 202
    line [201, 201]
```

2026-10-18 201 → 2026-10-24 201（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a25acb9694cd` · [字段定义](../../DATASET.md)*
