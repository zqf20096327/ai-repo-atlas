# dshapi/AI-SPM

⭐ 17 · Python · Apache-2.0 · 推送 2026-05-17 · [GitHub](https://github.com/dshapi/AI-SPM) · 组织维护

**企业级 AI 安全态势管理（AI-SPM）平台：发现并防护 AI 资产风险**

开源的企业级 AI 安全态势管理（AI-SPM）平台 Orbyx：对 AI 模型、agent、MCP 服务器及关联资源做持续监控、发现与风险评估，识别影子 AI，检测 AI 供应链/流水线中可能导致数据外泄的风险，并围绕 AI 使用实施治理与策略控制。部署基于 Kubernetes（Kind）集群，提供管理门户（FastAPI 后端微服务 + React 前端），新机器端到端部署约 20 分钟，含 admin/admin 演示账户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发现环境中的 AI 模型、agent 及关联资源（含影子 AI）
- AI 供应链/流水线风险识别与数据外泄检测
- Admin Portal 提供库存、运行时、策略与威胁响应视图
- 基于 Kind 集群的脚本化部署，步骤幂等

## 适用场景

- 盘点组织内 AI 模型与 agent 资产及其安全状态
- 识别 AI 应用供应链中的数据外泄风险并按上下文排定优先级
- 对 AI 使用实施治理与合规策略控制

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: This opensource project dedicated to implementing Enterprise level AI-SPM. By doing so organizations can proactively
> L75:  A Real-time AI security posture across every agent, model, and data source — inventory, runtime, policies, and thr

## 星数曲线

```mermaid
xychart-beta
    title "dshapi/AI-SPM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `6eae009cfca6` · [字段定义](../../DATASET.md)*
