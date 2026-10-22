# zj-unicom-ai/UniEmployee

⭐ 429 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/zj-unicom-ai/UniEmployee) · 组织维护 · 中文 README

**企业数字员工构建与运行平台：把员工经验固化为可上岗 AI 员工**

面向企业的数字员工平台：通过 Employee→Workflow/SOP→Skill→Connector→Tool 五层能力模型，把大模型编排成客服、销售、数据分析、HR、经营分析、算网运营等岗位的数字员工。关键机制包括：SKILL.md 技能规程与 StateGraph 状态机工作流、HITL 人工审批中断恢复、按 (user, employee) 隔离的跨会话长期记忆、超长对话自动压缩、全链路 Trace 可回放、MCP 连接器与企业知识本体。限制：微信/企微/飞书/钉钉等外部渠道尚未随当前版本发布，需自备 OpenAI 兼容模型服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 技能规程 + StateGraph 状态机 SOP（含人工审批节点）
- HITL 审批中断恢复 + 敏感词/工具白名单/SQL 只读校验等安全护栏
- 跨会话长期记忆落盘 PostgreSQL，超长对话自动压缩（85% 窗口比例或 17 万 token 触发）
- 内置 8 个示例数字员工，覆盖售前、数据分析、HR、经营分析等岗位

## 适用场景

- 把客服、销售等岗位的流程和经验配置为可审批可观测的 AI 员工
- 企业知识本体 + RAGFlow 多源知识做带溯源的客户问答与客户 360
- cron/webhook 触发自动任务并经人工审批后发布

## 场景标签

 · 领域:企业 AI/Agent 平台

## 证据(README 行号)

> L12: UniEmployee 是一套面向企业的**数字员工构建与运行平台**：把专业员工的工作经验、业务流程和判断标准，固化为可随时上岗、可配置、可审批、可观测的 AI 数字员工。通过 **Employee → Workflow/SOP
> L18: - 📊 **数据分析与报告工作台**：小数（`xiaoshu`）拥有独立的 `/app/analyst` 工作台，支持数据库、附件表格、知识库和连接器数据源；SQL 查询采用 AST 级只读校验、表白名单、行数上限和服务端超时。分

## 星数曲线

```mermaid
xychart-beta
    title "zj-unicom-ai/UniEmployee 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 357 --> 421
    line [362, 363, 416]
```

2026-10-18 362 → 2026-10-22 416（+54）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3cdfeca9f75d` · [字段定义](../../DATASET.md)*
