# Harshit-J004/toolguard

⭐ 15 · Python · MIT · 推送 2026-05-04 · [GitHub](https://github.com/Harshit-J004/toolguard) · [官网](https://pypi.org/project/py-toolguard/) · 个人维护

**AI agent 工具链的安全拦截与可靠性测试框架**

面向开发者的 Python 库与 CLI：对 AI agent 的工具调用层（Layer 2）做确定性模糊测试与安全防护。通过 @create_tool 装饰器读取类型提示生成 Pydantic schema，注入空值、类型错配、超大 payload 等破坏性数据测试工具链，输出可靠性报告；不调用 LLM，测试确定且无 API 费用。另提供 7 层 MCP 安全拦截瀑布（策略、风险分级人工审批、注入扫描、限流、语义校验、schema 漂移阻断、DAG 追踪）、实时 Web 仪表盘与 CI/CD 集成。限制：不测试模型智能/回答质量（Layer 1）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性 fuzzer 测试工具链，不依赖 LLM 调用
- 7 层 MCP 安全拦截：策略/风险分级/注入防御/限流/语义校验/schema 漂移/DAG 追踪
- 4 级风险分层，Tier 2 以上需人工审批，支持 Slack/Discord/Teams webhook 审批
- 实时 SSE Web 仪表盘与 CI/CD 漂移检查（toolguard drift check --fail-on-drift）

## 适用场景

- 在 CI/CD 中对 agent 工具链做可靠性回归测试
- 生产环境拦截提示注入、危险工具调用与 schema 漂移
- 对破坏性工具设置人工审批流程

## 场景标签

`网络安全` `模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L42: **ToolGuard does not test Layer 1.** We do not care if your AI is "smart" or makes good decisions. That is what eva
> L44: **ToolGuard mathematically proves Layer 2.** We solve the problem of agents crashing at 3 AM because the LLM halluc
> L52: toolguard run my_agent.py

## 星数曲线

```mermaid
xychart-beta
    title "Harshit-J004/toolguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d5124183a367` · [字段定义](../../DATASET.md)*
