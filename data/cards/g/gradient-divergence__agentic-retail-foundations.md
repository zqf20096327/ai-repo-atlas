# gradient-divergence/agentic-retail-foundations

⭐ 26 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/gradient-divergence/agentic-retail-foundations) · [官网](https://www.amazon.com/dp/1069422649) · 个人维护

**《Foundations of Agentic AI for Retail》第三版配套可运行代码**

Fatih Nayebi 所著《Foundations of Agentic AI for Retail》（第三版，2026 年 10 月）的配套代码库：书中所有可运行清单均出自本仓库，覆盖 14 章，包括 agent 架构（RAOM/BDI/OODA）、决策框架（贝叶斯、MDP、RL）、多 agent 协调协议（Contract Net、拍卖、MCP/ACP/AP2）、护栏与评测（evals/、redteam/）及端到端 demo，每个修复配有回归测试，全套 1,029 个测试。环境锁定 Python 3.13 与 uv.lock，通过 uv sync --frozen 安装，可选 extras 覆盖流式、GNN、监控、云等栈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 书中全部可运行清单来自本仓库，逐章对应 demos 与 agents 文件
- 113 个测试文件、1,029 个测试全部通过，每处修复配有回归测试
- 覆盖 RAOM、BDI/OODA、多 agent 协议、评测与红队场景包
- 可选 extras：streaming(Redis/Kafka)、gnn、monitoring(Prometheus)、cloud 等

## 适用场景

- 按章节运行书中示例学习零售 AI agent 设计
- 参考多 agent 协调与评测护栏的实现代码
- 以回归测试核对书中清单的行为

## 场景标签

`多智能体` `模型评测` `强化学习` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Foundations of Agentic AI for Retail: Companion Code (Third Edition)
> L3: The runnable companion to *Foundations of Agentic AI for Retail*, Third Edition. Agent architectures, decision frame
> L5:  Foundations of Agentic AI for Retail: Designing, Building, and Operating Retail AI Agents, from First Principles to

## 星数曲线

```mermaid
xychart-beta
    title "gradient-divergence/agentic-retail-foundations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e523f41a2526` · [字段定义](../../DATASET.md)*
