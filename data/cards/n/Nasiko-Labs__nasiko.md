# Nasiko-Labs/nasiko

⭐ 11,930 · Rust · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/Nasiko-Labs/nasiko) · [官网](https://www.nasiko.com) · 组织维护

**AI Agent 开放运行时：统计开销、路由模型、部署治理**

以单一服务器进程形式运行的 Agent 运行时，定位在 Agent 调用链路上：发现机器上的 Claude Code、Codex、OpenCode、Cursor CLI 并汇总其 token 与成本；提供 LLM Router（Agent 只持短期 token，不持真实 API key）、按 Agent/模型的成本归因、OTel 全链路追踪；治理侧含 MCP Gateway、访问控制、人工审批与流程防护；支持部署任意 A2A v1.0 Agent。服务器需 Docker Compose 运行，状态存于 Postgres、Redis、S3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发现本机 coding agent 并把 token 与成本汇入单一仪表盘
- LLM Router：Agent 获取短期 token，密钥在服务器端解析
- MCP Gateway 统一发放工具，凭据留在网关侧
- 人工审批（ask）与深度/扇出/预算/循环等流程防护

## 适用场景

- 统计团队各 coding agent 在各模型上的花费
- 用自己的模型 key 驱动现有 coding agent
- 部署自研 A2A Agent 并控制其工具权限与预算

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Nasiko is the OpenRuntime for AI agents.**
> L4: See every coding agent your team runs and what it costs. Route it to the models you choose. Then deploy and govern y
> L50: |**LLM Router**|Agents get a short-lived token, never a real API key. Provider, model and key are resolved on the s

## 星数曲线

```mermaid
xychart-beta
    title "Nasiko-Labs/nasiko 星数(近 25 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26"]
    y-axis "stars" 9201 --> 12218
    line [9457, 9454, 9452, 9502, 9506, 10189, 10584, 10771, 10903, 11339, 9454, 11945, 11967, 11962, 11957, 11950, 11942, 11932, 11951, 11958, 11957, 11955, 11948, 11938, 11930]
```

2026-10-24 9,457 → 2026-11-26 11,930（+2,473）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e922c33bb7ef` · [字段定义](../../DATASET.md)*
