# ScholarXIV/enkokilish_bench

⭐ 27 · Svelte · MIT · 推送 2025-12-27 · [GitHub](https://github.com/ScholarXIV/enkokilish_bench) · [官网](https://enkokilish-bench.vercel.app) · 组织维护

**阿姆哈拉语谜语（Enkokilish）LLM 评测基准数据集**

面向 LLM 的阿姆哈拉语谜语基准，用于评估模型理解、推理与解答 Enkokilish 谜语的能力。基于 Evalite 评测框架构建，通过 AI-SDK 调用 LLM；数据集（谜语及答案）存于 datasets/enkokilsh.ts，持续更新并接受社区贡献。使用方式为克隆仓库、在 .env 配置 API Key 后运行 pnpm eval:dev，在 localhost:3000 查看结果。仓库结构可复用于构建其他基准。

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

- 阿姆哈拉语谜语数据集（谜语与答案，持续更新）
- 基于 Evalite 框架，经 AI-SDK 调用 LLM
- 可复用结构：改数据集与标题即建新基准

## 适用场景

- 评测 LLM 对阿姆哈拉语谜语的理解与推理能力
- 复用仓库结构搭建自定义评测基准
- 贡献或获取低资源语言推理评测数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: This is a new benchmark for LLMs focused on evaluating an LLMs ability to understand, reason and solve Amharic riddl
> L11: All the riddles and their answers are listed in datasets/enkokilsh.ts file and will keep on being updated.

## 星数曲线

```mermaid
xychart-beta
    title "ScholarXIV/enkokilish_bench 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-31"]
    y-axis "stars" 25 --> 28
    line [27, 26, 27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `afd67947082f` · [字段定义](../../DATASET.md)*
