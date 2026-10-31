# Vir-Multiplicis/ai-frameworks

⭐ 28 · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/Vir-Multiplicis/ai-frameworks) · 个人维护

**面向 AI 安全与对齐的推理时提示词框架集合（ELT）**

Vir Multiplicis 随 Medium 系列 Web 文章开发的提示词框架仓库：以 Epistemic Lattice Tethering（ELT）为核心，包含已部署的 Adversarial Convergence、Ontology Anchor、Earned Confidence Gating、Alignment Governor 等组件，通过推理时提示词机制约束 LLM 的推理质量、长上下文一致性与真值寻求对齐。组件以标记化提示词文档形式提供于 ELT 文件夹，随系列文章持续更新；另有 ELT-H/C/A 变体与开发中的 ELT-Agentic。内容以 CC BY 4.0 授权，需署名引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 个已部署组件：对抗收敛、本体锚定、置信度门控、对齐治理器等
- 针对长上下文的 W 形注意力加权与上下文治理层（Context Management）
- ELT-H/C/A 三种变体分支与开发中的 ELT-Agentic 扩展
- 内容以 CC BY 4.0 许可发布并要求署名

## 适用场景

- 为长对话 LLM 交互添加推理时的认识论约束提示词
- 降低模型谄媚与流畅性伪装，校准置信度表达
- 作为 AI 安全与对齐的提示工程参考材料

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A repository of prompt frameworks developed alongside the AI safety, governance, and alignment series published on M
> L84: See the `/Epistemic Lattice Tethering (ELT)` folder for current prompts and implementations of the key components.

## 星数曲线

```mermaid
xychart-beta
    title "Vir-Multiplicis/ai-frameworks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d1558b8c9ea9` · [字段定义](../../DATASET.md)*
