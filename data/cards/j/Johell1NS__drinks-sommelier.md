# Johell1NS/drinks-sommelier

⭐ 15 · MIT · 推送 2026-07-07 · [GitHub](https://github.com/Johell1NS/drinks-sommelier) · 个人维护 · 中文 README

**教 AI agent 充当啤酒/葡萄酒侍酒师的技能文件**

以 SKILL.md 纯文本文件形式提供的 agent 技能：让 OpenCode、Claude Code、Cursor 等 AI agent 充当个人啤酒与葡萄酒侍酒师。机制为五阶段流程——首次引导式填写口味档案（存于可读可编辑的文本文件）、分析照片或文字中的酒品清单、对每款产品做网络检索（禁止使用预训练知识）、按口味规则与历史偏好打 0-100% 匹配指数、输出推荐与配餐。仅覆盖啤酒和葡萄酒，其他酒类被忽略；不做专业品鉴评价。通过 npx skills 或 git clone 安装，无需 API key。

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

- 五阶段流程：口味建档→输入分析→逐款联网检索→匹配评估→结构化推荐
- 口味档案持久化于可读可编辑的文本文件，跨会话保留并随反馈更新
- 0-100% 偏好指数与避选清单输出，附食物搭配建议
- SKILL.md 为纯文本，可自定义规则并转换到其他 agent 框架

## 适用场景

- 在酒架、菜单前拍照片，让 AI agent 按 my 口味推荐该买哪款
- 让 agent 记住我喜欢的啤酒和葡萄酒，长期积累口味偏好
- 没有清单时询问晚餐配酒建议，agent 会先问清情况再推荐

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L10: > **A skill for AI agents.** OpenClaw, Hermes Agent, OpenCode, Claude Code, Cursor, and beyond.
> L25: **drinks-sommelier** teaches any AI agent to act as a personal
> L74: - **Fully customizable.** SKILL.md is a text file.

## 星数曲线

```mermaid
xychart-beta
    title "Johell1NS/drinks-sommelier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e3136187e3f5` · [字段定义](../../DATASET.md)*
