# footprintjs/footPrint

⭐ 21 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/footprintjs/footPrint) · [官网](https://footprintjs.github.io/footprint-demo/) · 组织维护

**给后端开发者的流程图式执行取证库：记录决策与依赖证据**

以"流程图模式"组织后端逻辑：将工作流写成命名阶段、受跟踪状态与显式决策，执行时捕获数据活动、执行路径与决策评估的连接证据，供人类与 AI agent 事后调查。证据在执行中捕获而非由 LLM 事后重构，运行时无需模型。记录器属于执行引擎 footprintjs，查询与回放属于 foottrace。提供依赖查询、控制依赖记录、重试对账节点、attempt 指标及 OTel 导出。要求 Node.js 22+。README 另列明记录无法证明正确性、完整性或合规性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 执行中捕获数据/控制依赖与决策评估证据，无需运行时 LLM
- 两个包分工：footprintjs 执行流程图，foottrace 负责回放/时间旅行/依赖查询
- addRetryLoop 将重试与对账放入普通节点
- attempts() 指标与 toOTel() 导出（不发送数据）

## 适用场景

- 调查后端工作流中错误结果的产生路径
- 为编码 agent 提供带证据的执行记录切片用于调试
- 在 agent 运行时中追溯工具活动与决策依据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L17: FootPrint is the **flowchart pattern for inspectable workflows**. Write your logic as named stages, tracked state, 
> L19: **The evidence is captured during execution—not reconstructed by an LLM afterward.** People and AI agents can inves
> L33: FootPrint records tracked data activity and evaluated decision evidence as the flow executes. Its control-dependenc

## 星数曲线

```mermaid
xychart-beta
    title "footprintjs/footPrint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0350d33e566e` · [字段定义](../../DATASET.md)*
