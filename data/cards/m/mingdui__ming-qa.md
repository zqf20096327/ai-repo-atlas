# mingdui/ming-qa

⭐ 42 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/mingdui/ming-qa) · 个人维护 · 中文 README

**端到端 QA 验收编排技能：上下文到报告自动衔接，用例处人工把关**

以 Agent Skill 形式分发的端到端 QA 验收工具包，支持 Claude Code、Codex、Cursor 及遵循 SKILL.md 规范的 agent。把一次功能验收拆成固定阶段：上下文收集、风险分析、用例设计、脚本生成、执行与修复、代码审查、报告，仅在用例确认处设人工门禁。产物落在目标项目 .qa-agent/ 目录，支持回归重跑与增量加用例。CLI 仅用 Python 标准库，E2E 测试基于 Playwright；不内置外部服务地址，LLM 网关与告警 webhook 均为可选配置。

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

- 验收流程拆为固定阶段，仅用例确认一处人工门禁
- 8 个技能经 npx skills 一键安装，跨 agent 通用目录部署
- CLI 仅用 Python 标准库，无第三方运行时依赖
- 产物集中在 .qa-agent/ 目录，用例与脚本可随 git clone 沉淀

## 适用场景

- 让 coding agent 对我的模块做端到端功能验收
- 回归时只重跑已有脚本，不重复分析设计
- 为既有项目补充新场景的验收用例与脚本

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 端到端 QA 验收工具包，以 **Agent Skill** 形式分发，支持 Claude Code、Codex、Cursor
> L10: 上下文收集 → 风险分析 → 用例设计 → 【你来确认】 → 脚本生成 → 执行与修复 → 代码审查 → 报告

## 星数曲线

```mermaid
xychart-beta
    title "mingdui/ming-qa 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-26 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `354f00d8cc7b` · [字段定义](../../DATASET.md)*
