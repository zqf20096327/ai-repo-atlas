# vishal-dehurdle/state-harness

⭐ 18 · Python · NOASSERTION · 推送 2026-08-15 · [GitHub](https://github.com/vishal-dehurdle/state-harness) · [官网](https://vishalvermalabs.com/papers/empirical-lyapunov-stability-agent-failure) · 个人维护

**LLM agent 运行时安全监控库：检测 token 失控并诊断失败原因**

面向多轮 LLM agent 的运行时监控库，用 Lyapunov 稳定性能量函数监测 token 消耗相对 warmup 基线的增长比，连续 W 步超阈值即触发熔断，并将失败分类为上下文螺旋、重试风暴、策略漂移等模式并给出修复建议，全程无需额外 LLM 调用。Rust 实现核心（PyO3），提供 Python SDK、装饰器、CLI 及 LangGraph/CrewAI 适配器，可导出 OpenTelemetry 属性。作者自述不提升任务成功率，价值在失败诊断与长循环搜索树的算力节省；不适用于聊天、RAG 或少于 10 轮的 ReAct 循环。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Lyapunov 能量监测触发熔断（约 1μs/步），无额外 LLM 调用
- 失败模式分类：Context Spiral/Retry Storm/Policy Drift/Early Explosion/Budget Exhaustion
- 提供 LangGraph/CrewAI/裸 Python 适配器与 CLI 模拟命令
- SWE-bench 上报告 38.6% 搜索节点减少与 30% 墙钟时间缩短（3,175 次运行验证）

## 适用场景

- 多 agent 生产系统提前终止注定失败的长循环任务
- 搜索树 agent（MCTS/beam search）控制树级成本爆炸
- 平台团队在边缘做失败分类并导出 OpenTelemetry 告警

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L10: Lyapunov-stability monitor for multi-turn LLM agents. Detects token spirals, classifies failure patterns, and tells
> L30: State-harness monitors token consumption relative to a warmup baseline via a Lyapunov energy function. When the gro
> L201: Three mechanisms, implemented in Rust (via PyO3):

## 星数曲线

```mermaid
xychart-beta
    title "vishal-dehurdle/state-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6366fe0df038` · [字段定义](../../DATASET.md)*
