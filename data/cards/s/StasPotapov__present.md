# StasPotapov/present

⭐ 16 · HTML · MIT · 推送 2026-10-25 · [GitHub](https://github.com/StasPotapov/present) · 个人维护

**Claude Code 技能：从想法到离线 HTML 演示文稿的完整流水线**

面向 Claude Code 用户的 agent 技能（skill），以 /present 命令引导四阶段流水线：Context（采访/口述/既有材料生成 slides.md）、Design（生成 design.md 并构建）、Build（生成自包含离线 HTML 幻灯片，含演讲者窗口与 PDF 导出）、Voice（转录排练录音、对比时间预算、按原话修剪并重建）。状态记录在 DECK.md，可跨会话续作。配套工具 BMAD、OpenSuperWhisper、styles.refero.design、Claude Design 均为可选；无 Claude Design 时流水线仍可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段流水线：slides.md → design.md → 离线 HTML 幻灯片 → 排练修剪循环
- 输出自包含 HTML 文件：离线可开、无 CDN 与网络引用
- Voice 阶段转录排练录音，按时间预算修剪演讲稿并展示 slides.md diff
- 进度记录在 DECK.md，跨会话从中断处继续

## 适用场景

- 让 Claude 从想法或既有材料生成定制化 HTML 演示文稿
- 通过录音排练并让 AI 按时间预算修剪讲稿
- 无需设计经验，通过对话迭代幻灯片样式与内容

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: # present — a skill for Claude Code
> L7: An agent skill that walks you from an idea to a finished **bespoke HTML presentation** (a deck): slide text, a desig
> L33: **In the skill** this is the "Context" stage. It runs all three entry points itself, no BMAD needed: an interview a

## 星数曲线

```mermaid
xychart-beta
    title "StasPotapov/present 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a61a92209e65` · [字段定义](../../DATASET.md)*
