# yjoonjang/rebuttal-skills

⭐ 19 · Python · NOASSERTION · 推送 2026-07-30 · [GitHub](https://github.com/yjoonjang/rebuttal-skills) · [官网](https://yjoonjang-reviewsearch.hf.space) · 个人维护

**论文评审回复技能包：检索真实评审先例并代跑实验起草 rebuttal**

面向论文作者的 agent 技能包，以插件形式装入 Claude Code 或 Codex：包含 ReviewSearch（基于 205,988 条 ICLR/ICML/NeurIPS/COLM 真实评审与作者回复训练的混合检索引擎，稠密+稀疏编码器经 RRF 融合）和 RebuttalDraft 五步流程——读取论文与评审提取并分级质疑、检索真实先例、在用户工作区设计并经确认后运行实验、以实测数字起草回复、自我批评校验，输出逐评审人的可粘贴草稿到 rebuttal/ 目录。数据来自 OpenReview（CC-BY-4.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 205,988 条真实评审与作者回复构建的混合检索（dense+sparse+RRF）
- 在用户工作区设计并运行实验，回复中填入实测数字
- 五步流程：提取质疑→检索先例→跑实验→起草→以敌意评审视角自我校验
- 逐评审人输出可粘贴草稿与数字溯源（RESULTS.md/grounding.md）

## 适用场景

- 收到审稿意见后，让 agent 检索同类质疑的真实回应方式
- 在代码仓库中自动补跑实验，把口头承诺变成结果表格
- 按评审人逐个生成可粘贴的 rebuttal 草稿

## 场景标签

`编码 Agent` `科研工具` · 领域:编码与开发

## 证据(README 行号)

> L15: **rebuttal-skills** turns your paper and its reviews into a paste-ready, per-reviewer rebuttal. Two skills,
> L30: 3. **Plan & Run**: inventories your workspace, designs the experiments, and runs them after your confirmation.

## 星数曲线

```mermaid
xychart-beta
    title "yjoonjang/rebuttal-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0f7d152b1fa5` · [字段定义](../../DATASET.md)*
