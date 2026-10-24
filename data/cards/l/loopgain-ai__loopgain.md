# loopgain-ai/loopgain

⭐ 126 · Python · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/loopgain-ai/loopgain) · [官网](https://loopgain.ai) · 组织维护

**AI agent 循环的成本控制器：实时判定收敛并回滚**

纯 Python 库（无运行时依赖，Python 3.10+），用控制理论方法（Barkhausen 判据与多特征轨迹分类器）替代 max_iterations 固定上限：每轮读取一个非负误差信号，将轨迹分类为 FAST_CONVERGE/CONVERGING/STALLING/OSCILLATING/DIVERGING 五种状态，据此决定继续、停止或回滚到缓冲中误差最低的历史输出。面向任意具有可测量误差信号的迭代式 AI 工作流（验证-修订、RAG 自纠、代码生成+linter 等），提供 LangGraph、CrewAI、AutoGen、LangChain、OpenAI Agents SDK、Claude Agent SDK 适配器，另含 Claude Code 插件与可自托管遥测仪表盘。README 明确列出限制：只检测收敛不检测正确性，停止质量受误差信号/验证器质量约束。

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

- 五状态轨迹分类器（基于累积降幅、OLS 斜率与 t 检验）决策停止/继续/中止
- 终止时返回缓冲中误差最低的历史输出而非末轮输出
- 六种框架预置适配器：LangGraph/CrewAI/AutoGen/LangChain/OpenAI Agents/Claude Agent SDK
- 纯 Python 无运行时依赖，公开 2,000 次配对试验的可复现基准

## 适用场景

- 我跑 agentic coding 循环时按失败测试数自动判断何时停，省 token
- 我的 RAG 自纠循环在震荡或发散时回滚到此前质量更优的输出
- 团队通过自托管仪表盘查看全队循环的稳定性、成本与回滚情况

## 场景标签

`Agent 框架` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L5: AI agent loops waste time and money when they don't know when to stop. LoopGain measures the loop in real time and s
> L23: Works for **any iterative AI workflow with a measurable error signal** — verify-revise loops, refinement passes, to

## 星数曲线

```mermaid
xychart-beta
    title "loopgain-ai/loopgain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-24 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b2a1d1ddeb3e` · [字段定义](../../DATASET.md)*
