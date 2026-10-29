# bonnguyenitc/antigravity-superpowers

⭐ 20 · Python · MIT · 推送 2026-05-08 · [GitHub](https://github.com/bonnguyenitc/antigravity-superpowers) · [官网](https://www.npmjs.com/package/agy-superpowers) · 个人维护

**为 Google Antigravity agent 移植的 Superpowers 技能库**

将上游 Superpowers 技能库移植为 Google Antigravity 原生可用的技能、工作流与规则集合：通过 npx 或全局 npm 安装脚手架生成 .agent/ 目录，含 23 个技能；Antigravity 依据 alwaysApply 规则在每次响应前自动读取并选择技能。提供 /brainstorm→/write-plan→/execute-plan→/code-review 核心开发循环，以及 /debug、/publish、/update-superpowers 等工作流；技能经 AI 补丁移除非 Antigravity 引用，覆盖前端、移动、产品、UX、计费、i18n 等领域。

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

- 23 个可组合技能，agent 基于自然语言请求自动选择激活
- 五步开发循环：/brainstorm → /write-plan → /execute-plan → /code-review → merge
- npx 一条命令脚手架生成 .agent/ 目录，无需手动调用
- AI 驱动的技能补丁系统，/update-superpowers 同步上游并重写规则

## 适用场景

- 在 Google Antigravity 中按结构化流程从想法走到可合并代码
- 让编码 agent 在前端、移动、产品、UX、计费等领域自动调用专业技能
- 通过自动技能检查规范 agent 的开发行为（TDD、调试、验证、代码评审）

## 场景标签

`提示工程` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L8: This repo ports the Superpowers skills library to work natively with **Google Antigravity agent**, with Antigravity-
> L47: **Antigravity automatically reads skills before every response.** You don't need to invoke them manually — the `sup

## 星数曲线

```mermaid
xychart-beta
    title "bonnguyenitc/antigravity-superpowers 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f92aef5aeb53` · [字段定义](../../DATASET.md)*
