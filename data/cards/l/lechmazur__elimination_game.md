# lechmazur/elimination_game

⭐ 298 · 推送 2026-01-07 · [GitHub](https://github.com/lechmazur/elimination_game) · 个人维护

**多智能体淘汰赛式 LLM 社交推理/策略/欺骗评测基准**

让 8 个 LLM 进行多轮淘汰锦标赛：公开发言、偏好排序配对、三轮私聊结盟、匿名投票淘汰，直至剩两人，由被淘汰者组成陪审团投票定胜。基于多局排名用 TrueSkill 计分，并提供排名分布、背叛率（加害/受害双视角）、冠军次数、最早出局、决赛胜率、发言字数等可视化指标；另测仅公开发言版本。README 附 61 个模型的 TrueSkill 排行榜与逐轮回放动画、日志摘录。供研究者在社交推理与欺骗维度比较模型。

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

- 公开/私聊双层对话 + 匿名投票淘汰的 8 模型锦标赛机制
- TrueSkill 评分聚合多局随机对局结果
- 背叛率、排名分布、决赛说服力等多维分析图表
- 61 个模型的 TrueSkill 排行榜与逐轮回放动画

## 适用场景

- 比较各 LLM 在结盟、欺骗与说服场景下的表现
- 研究模型共享知识与隐藏意图的处理差异
- 查看模型在博弈中的涌现对话行为样本

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: The **Elimination Game** is a multi-player tournament that tests LLMs in social reasoning, strategy, and deception. 
> L87: ### **Scoring & TrueSkill**

## 星数曲线

```mermaid
xychart-beta
    title "lechmazur/elimination_game 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 297 --> 299
    line [298, 298]
```

2026-10-18 298 → 2026-10-25 298（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4abee1d16d9a` · [字段定义](../../DATASET.md)*
