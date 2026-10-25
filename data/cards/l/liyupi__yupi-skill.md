# liyupi/yupi-skill

⭐ 452 · MIT · 推送 2026-04-09 · [GitHub](https://github.com/liyupi/yupi-skill) · [官网](https://www.codefather.cn) · 个人维护 · 中文 README

**把博主程序员鱼皮蒸馏成 AI 技能包，供编程求职咨询**

由程序员鱼皮（@liyupi）发布的 Agent Skill：将其思维方式（7 个心智模型、决策规则）与表达风格（结论先行、自嘲式幽默等）打包成遵循 AgentSkills 开放标准的技能文件，通过 git clone 安装到 Claude Code、Cursor 或 OpenClaw 后，AI 以其风格回答编程学习、求职面试、技术选型、创业经验等问题，并按内置信息源列表联网搜索。README 声明素材截至 2026 年 4 月，技术深度问题先搜索再回答。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md + references 结构，遵循 AgentSkills 开放标准，渐进式加载
- 内置 7 个心智模型与决策规则、表达风格模板
- 内置 codefather.cn、mianshiya.com 等指定信息源与联网搜索规则
- 支持 Claude Code / Cursor / OpenClaw 三种环境安装

## 适用场景

- 编程学习路线与求职 offer 决策咨询，获得个人风格的直接建议
- 简历优化与面试准备问答
- 参考其流程制作自己的个人风格 Agent Skill

## 场景标签

`AI 助手` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L134: ├── SKILL.md                          # 入口：触发条件、工作流、回答模式
> L141: 遵循 AgentSkills 开放标准，渐进式加载：AI 先读元数据判断是否触发 → 触发后读 SKILL.md → 按需加载 references。

## 星数曲线

```mermaid
xychart-beta
    title "liyupi/yupi-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 450 --> 453
    line [451, 452, 452]
```

2026-10-18 451 → 2026-10-25 452（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `abab4e4af4d7` · [字段定义](../../DATASET.md)*
