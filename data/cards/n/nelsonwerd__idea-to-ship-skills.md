# nelsonwerd/idea-to-ship-skills

⭐ 90 · Shell · MIT · 推送 2026-08-04 · [GitHub](https://github.com/nelsonwerd/idea-to-ship-skills) · 个人维护

**Claude/Codex 可复用技能套件：把想法经验证、规划推进到交付**

面向个人与小团队开发者的 Agent Skills 组合套件，运行于 Claude 与 OpenAI Codex。手动层级含 ideate（概念锁定与路线图）、deep-dive（多专家代理并行分析+红队验证）、prompt-pack（生成自包含可独立交付的构建提示序列）、build-loop（迭代构建至接近完成）；自主层级 autopilot 端到端执行整条流水线，audit-and-fix 对既有代码库做审计-分诊-修复。作者声明自主层级为早期实验，产出为约80%完成度的首稿而非已验证产品，且 token 消耗量大（单次运行可达千万级 token）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ideate→deep-dive→prompt-pack→build-loop 四段流水线，技能独立可组合
- autopilot 端到端自主运行整条流水线，audit-and-fix 面向既有代码库
- deep-dive 采用并行专家代理+对抗红队，输出带 1-10 置信度判定
- 自主层级声明为实验性：约80%完成度上限、合成反馈不作为市场验证

## 适用场景

- 动手编码前先锁定并验证要构建什么
- 把大需求拆成可独立交付的自包含构建提示
- 让 autopilot 自主跑完从想法到首稿应用的流水线

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Composable Agent Skills — for Claude and OpenAI Codex — that take an idea from *fuzzy* → *validated* → *sequenced 
> L5: Most "build with AI" workflows skip the hard half. They jump straight to code — and skip *deciding what's actually w
> L13: They're **separate, composable** skills on purpose — sharp triggers, lean context, independent use. Run them **by h

## 星数曲线

```mermaid
xychart-beta
    title "nelsonwerd/idea-to-ship-skills 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-26"]
    y-axis "stars" 87 --> 91
    line [88, 89, 90, 90]
```

2026-10-18 88 → 2026-10-26 90（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `501100a3c187` · [字段定义](../../DATASET.md)*
