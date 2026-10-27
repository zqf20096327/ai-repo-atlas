# kyegomez/WhiteRock

⭐ 44 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/WhiteRock) · 个人维护

**自动化 VC 投资流程的多 agent 系统：触达、尽调、决策、监控**

WhiteRock 是一个以 Python 包（pip3 install whiterock）形式提供的自动化风险投资系统。流程包括：通过 Bland.ai 的对话 AI 自主联系创始人并访谈收集数据；Analyst Agent 用机器学习模型基于历史投资数据评估；Investor Agent 评估风险并给出投资建议；投后持续监控组合公司。构建于其自有 Swarms Framework 与 Bland.ai API 之上，运行需配置 BLAND_API_KEY 与 OPENAI_API_KEY。README 为黑客松项目自述，'fully autonomous' 为主张性表述，未附实盘运营证据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自主外联创始人并访谈收集创业公司数据（Bland.ai 对话 AI）
- Analyst / Investor 多 agent 分工完成评估与投资建议
- 基于自研 Swarms Framework 的模块化架构
- 投后持续监控组合公司表现

## 适用场景

- 自动化早期项目触达与初步尽调访谈
- 用多 agent 流程生成投资评估与建议
- 持续跟踪被投公司表现获取建议

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L29: 1. **Initial Outreach**: The system autonomously reaches out to founders and fundraisers through various channels. 
> L31: 3. **Analysis and Evaluation**: The collected data is then passed to the Analyst Agent, which performs a detailed e
> L37: WhiteRock was built using a combination of **Bland.ai API** and our proprietary **Swarms Framework**. Here’s a brea

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/WhiteRock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `650ea9f1ed85` · [字段定义](../../DATASET.md)*
