# Future-House/ldp

⭐ 139 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Future-House/ldp) · [官网](https://edisonscientific.gitbook.io/edison-cookbook/ldp-language-decision-processes) · 组织维护

**语言智能体模块化框架：可互换组合智能体、环境与优化器**

Future-House 维护的 Python 框架，将语言智能体交互形式化为语言决策过程（LDP，即动作与观测均为自然语言的 POMDP），提供 Agent 抽象（init_state/get_asv 接口）、随机计算图（SCG）支持对智能体参数含 LLM 权重求梯度，用于微调与强化学习训练。配合姊妹库 Aviary 定义语言智能体环境（含 GSM8K 教程）。面向做语言智能体研究与训练的开发者/科研人员。

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

- LDP 形式化：动作与观测为自然语言的 POMDP
- Agent 抽象支持工具调用、记忆与状态管理
- 随机计算图（SCG）可对智能体参数（含 LLM 权重）求梯度
- 与 Aviary 环境库配合，提供 GSM8K 教程

## 适用场景

- 构建和运行语言智能体完成环境任务
- 对语言智能体做微调或强化学习训练
- 研究语言决策过程的形式化与实验

## 场景标签

`Agent 框架` `强化学习` `微调` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L17: **LDP** [^1] is a framework for enabling modular interchange of language agents, environments, and optimizers.
> L139: For more advanced use-cases, LDP features a stochastic computation graph [^2]

## 星数曲线

```mermaid
xychart-beta
    title "Future-House/ldp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 137 --> 140
    line [138, 139, 139]
```

2026-10-18 138 → 2026-10-28 139（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b212538d28fd` · [字段定义](../../DATASET.md)*
