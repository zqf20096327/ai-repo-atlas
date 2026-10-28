# emmazangAI/mindwiki-skills

⭐ 20 · 推送 2026-05-29 · [GitHub](https://github.com/emmazangAI/mindwiki-skills) · 个人维护 · 中文 README

**10 位专家思维模型封装的 Agent Skills 决策追问包**

面向 Claude Code / CodeBuddy 等 agent 框架的技能集合：将张小龙、乔布斯、芒格等 10 位人物的心智模型与决策启发式封装为 SKILL.md 格式的 agent skills，通过 cp 命令安装到 skills 目录。每个 skill 可调用 WebSearch 搜索真实数据、读写用户文件并记录决策日志，配有 test-prompts.json 做方向一致性、诚实边界与专家分歧测试，兼容 darwin-skill 的棘轮机制。提供在线体验站点。

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

- 10 位专家共 51 个心智模型，支持多专家冲突对撞式追问
- 每个 skill 可调用 WebSearch、读写文件并写入决策日志
- test-prompts.json 自我验证（方向/不确定性/冲突三类测试）
- 兼容 darwin-skill 棘轮机制，保留改进自动回滚退步

## 适用场景

- 在做产品或投资决策时获得多视角的深度追问
- 用特定专家的框架审视自己的 PRD 或功能列表
- 记录决策日志并事后回顾判断对错

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 10位顶级专家的思维操作系统，封装为可运行的 Agent Skills。
> L28: cp SKILL.md ~/.claude/skills/mindwiki/SKILL.md

## 星数曲线

```mermaid
xychart-beta
    title "emmazangAI/mindwiki-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2edd76d7b6a2` · [字段定义](../../DATASET.md)*
