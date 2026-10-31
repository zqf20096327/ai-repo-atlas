# Popschlock/Claude-Harness-Generator

⭐ 14 · MIT · 推送 2026-09-24 · [GitHub](https://github.com/Popschlock/Claude-Harness-Generator) · 个人维护

**为 Claude Code 生成/校验/升级项目 harness 配置的生成器**

面向 Claude Code 用户的 harness 生成工具：通过访谈（或从 4 个基础预设、16 个领域预设中选取）生成完整项目配置，包括 CLAUDE.md、规则、专用 agents、斜杠命令技能、记忆与权限范围；也提供对已有 harness 的结构校验、最佳实践审计与升级。架构采用编排器 + 5 个子代理模式，产物落盘。前置要求为 Claude Code CLI 与 Anthropic API key 或 Claude 订阅，完整生成流程约 10-20 分钟。

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

- 访谈驱动生成完整 Claude Code harness（CLAUDE.md+规则+agents+技能+记忆+权限）
- 4 个基础预设 + 16 个捆绑领域预设，高风险领域内置职业/合规保障
- 编排器+5 子代理架构，产物写入磁盘（artifact-first）
- 提供 /validate-environment、/upgrade-environment、/update 等校验与自学习命令

## 适用场景

- 新项目快速搭建符合最佳实践的 Claude Code 配置
- 审计并升级已有项目 harness 的一致性与质量
- 法律、金融、安全等高风险领域选用带合规保障的领域预设

## 场景标签

`提示工程` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L5: > Generate a production-ready, best-practice Claude Code **harness** -- fully tailored to your use case, in minutes,
> L7: A *harness* is a complete Claude Code setup for a project: `CLAUDE.md` + rules + specialized agents + slash-command 
> L46: - Claude Code CLI

## 星数曲线

```mermaid
xychart-beta
    title "Popschlock/Claude-Harness-Generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `678966e01cb4` · [字段定义](../../DATASET.md)*
