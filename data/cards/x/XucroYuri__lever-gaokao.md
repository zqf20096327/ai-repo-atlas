# XucroYuri/lever-gaokao

⭐ 12 · Python · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/XucroYuri/lever-gaokao) · 个人维护 · 中文 README

**面向高考考生和家长的志愿填报 Agent 方法论与技能包**

以 Agent 技能（SKILL.md + references 文档）形式发布的志愿填报辅助项目：先问诊家庭与分数情况，再整理候选学校与专业，通过第一性原理和对抗式审查输出方向建议、风险与待核验清单。附 Python 脚本做候选表格的字段与硬限制机械校验。适用于会使用 Codex/Claude Code 等 Agent 工具的用户，也支持网页聊天粘贴片段的降级用法。定位为决策辅助，不承诺录取概率。许可为 CC BY-NC-SA 与 PolyForm Noncommercial 的非商用限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 形式的 Agent 技能，含引导式问诊、候选筛选、对抗式审查流程
- 附 ledger_tool.py 脚本做候选表格字段与硬限制校验
- 支持无网络代理场景：可配 OpenAI-compatible 接口的国产模型或纯网页聊天降级使用
- 源自作者 2025 年真实志愿填报实践案例

## 适用场景

- 为中低分段考生整理候选学校与专业清单并逐层排除
- 在家长和考生之间摊开各选项的收益、风险与退路
- 用脚本校验志愿候选表格的字段与硬性限制

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L13: `Lever-GaoKao` 是一个**AI Agent高考志愿填报辅助项目**。
> L18: - 最后用第一性原理和对抗式审查，把每个选择的好处、风险、被误杀的机会和还要核验的资料说清楚。
> L74: 请使用 $lever-gaokao，先问清资料，再为一名中国高考考生生成有依据、讲风险、兼顾长期机会的志愿填报建议。

## 星数曲线

```mermaid
xychart-beta
    title "XucroYuri/lever-gaokao 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-11-08", "2026-11-21"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-10-19 11 → 2026-11-21 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `0c934e61bbf6` · [字段定义](../../DATASET.md)*
