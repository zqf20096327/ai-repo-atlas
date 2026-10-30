# hpbyte/rocky

⭐ 18 · Python · 推送 2026-04-13 · [GitHub](https://github.com/hpbyte/rocky) · 个人维护

**让 agent 用《挽救计划》Rocky 语气回复的技能插件**

面向 Claude Code 与 Codex 的 agent 技能/插件：触发后使 agent 以小说《挽救计划》中 Rocky 的风格回复——紧凑、字面化、偏实用。技能声明在保留代码、命令与标识符的技术精确性的同时压缩措辞，并在高风险或高精度场景回退到常规清晰表达。README 给出基于 10 个开发提示词的 token 基准：Rocky 风格均值较简洁对照组节省 47%。通过 Claude Code 插件市场或 Codex 插件搜索安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Rocky 风格回复：紧凑、字面化、保留技术精确性
- 高风险/高精度场景自动回退常规清晰表达
- 基准显示 token 输出较简洁对照均值减少 47%
- 支持 Claude Code 插件市场与 Codex 两种安装途径

## 适用场景

- 给 Claude Code / Codex 的回复换上 Rocky 风格
- 在保持代码与命令准确性的前提下减少输出 token
- 按需用 /rocky 触发、normal mode 退出风格

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: An agent skill/plugin that makes agents talk like **Rocky** from Project Hail Mary by Andy Weir.
> L38: |**Claude Code**|`/plugin marketplace add hpbyte/rocky` then `/plugin install rocky`|

## 星数曲线

```mermaid
xychart-beta
    title "hpbyte/rocky 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `db5297f59d3c` · [字段定义](../../DATASET.md)*
