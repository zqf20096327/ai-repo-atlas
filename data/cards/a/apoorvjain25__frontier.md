# apoorvjain25/frontier

⭐ 79 · JavaScript · MIT · 推送 2026-07-04 · [GitHub](https://github.com/apoorvjain25/frontier) · 个人维护

**让主流 LLM 按 21 条书面工艺标准产出高质量作品的技能包**

面向 Claude Code 及其他 chat/API 表面的提示工程工具包：将 21 个领域（设计、写作、代码、数据等）的工艺标准文件、评审代理与流程打包为 Claude Code 插件/技能，通过 rubric 生成、best-of-N 候选、fresh-eyes 评审与 taste gate 收敛循环提升输出质量；也可仅粘贴 PROMPT.md 在单次回复内完成 quick 模式。作者声称标准由 Claude Fable 5 编写并审计。输出为带位置与 rubric 行号的可解析 findings；结果非确定性，full 模式 token 消耗约为单次的 5-9 倍（作者估计）。

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

- 21 个领域工艺标准文件，各含 34-59 条可检验规则与禁用清单
- quick/full/gate 三种模式，单次回复或最多 8 轮收敛循环
- fresh-eyes 评审与 taste gate 输出固定格式的可解析 findings
- DISTILL 机制：将品味判定转为持久规则以逐步改进

## 适用场景

- 让已有模型按书面标准完成页面、文案、代码等交付物
- 对已有作品跑 gate 模式做单轮品味评审
- 在 Claude Code 中以插件形式使用技能与评审代理

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L39: Method can be written down. frontier is that method, packaged: one command that runs any
> L158: **Claude Code, as a plugin** (skills + the two judge agents):
> L171: **Cursor, Windsurf, aider, raw API**: paste PROMPT.md, attach the craft file

## 星数曲线

```mermaid
xychart-beta
    title "apoorvjain25/frontier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-26 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `840a0bcbb21d` · [字段定义](../../DATASET.md)*
