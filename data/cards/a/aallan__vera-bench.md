# aallan/vera-bench

⭐ 15 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/aallan/vera-bench) · [官网](https://veralang.dev) · 个人维护

**评测 LLM 在 Vera 语言中代码生成能力的基准套件**

VeraBench 用 60 道题、五个难度层级评测 LLM 在 Vera（一种为 LLM 设计、缺席于所有训练集的静态类型契约语言）中的代码生成，以 % solved（pass@1）计分，与 Python/TypeScript 及 Aver、AILANG 等零训练数据语言对比。支持两种模式：给定契约只写函数体（Vera），或从英文题面自行推导类型与契约（Vera NL）。README 报告九个模型、三个供应商的结果，并说明基准已接近饱和、单次运行无 pass@k 等限制。面向研究 LLM 代码生成与语言设计的人员。

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

- 60 道题、五个难度层级，覆盖契约、ADT、递归终止与效果
- 双模式评测：按规范写实现与从自然语言自建规范
- 与 Python/TypeScript 及 Aver、AILANG 等零训练数据语言对比
- 指标为 % solved（pass@1），拒绝/编译失败/错误答案均计为未解

## 适用场景

- 比较各 LLM 在面向模型设计的编程语言中的代码生成表现
- 研究语言设计（类型约束、契约）对 LLM 生成代码可验证性的影响
- 复现或扩展跨语言、跨模型世代的代码生成评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: A benchmark for evaluating LLM code generation in Vera, a programming language designed for large language models (L
> L239: VeraBench measures whether LLMs write better code in a language designed for

## 星数曲线

```mermaid
xychart-beta
    title "aallan/vera-bench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bd25b031606f` · [字段定义](../../DATASET.md)*
