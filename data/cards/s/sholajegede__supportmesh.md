# sholajegede/supportmesh

⭐ 15 · TypeScript · 推送 2026-06-03 · [GitHub](https://github.com/sholajegede/supportmesh) · [官网](https://supportmesh-agent.vercel.app) · 个人维护

**面向 AI/自动化来源工单的多租户支持运营平台**

基于 Next.js 16、Mastra、Convex、Kinde、Resend 构建的工单支持平台：工单可经 Web 表单、REST API 或 MCP 工具调用提交，由运行 Claude Haiku 的 Mastra 分诊 Agent 自动分类、定优先级、评分情绪、检索组织知识库、起草回复并检测是否需升级。多租户隔离贯穿全栈：Kinde 的 org_code 经 JWT 传递，Convex 在查询层强制校验，每组织可生成密码学绑定的 API key。还提供 Slack 通知、白标品牌、每日汇总 Agent 与外部 MCP 服务器。需自行部署，依赖 Node.js 22+、Kinde/Convex/Anthropic API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Haiku 分诊 Agent 自动分类/定级/情绪评分/起草回复
- org_code 贯穿 JWT→工具调用→Convex 查询的多租户隔离
- /api/mcp MCP 服务器暴露工单工具供外部 AI agent 调用
- 每组织独立 API key，服务端密码学绑定组织

## 适用场景

- 团队把 CI、监控和 AI 编码助手的告警作为工单来源统一处理
- 多产品/多客户组织在一账号下隔离管理工单与知识库
- 让外部 AI agent 通过 MCP 提交和查询工单

## 场景标签

 · 领域:企业服务/支持运营

## 证据(README 行号)

> L7: SupportMesh is support infrastructure for teams where tickets come from AI agents and automated systems, not just pe
> L30: - **AI triage** — every ticket is automatically classified (billing, technical, account, feature_request, general),

## 星数曲线

```mermaid
xychart-beta
    title "sholajegede/supportmesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `66e1734afefc` · [字段定义](../../DATASET.md)*
