# huaxialucaicaizi/ai-startup-skills

⭐ 286 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/huaxialucaicaizi/ai-startup-skills) · 个人维护 · 中文 README

**一人公司做 AI 产品的 7 步 Agent Skill 合集：验证到注册**

将 7 个独立 Agent Skill（MVP 验证、商业计划书、政策导航、路演教练、获客增长、定价成交、注册合规）打包进一个仓库，外加按创业阶段路由的总入口 skill：用户说明所处阶段后由总入口调用对应子 skill，且上一步产出（验证证据、BP）可衔接下一步。安装方式为 git clone 后复制到 Codex（~/.agents/skills）或 Claude Code（~/.claude/skills）技能目录，其他支持 Agent Skills 的工具（如 Cursor）亦可。政策与合规内容主要针对中国大陆，子 skill 内容由 scripts/sync.sh 从独立仓库同步。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 步 skill 加总入口路由：按创业阶段自动选择子 skill
- 一次安装 7 个 skill，sync.sh 一键同步上游独立仓库
- 政策、法规引用附官方原文链接，声明不替代法律/税务意见
- 同时提供 Codex 与 Claude Code 技能目录安装命令

## 适用场景

- 一个人做 AI 产品时按步骤完成从验证到注册的流程
- 让 agent 根据我目前的进度建议下一步做什么
- 查找可申请的政策补贴、算力券并准备申请材料

## 场景标签

 · 领域:创业工具/Agent 技能包

## 证据(README 行号)

> L19: 「一人公司工具包」的合集仓库：把 7 个独立的 Agent Skill 打包在一起，再加一个**总入口 skill**。你只要说清楚在做什么、做到哪一步，它会判断你处在创业的哪个阶段，然后调用对应的子 skill。
> L116: ├── SKILL.md                 # 总入口：按阶段路由到子 skill

## 星数曲线

```mermaid
xychart-beta
    title "huaxialucaicaizi/ai-startup-skills 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-27"]
    y-axis "stars" 285 --> 287
    line [286, 286]
```

2026-10-26 286 → 2026-10-27 286（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ee4556c39fc7` · [字段定义](../../DATASET.md)*
