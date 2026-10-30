# currents-dev/currents-mcp

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/currents-dev/currents-mcp) · [官网](https://currents.dev) · 组织维护

**让 AI 编码 agent 读取 CI 测试结果的 MCP 服务器**

Currents 官方的 MCP Server，把 Currents CI 测试平台的能力暴露给 Cursor、Claude Code、GitHub Copilot 等编码 agent：查询运行、spec 文件与单测结果，聚合错误趋势与性能指标，管理隔离规则与 webhook，从失败测试生成含错误、步骤与 trace 证据的修复上下文，并可创建 Jira 工单与共享证据链接。附 3 个多步工作流 Skills。支持 stdio 本地运行（npx）、托管 HTTP 端点与 Docker 自托管，需 Currents API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40+ MCP 工具覆盖运行查询、错误分析、隔离规则、webhook、Jira 集成
- 失败测试上下文工具返回错误、步骤与文件，供 agent 修复
- 3 个 agent Skills（修复失败测试、收集证据、浏览器取证），以 MCP resource 发布
- 支持 stdio 本地运行、托管 HTTP 端点与 Docker 自托管

## 适用场景

- 在编辑器内让 AI agent 诊断并修复 CI 中失败的测试
- 让 agent 基于真实执行数据分析 flaky 测试与错误趋势
- 通过 agent 编程式管理隔离规则、webhook 与项目设置

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Give your AI coding agents full visibility into your CI test results. The Currents MCP Server connects tools like Cu
> L107: claude mcp add --transport stdio currents --env CURRENTS_API_KEY=<KEY> -- npx -y @currents/mcp
> L141: In addition to the local stdio transport above, the same server can run as a hosted

## 星数曲线

```mermaid
xychart-beta
    title "currents-dev/currents-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `765cd2be3816` · [字段定义](../../DATASET.md)*
