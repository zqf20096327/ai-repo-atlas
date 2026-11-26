# NadeenAhmad/AccessGuruLLM

⭐ 17 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/NadeenAhmad/AccessGuruLLM) · 组织维护

**面向无障碍研究者的 HTML 违规检测/修正系统与基准数据集**

ASSETS '25 论文的配套仓库：结合 Axe-Playwright 无障碍测试引擎与 LLM，对 HTML 做语法/布局与语义两类违规检测，并通过提示策略（含违规分数驱动的再提示循环）生成修正代码。随仓库提供三类违规的分类体系，以及覆盖 112 种类型、3500 余条真实网页违规的标注数据集（存于 DaRUS，CC BY 4.0），检测与修正流程以 Notebook 形式提供，另含 ACCESS 基线数据集用于对比评估。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语法/布局与语义双检测器：Axe-Playwright 引擎 + LLM 语义检测
- 修正模块对生成代码赋违规分数，分数未清零时执行纠正性再提示
- 3,500+ 真实网页违规标注数据集，覆盖 112 种违规类型与三个类别
- 违规条目含 WCAG 引用、影响等级与补充信息字段

## 适用场景

- 评估不同 LLM 在网页无障碍自动修复任务上的效果
- 用真实违规数据微调面向 HTML 无障碍修正的模型
- 对规则型与 AI 型无障碍工具做基准对比
- 训练模型检测或解释未见过的布局中的违规

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L12: **AccessGuru** is a novel system that combines large language models (LLMs) and accessibility testing tools to **au
> L19:  - `AccessGuruDetect`: Detect violations (Axe-Playwright + LLM) [SyntaxLayout Notebook] [Semantic Notebook]
> L67: ## 📊 Our Dataset


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `021f32761e4d` · [字段定义](../../DATASET.md)*
