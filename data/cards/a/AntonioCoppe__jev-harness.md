# AntonioCoppe/jev-harness

⭐ 15 · TypeScript · MIT · 推送 2026-09-25 · [GitHub](https://github.com/AntonioCoppe/jev-harness) · [官网](https://github.com/AntonioCoppe/jev-harness) · 个人维护

**把 TypeSafe Jev 决策输出转为可上线动作的 TypeScript 库**

封装 TypeSafe Jev 决策 API 的 TypeScript 库：Jev 返回带置信度的结构化决策（choice/score/noul），本库在其外层补上策略映射、置信度门控、影子模式、可复用 recipes 与离线评测 CLI。开发者可将低置信度决策路由为人工复核或拦截而不直接执行。后端可替换：支持通过 TYPESAFE_BASE_URL 指向自托管 /v1/systemone 服务，或传入自定义 DecisionBackend 与进程内规则。需 Node 20+ 与 TypeSafe API key，非 TypeSafe 官方产品。

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

- 策略映射 + 置信度门控 + 影子模式（不改变线上行为的日志回放）
- recipes 覆盖告警门控、NL 行过滤、多 agent 通信、下单风控等决策模式
- 离线评测 CLI：基于 fixtures 断言动作而非自由文本
- 可替换后端：自托管 systemone 服务或自定义 DecisionBackend

## 适用场景

- 把 LLM 决策接入生产流程前加置信度门控与人工复核路径
- 用影子模式验证策略改动的实际效果再上线
- 对决策策略做离线 fixture 回归测试

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: Jev returns structured decisions (`choice` / `score` / `noul`) with confidence scores. This harness adds the missing
> L63: The harness talks to anything that implements `DecisionBackend` (`systemOne({ state, questions, model })` → `{ mode

## 星数曲线

```mermaid
xychart-beta
    title "AntonioCoppe/jev-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2a8927f52534` · [字段定义](../../DATASET.md)*
