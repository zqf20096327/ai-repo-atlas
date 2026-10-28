# The-Swarm-Corporation/PARL

⭐ 55 · Python · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/The-Swarm-Corporation/PARL) · [官网](https://discord.gg/EamjgSaEQf) · 组织维护

**PARL 训练范式的社区开源实现：奖励函数与并行度指标**

由 The Swarm Corporation 维护的 Parallel-Agent Reinforcement Learning 非官方开源实现，基于 Kimi K2.5 技术报告。提供三项奖励（实例化奖励、子代理完成率、任务级结果）的 staged reward shaping、延迟导向的 Critical Steps 评估指标，以及编排者-子代理架构的可微分组件，用于训练模型分解任务并并行协调最多 100 个子代理。以 pip 包 open-parl 提供，含 Hugging Face 集成示例。声明与 Kimi AI 无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三项式 PARL 奖励函数与退火调度（λ1/λ2 训练中退火至零）
- Critical Steps 延迟导向评估指标
- 可微分组件，兼容梯度优化
- 提供 Hugging Face 集成示例与测试套件

## 适用场景

- 多智能体训练中缓解串行坍缩问题
- 复现 Kimi K2.5 报告中的 PARL 训练方法
- 用延迟导向指标评估智能体并行化效果

## 场景标签

`多智能体` `强化学习` · 领域:Agent 开发

## 证据(README 行号)

> L9: Open-source implementation of **PARL (Parallel-Agent Reinforcement Learning)**, a novel training paradigm that enabl
> L34: PARL implements the three-term reward from the Kimi K2.5 technical report:
> L63: pip3 install -U open-parl

## 星数曲线

```mermaid
xychart-beta
    title "The-Swarm-Corporation/PARL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0ff39b34abd1` · [字段定义](../../DATASET.md)*
