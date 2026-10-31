# marcopatzelt/brunnfeld-agentic-world

⭐ 139 · TypeScript · MIT · 推送 2026-04-06 · [GitHub](https://github.com/marcopatzelt/brunnfeld-agentic-world) · 个人维护

**中世纪村庄经济模拟：最多 1000 个 LLM 智能体自主生产与交易**

Node.js/TypeScript 实现的 LLM 多智能体经济模拟引擎：22 个地点的村庄中，最多 1000 个智能体在饥饿、工具损耗、供应链（小麦→面粉→面包）、实时订单簿、季节产量与债务等引擎约束下生存与交易，不接收任何行为指令。每模拟小时执行一次 tick，引擎构建感知、调用 LLM、解析动作；支持村庄议会立法、持久化 markdown 记忆、多村庄世界生成。可通过 OpenRouter 接入模型或留空使用 Claude CLI，另有 3-8 次工具调用的 Harness 模式。git clone 源码 npm 安装运行，带 Web 查看器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 最多 1000 个智能体、5 个村庄的多智能体经济模拟
- 硬供应链与实时订单簿、价格指数、工具损耗、腐败与债务等经济机制
- 引擎/LLM 分离架构：确定性引擎解析动作，LLM 仅做决策
- Harness 模式提供每 tick 3-8 次工具调用与轮转交互

## 适用场景

- 研究 LLM 智能体在资源约束下的涌现经济行为
- 运行多村庄规模化的生成式社会模拟实验
- 观察供应链断裂、治理投票等机制对智能体行为的影响

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L14: Up to 1000 LLM agents live in a 22-location village. They receive no behavioral instructions, no trading strategies
> L127: 11. **Decision phase** — group by location, run LLM calls (solo / multi-agent rounds)

## 星数曲线

```mermaid
xychart-beta
    title "marcopatzelt/brunnfeld-agentic-world 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-31 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5fd5f97e482c` · [字段定义](../../DATASET.md)*
