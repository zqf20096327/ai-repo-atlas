# AskRoundtable/expert-skills

⭐ 55 · MIT · 推送 2026-04-09 · [GitHub](https://github.com/AskRoundtable/expert-skills) · 组织维护 · 中文 README

**给 Claude 类工具加载专家思维模型（Munger/Feynman 等）的技能模块集**

由 5 个专家模块（Munger、Naval、Feynman、Kahneman、Graham）组成的 SKILL.md 技能集合，通过 npx openskills 安装到 Claude Code、Cursor、Windsurf 等兼容工具。每模块编码专家的思维模式、心智模型、线索敏感点与盲点，由基于 Gary Klein 认知决策模型的 6 步认知引擎驱动。README 给出各专家相对基线 Claude 的 4 维度评分提升数据（+18% 到 +83%），评测条件为 temperature=0、每专家 3 个真实案例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个专家模块各含心智模型、模式识别与盲点内容
- 基于 Recognition-Primed Decision 模型的 6 步认知引擎双层架构
- 兼容任意 SKILL.md 格式工具（Claude Code/Cursor/Windsurf）
- README 附 4 维度评分与基线 Claude 的对比数据

## 适用场景

- 让 Claude 在投资、职业、创业等决策场景应用特定专家框架
- 用第一性原理分解或认知偏差检查改进分析质量
- 为 Cursor/Windsurf 等编码助手补充决策类思维技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L21: npx openskills install https://github.com/AskRoundtable/expert-skills
> L24: Works with Claude Code, Cursor, Windsurf, or any SKILL.md-compatible tool.

## 星数曲线

```mermaid
xychart-beta
    title "AskRoundtable/expert-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-30 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d439d16cc9ba` · [字段定义](../../DATASET.md)*
