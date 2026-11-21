# xmohamedtariq/AquaMindAI-Agent

⭐ 3 · Python · MIT · 推送 2026-11-11 · [GitHub](https://github.com/xmohamedtariq/AquaMindAI-Agent) · [官网](https://aquamindai-agent.onrender.com/) · 个人维护

**反渗透海水淡化运维的自主诊断决策支持 Agent**

面向反渗透海水淡化系统的自主工程决策支持 Agent：读取水厂 CSV 数据后按 Plan→Act→Observe→Reflect→Decide 流程执行校验、KPI 计算、异常检测、MCP 知识检索、SQLite 事故记忆搜索，生成有据可查的诊断假设与验证建议。安全上采用三级权限模型与注入防御，物理控制操作被排除在自主执行边界外；Gemini 仅为已批准动作提供推理摘要，不可用时回退确定性规划器，并输出 JSONL 审计轨迹与成本跟踪。

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

- 七个受约束的运维工具构成自主调查闭环
- Gemini 混合规划：确定性规划器选动作，Gemini 提供摘要，不可用时回退
- MCP 官方 SDK 实现 server/client 知识检索，SQLite 持久事故记忆
- 三级权限模型、注入防御与 JSONL 审计轨迹

## 适用场景

- 对反渗透水厂传感器数据做质量校验与 KPI 分析
- 排查运行异常并生成有出处的诊断报告
- 检索经过审批的工程知识与历史事故记录

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L23: **AquaMindAI-Agent** is an autonomous engineering decision-support agent designed to investigate operational proble
> L31: Given RO plant CSV data, the agent can:
> L69: AquaMind integrates **Google Gemini** inside the agent runtime through a hybrid planning layer.

## 星数曲线

```mermaid
xychart-beta
    title "xmohamedtariq/AquaMindAI-Agent 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `26dd7ea2b299` · [字段定义](../../DATASET.md)*
