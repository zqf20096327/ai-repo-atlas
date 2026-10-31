# lowenbjer/claude-terse

⭐ 52 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/lowenbjer/claude-terse) · [官网](https://github.com/lowenbjer/claude-terse#readme) · 个人维护

**让 Claude Code 回复简短直白的输出风格插件**

面向 Claude Code 用户的插件，用于改变 Claude 的回复文风：通过 22 条写作规则和 18 组改写示例（877 词）作为 output style 注入主 agent 系统提示，并用 SubagentStart 钩子将同样规则传给子 agent；UserPromptSubmit 钩子每轮追加 576 字符的精简提醒（约每轮 145 输入 token）以对抗长对话后规则失效。附带状态栏上下文计量器，阈值参考三份上下文退化研究。README 给出在 12 个公开提示上的字数/token/文风违规测量表。安装走 Claude 目录或 GitHub 插件市场命令。限制：仅适用于 Claude Code，规则针对英文文风问题。

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

- 22 条写作规则 + 18 组改写示例构成 output style，随插件启用生效
- UserPromptSubmit 钩子每轮注入 576 字符精简提醒，对抗长上下文下规则失效
- 状态栏上下文计量器，阈值参考 Chroma/NoLiMa/Lost in the Middle 三项研究
- README 附 12 个提示上的字数、token 与文风违规测量表

## 适用场景

- 嫌 Claude Code 回复过长、想让它直接给答案的开发者
- 降低输出 token 成本同时保持信息量
- 在状态栏监控上下文占用百分比

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L19: A Claude Code plugin that cuts reply length in half and removes mannered prose. **Fable 5.1: 46% fewer words, 51% l
> L65: The rules are a reply shape, 22 rules and 18 before/after pairs, 877 words. The shape: one sentence with the answer
> L67: The rules ship as an output style. It applies while the plugin is enabled and is part of the main agent's system pr

## 星数曲线

```mermaid
xychart-beta
    title "lowenbjer/claude-terse 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-31 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `12cb5ac5a7bb` · [字段定义](../../DATASET.md)*
