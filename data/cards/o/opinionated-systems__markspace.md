# opinionated-systems/markspace

⭐ 19 · Python · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/opinionated-systems/markspace) · [官网](https://opinionated.systems) · 组织维护

**面向 agent 舰队的环境介导协调协议：在边界层强制安全**

基于共识迹（stigmergy）机制的多 LLM agent 协调协议：agent 不直接互发消息，而是在共享环境中留标记（marks），由环境边界处的外部 guard 层强制执行身份、作用域权限与冲突解决，约束置于 agent 无法影响的基础设施中。协议定义 5 种标记类型、3 级可见性、3 种冲突策略、信任加权衰减和 70 条形式化属性；附带 Python 参考实现用于实验验证属性，含 325 项单元测试和 525/1050 agent 规模的压力测试。面向需要多 agent 安全协调的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种标记类型（Intent/Action/Observation/Warning/Need）与信任加权衰减
- guard 层在环境边界强制身份、作用域与冲突策略，身份由基础设施提供
- 70 条形式化属性，Python 参考实现含 325 项单元测试
- 21 次实验（gpt-oss-120b 与 Mercury 2）报告零安全违规，最高 1,050 agent

## 适用场景

- 多 agent 共享资源场景中防止越权与重复预订
- 在不依赖 agent 自身合规的前提下给 agent 舰队加安全边界
- 通过 need 标记为人机决策升级提供结构化路径

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L15: Coordination guarantees should hold independent of agent behavior. Markspace is a coordination protocol for agent f
> L17: The protocol defines five mark types, three visibility levels, three conflict policies, trust-weighted decay, and 7

## 星数曲线

```mermaid
xychart-beta
    title "opinionated-systems/markspace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `59558cf9dd7b` · [字段定义](../../DATASET.md)*
