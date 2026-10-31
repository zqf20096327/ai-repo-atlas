# dososo/HarmonyOS-Design

⭐ 39 · Python · Apache-2.0 · 推送 2026-07-15 · [GitHub](https://github.com/dososo/HarmonyOS-Design) · 个人维护 · 中文 README

**面向 AI Agent 的 HarmonyOS/ArkUI 设计规则与 Skill 库及评测基线**

独立非官方项目，将公开的 HarmonyOS/OpenHarmony 设计原则与 ArkUI 能力整理为 3 个可触发的 Agent Skill（设计主 Skill、严格 Reviewer、动效词汇）、38 条带来源等级（H1–H4）与稳定 ID 的机器可读规则，以及 52+17+13 条评测基线；另含已在模拟器（API 21）验证的 ArkUI 示例工程。默认完全离线、不写用户工程，自动修复全部关闭。给 AI Coding Agent、HarmonyOS 设计师与 ArkUI 开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 个 Agent Skill + 38 条 JSON Schema 校验的机器可读规则
- 52 条触发 / 17 条 Review / 13 条路由评测基线
- 异步状态真实性约束（Idle→Acknowledged→Pending→Confirmed/Failed）
- 含已在 HarmonyOS 模拟器验证的 ArkUI 示例工程（4 个场景）

## 适用场景

- 让 AI Coding Agent 审视 ArkTS 页面的设计、动效与无障碍
- 从零建立鸿蒙应用的设计基线与验收矩阵
- 把模糊的动效手感翻译为术语与 ArkUI 落点

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: > 面向 AI Coding Agent、HarmonyOS 设计师与 ArkUI 开发者的**独立、非官方**设计与动效 Skill、规则库与评测基线。把公开的 HarmonyOS / OpenHarmony 设计原则和 ArkU
> L100: **2 · 38 条机器可读规则** — 每条带来源、范围、证据、ArkUI 落点、检测方式、稳定性与知识层；JSON Schema 校验，稳定 ID，可供静态扫描与工具接入。
> L108: **6 · 真机验证 + 评测基线** — 含 52 条触发 Eval、17 条 Review Eval、13 条 Skill 路由 Eval，以及可运行、已在模拟器验证的 ArkUI 示例工程。

## 星数曲线

```mermaid
xychart-beta
    title "dososo/HarmonyOS-Design 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-31 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f8b572652d68` · [字段定义](../../DATASET.md)*
