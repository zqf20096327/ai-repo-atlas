# TelivityAI/otaip

⭐ 45 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/TelivityAI/otaip) · [官网](https://telivity.app) · 组织维护

**面向旅游业的 AI agent 编排平台：覆盖机票酒店全预订生命周期**

开源旅游 AI 平台，将机票与酒店预订全流程（搜索、定价、出票、退改、BSP/ARC 结算）建模为带类型契约的 agent。提供 77 个 agent（12 个运营阶段）、6 个分销适配器（Amadeus/Sabre/Navitaire/TripPro/Duffel/HAIP，共 456 个适配器测试）。核心机制为 pipeline contract 系统：LLM 编排调用需通过 schema 校验、意图锁、置信度门控等 6 道门以防止幻觉；agent 可脱离 LLM 直接调用。TypeScript 严格模式，pnpm monorepo，Node.js >=24。

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

- 77 个 agent 覆盖预订、退改、结算等 12 个运营阶段
- 6 个 GDS/NDC/LCC 分销适配器（456 个测试）
- pipeline contract 六道门校验 LLM 编排调用
- 内化 ATPCO 运价规则、NUC/ROE 运价构建、BSP 对账等行业逻辑

## 适用场景

- 构建多供应商 OTA 搜索与出票系统
- 搭建航空 NDC+GDS 分发层或酒店预订平台
- 在旅游 AI 助手中以受控管道调用预订 agent

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: The full airline and hotel booking lifecycle — search, pricing, booking, ticketing, exchange, refund, and BSP/ARC se
> L23: - **A travel AI assistant** — AgentLoop + pipeline validator + MCP/OpenAPI tool generation
> L95: The pipeline validator enforces six gates on every LLM-orchestrated call: schema conformance, semantic validation, 

## 星数曲线

```mermaid
xychart-beta
    title "TelivityAI/otaip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3f13599c4d3e` · [字段定义](../../DATASET.md)*
