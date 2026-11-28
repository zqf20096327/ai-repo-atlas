# Liquicent/liquicent-decisiontrace

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/Liquicent/liquicent-decisiontrace) · [官网](https://liquicent.github.io/liquicent-decisiontrace/) · 组织维护

**为 AI agent 决策提供本地防篡改追溯记录的工具**

以 Python 包形式提供的决策审计层：通过 Claude Code hook、MCP 适配器、SDK 包装（dt.wrap）与 OpenTelemetry span 摄取，在决策发生时记录上下文、策略判定、例外审批、被否决的备选项、人工路径与结果，写入本地 SQLite 的 append-only、带哈希链的防篡改存储；事后可用 dt why/dt log/dt similar/dt verify 回溯与校验。定位为记录器而非网关或策略执行器，不存储模型推理内容，默认脱敏。0.1.0 alpha，Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- dt why 按记录 ID/文件/commit 回溯单条决策的完整凭据
- append-only 哈希链存储，dt verify 重算校验链
- 多入口接入：Claude Code hooks、MCP、SDK 包装、OpenTelemetry GenAI span 摄取
- 本地 SQLite 存储，无账号、无服务器、无遥测，写入前脱敏

## 适用场景

- 审计 agent 在额度/政策约束下做出退款等决策的依据
- 事后追问某次自动化决策通过了哪些规则、谁批的例外
- 团队共享服务器上集中回溯成员的 agent 决策记录

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L64: |Anthropic or OpenAI SDK|`client = dt.wrap(client)`|docs/adapters/sdk.md|
> L90: - **On top of your tools, not in front of them.** No gateway, no proxy. Hooks, spans and SDK
> L98: Not a gateway or policy enforcer (your code and your tools enforce; DecisionTrace records),


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `969ca4da40d9` · [字段定义](../../DATASET.md)*
