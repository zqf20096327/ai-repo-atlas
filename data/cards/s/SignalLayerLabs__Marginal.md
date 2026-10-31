# SignalLayerLabs/Marginal

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/SignalLayerLabs/Marginal) · [官网](https://signallayerlabs.github.io/Marginal/) · 组织维护

**AI 编码 agent 的运行时治理器：检测并拦截无进展的重复操作**

面向 AI 编码 agent（Codex、Claude Code、OpenCode、PrivacyCode）的开源运行时治理工具：本地观测 agent 动作，识别“同一成功动作＋可观测状态不变＋无新证据”的无进展重复。新集成默认以 Shadow Mode 仅观测，拦截权限需凭仓库本地证据逐级晋升（观察→验证→挣得→窄干预→恢复），状态或证据变化即降级并放行。Codex 集成提供 Tool Enforcement（仅限带路径参数的局部 Read 类动作），其余引擎为 observe-only。以 Python 包与 Codex 插件形式分发，账本哈希链与本地密钥伪onym化保障隐私与完整性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Shadow Mode 先观测，拦截权限需本地证据晋升且可降级
- Codex 原生插件提供窄范围 Tool Enforcement，其余引擎 observe-only
- v3 治理账本以哈希链链接记录，私有数据不进入证据字段
- 提供 Python 库（BudgetLimits/Treasury/build_policy）与 status/doctor/explain CLI

## 适用场景

- 治理编码 agent 反复读文件等无进展动作
- 审计 agent 动作与治理决策的可追溯记录
- 在不放行私有数据的前提下共享聚合统计（Commons）

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: **Open-source runtime governor for AI coding agents.** MARGINAL observes agent work, detects proven no-progress repe
> L111: |Engine|Capability|Current behavior|

## 星数曲线

```mermaid
xychart-beta
    title "SignalLayerLabs/Marginal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7ffd9fa8303f` · [字段定义](../../DATASET.md)*
