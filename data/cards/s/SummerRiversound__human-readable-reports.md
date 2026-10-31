# SummerRiversound/human-readable-reports

⭐ 14 · MIT · 推送 2026-10-26 · [GitHub](https://github.com/SummerRiversound/human-readable-reports) · 个人维护

**让 AI agent 写的分析报告对人类易读的 agent skill**

面向 Claude Code 等 agent 的技能包：以 14 条写作规则（读者优先、结论先行、完整句子、术语解释或删除、证据放尾注、去冗余等）约束 agent 产出的人类面向报告/分析文档，减少 AI 冗长与术语堆砌。安装后 agent 在被要求写报告时自动加载规则；提供前后对比示例与 SKILL.md 完整规则及不适用边界（如供 agent 执行的 spec/plan 不适用）。Cursor 等其他 agent 可将规则粘贴进 system prompt 使用。

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

- 14 条人类可读性写作规则（读者定位、结论先行、证据后置等）
- 以 Claude Code 插件或 git clone 到 skills 目录方式安装
- 规则与框架、语言无关，可粘贴进任意 agent 的 system prompt
- 提供 flaky CI 测试报告的前后对照示例

## 适用场景

- 团队里 coding agent 产出的报告没人读，需要让报告对人类可读
- 规范 agent 生成技术分析与文档的写作风格
- 为 Cursor 等其他 agent 复用这套写作规则

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Your coding agent writes reports that are technically correct and unreadable.** Walls of jargon, `file:line` dumps
> L54: **Claude Code** — install it as a plugin, so `/plugin update` keeps it current:
> L70: The agent loads it automatically when you ask for a report or analysis doc.

## 星数曲线

```mermaid
xychart-beta
    title "SummerRiversound/human-readable-reports 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `eb42d697591b` · [字段定义](../../DATASET.md)*
