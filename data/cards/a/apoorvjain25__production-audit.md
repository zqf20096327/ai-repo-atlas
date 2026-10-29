# apoorvjain25/production-audit

⭐ 18 · MIT · 推送 2026-06-25 · [GitHub](https://github.com/apoorvjain25/production-audit) · [官网](https://pulsehq.tech) · 个人维护

**面向 Claude Code 的产品审计技能：24 视角循环扫描至收敛**

一个 Claude Code skill（SKILL.md 提示工程文件），对产品做全量审计：先盘点全部界面（页面、路由、任务、prompt、邮件、locale），再用 24 个审计视角逐轮扫描，连续两轮无新发现才停止；fix 模式在修复后继续验证循环直至两轮无 CRITICAL/HIGH。每条发现必须锚定 file:line 或 URL+selector，默认逐条对代码核验。也可作为单文件 PROMPT.md 用于 Cursor、Windsurf、Copilot、aider 等。限制：非确定性、大仓库耗时数小时且有 token 开销、收敛不等于证明完备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个审计视角 + 3 个验证专用视角的收敛式扫描
- 每条发现强制锚定 file:line 或 URL+selector，默认逐条核验
- claim-vs-code 视角核验公开承诺与实现的一致性
- 支持 .audit-ignore 抑制已分诊的误报，且审计只读不写该文件

## 适用场景

- 发布前对整个产品做多轮深度审计
- 核验文档/营销页面上的承诺是否有对应代码实现
- fix 模式下按严重度分波修复并循环验证直至收敛

## 场景标签

`代码审查` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L6: Claude Code Skill
> L113: **Claude Code (easiest)**: install as a plugin.
> L130: **Everything else** (Cursor, Windsurf, Copilot, aider, raw API): paste PROMPT.md. Same methodology, single file, z

## 星数曲线

```mermaid
xychart-beta
    title "apoorvjain25/production-audit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9961754b8c40` · [字段定义](../../DATASET.md)*
