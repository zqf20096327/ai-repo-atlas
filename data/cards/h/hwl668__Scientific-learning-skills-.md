# hwl668/Scientific-learning-skills-

⭐ 15 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/hwl668/Scientific-learning-skills-) · 个人维护 · 中文 README

**面向学生的 Agent 技能包：让 AI 先诊断卡点再讲解**

一套 9 个 Agent Skill（结构化 Markdown 指令集），加载到 Claude Code、Codex、Cursor 等宿主后，让 AI 以“先诊断再讲解”的方式辅导学习：识别 6 类学习卡点、零基础讲解、错因归类、单词全息词典、SM-2 风格间隔复习记忆等。另含可独立运行的实验性 CLI 模块（路由、诊断、记忆调度、评测、Prompt 编译）与 TF-IDF learned-router 基线。README 明确标注示例为手工编写、未提供真实用户研究证据，模块尚未串联为端到端产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 9 个 Skill 覆盖零基础入门、卡点诊断、错题复习、背诵、学习规划等 9 类任务
- SM-2 风格记忆调度与跨会话薄弱点追踪（依赖可写 memory/ 目录）
- 可独立运行的 CLI 模块：路由、认知诊断、评测运行器、Prompt 编译器
- TF-IDF + Logistic Regression 的 learned-router 路由基线（合成数据训练）

## 适用场景

- 在 Claude Code 等宿主中加载 Skill，获得先诊断再讲解的学习辅导
- 背单词、背政治大题时自动存入记忆并按间隔复习
- 用 CLI 模块单独运行路由、诊断与静态结构回归评测

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: > A student-facing Agent Skills prototype for diagnosis-before-explanation tutoring.
> L45: |"我不想选，直接用一个大的学习入口"|`scientific-learning` — 总入口，先路由再调用子 skill|

## 星数曲线

```mermaid
xychart-beta
    title "hwl668/Scientific-learning-skills- 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3602e7d2cd01` · [字段定义](../../DATASET.md)*
