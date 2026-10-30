# FANzR-arch/Numerologist_skills

⭐ 1,527 · Python · 推送 2026-10-16 · [GitHub](https://github.com/FANzR-arch/Numerologist_skills) · [官网](https://numerologist-skills.vercel.app) · 个人维护 · 中文 README

**传统术数 AI skills：用固定排盘脚本与口径约束减少 LLM 幻觉**

面向奇门遁甲、紫微斗数、四柱八字三个术数体系的 Claude Code/Codex agent skills 集合。每个 skill 由 SKILL.md（触发条件、工作流、输出约束）、references（规则集、术语表、口径说明）与 scripts（刚性计算的外部 Python CLI）组成。设计原则包括先追问再输出、历法换算与排盘计算外包给确定性脚本、先声明流派口径再下结论。高风险场景仅输出结构化参考，不替代专业建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个术数体系（奇门遁甲/紫微斗数/四柱八字）的模块化 skills
- 固定排盘计算交给确定性 Python CLI 脚本执行
- references 固定术语、流派口径与判断顺序
- 高风险场景（健康/法律/财务）不替代现实专业建议

## 适用场景

- 为 Claude Code/Codex 类 agent 添加可审计的术数排盘技能
- 让 LLM 排盘时先补全参数、声明流派口径再输出
- 用确定性脚本替代模型自行进行历法换算与排盘计算

## 场景标签

 · 领域:传统文化/LLM 约束工程

## 证据(README 行号)

> L3: 本项目把传统术数相关的 AI skill 拆成可审计、可复用、可逐步扩展的工程模块。目标不是把模型包装成“更会玄学”，而是尽量减少它在排盘、流派口径、步骤顺序和解释链路上的幻觉。
> L15: - `SKILL.md`：主技能说明、触发条件、工作流、输出约束

## 星数曲线

```mermaid
xychart-beta
    title "FANzR-arch/Numerologist_skills 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 1514 --> 1528
    line [1515, 1527]
```

2026-10-29 1,515 → 2026-10-30 1,527（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `afa445de58c1` · [字段定义](../../DATASET.md)*
